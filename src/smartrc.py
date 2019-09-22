# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 09:12:02 2018

@author: dongsiku
"""


from os import path
from slackclient import SlackClient
import argparse
import sys

from config import ReadSetting
from slacktools import SlackTools
from irrp_file import IRRPFile
from exceptions import SlackClassNotFound, SlackTokenAuthError, SlackError
from gdrive import GDrive

from irrp_with_class import IRRP


class SmartRemoteControl:
    def __init__(self, smartrc_dir=None):
        if smartrc_dir is None:
            self.SMARTRC_DIR = sys.argv[1]
        else:
            self.SMARTRC_DIR = smartrc_dir
        setting_filename =\
            path.join(self.SMARTRC_DIR, "setting/.smartrc.cfg")
        self.is_settingfile = False
        if path.isfile(setting_filename):
            self.read_setting()
            self.is_settingfile = True
            self.irrpfile = IRRPFile(smartrc_dir=self.SMARTRC_DIR)
            self.gdrive = GDrive(smartrc_dir=self.SMARTRC_DIR)

    def read_setting(self):
        self.setting = ReadSetting(self.SMARTRC_DIR)
        self.sc = SlackClient(self.setting.slack_token)
        self.stool = SlackTools(self.sc, self.setting)
        self.smartrc_commands = ["backup", "send", "playback",
                                 "learn", "record", "recovery", "update"]
        if self.setting.mode is True:
            self.smartrc_commands.append("share")
        self.smartrc_commands.sort()

    def get_smartrc_channel_id(self, sc_class):
        channels_list = sc_class.api_call("channels.list")
        if channels_list["ok"] is False:
            if channels_list["error"] == "invalid_auth":
                raise SlackTokenAuthError("Invalid authorization")
            else:
                raise SlackError(channels_list)
        for channel in channels_list["channels"]:
            if channel["name"] == "smartrc":
                return channel["id"]
        raise SlackClassNotFound("The channel '# smartrc' was not found")
        # If Internet was not connected: requests.exceptions.ConnectionError

    def record(self, record_id):
        print(self.arguments.command[0])
        if record_id is None:
            record_id = self.rcd_ply_common()
        irrp = IRRP(gpio=self.setting.gpio_record,
                    filename=self.irrpfile.get_new_filename(),
                    post=130, no_confirm=True)
        irrp.record(record_id)

    def playback(self, playback_id):
        self.update_id_list()
        if playback_id is None:
            self.rcd_ply_common()
        try:
            filename = self.irrpfile.get_latest_filename()
            if playback_id in self.id_list:
                irrp = IRRP(gpio=self.setting.gpio_playback,
                            filename=filename)
                irrp.playback(playback_id)
            return "Sending {}".format(playback_id)
        except FileNotFoundError as err:
            return err

    def share(self):
        if self.setting.mode is True:
            self.gdrive.upload()
            self.stool.send_a_message("smartrc download_irrp_files")
        else:
            print("The mode is onlyPlayback")

    def update_id_list(self):
        try:
            self.id_list = self.irrpfile.get_id_list()
        except FileNotFoundError as err:
            return err

    def update_smatrc_completion_elements(self):
        self.update_id_list()
        smartrc_completion_elements_filename =\
            path.join(self.SMARTRC_DIR,
                      "smartrc_completion.d",
                      "smartrc_completion_elements")
        with open(smartrc_completion_elements_filename, "w")\
                as smartrc_completion_elements:
            smartrc_completion_elements.write("#!/bin/bash\n\n")
            smartrc_completion_elements.write("SMARTRC_COMMANDS=")
            smartrc_completion_elements.write('"')
            for smartrc_command in self.smartrc_commands:
                smartrc_completion_elements.write(smartrc_command)
                smartrc_completion_elements.write(" ")
            smartrc_completion_elements.write('"\n')
            smartrc_completion_elements.write("RCD_PLY_ID=")
            smartrc_completion_elements.write('"')
            for id_l in self.id_list:
                smartrc_completion_elements.write(id_l)
                smartrc_completion_elements.write(" ")
            smartrc_completion_elements.write('"\n')

    def get_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("smartrc_dir", nargs=1, type=str,
                            help=argparse.SUPPRESS)
        parser.add_argument("command", nargs=1, type=str,
                            choices=self.smartrc_commands,
                            help="startrc command")
        parser.add_argument("record_playback_id", nargs="?", type=str,
                            default=None,
                            help="record or playback id")
        self.arguments = parser.parse_args()

    def main(self):
        self.update_smatrc_completion_elements()
        self.get_arguments()
        command = self.arguments.command[0]
        if self.arguments.record_playback_id:
            if command not in ["send", "playback", "learn", "record"]:
                print("The argument '{}' "
                      "was ignored".format(self.arguments.record_playback_id))
        if command == "backup":
            self.gdrive.upload()
        elif command == "share" or command == "update":
            self.share()
        elif command == "send" or command == "playback":
            self.playback(None)
        elif command == "learn" or command == "record":
            self.record(None)
        elif command == "recovery":
            self.gdrive.download()

    def rcd_ply_common(self):
        rcd_ply_mode_str = self.arguments.command[0]
        rcd_ply_id = self.arguments.record_playback_id
        if not rcd_ply_id:
            if rcd_ply_mode_str == "send" or rcd_ply_mode_str == "playback":
                if len(self.id_list) < 1:
                    print("No recorded ID")
                    return False
                else:
                    print(self.id_list)
            elif rcd_ply_mode_str != "learn" and rcd_ply_mode_str != "record":
                return False
            rcd_ply_id = input("Input {} ID: ".format(rcd_ply_mode_str))

        if rcd_ply_mode_str == "send" or rcd_ply_mode_str == "playback":
            if rcd_ply_id not in self.id_list:
                print("No recorded ID: {}".format(rcd_ply_id))
                return False
        id_yn = input("Are you sure"
                      " to decide the {} id?:"
                      " {} (y/n): ".format(rcd_ply_mode_str, rcd_ply_id))
        if not id_yn.lower() == "y":
            print("Canceled")
            return False

        return rcd_ply_id


if __name__ == "__main__":
    smartrc = SmartRemoteControl()
    smartrc.main()
