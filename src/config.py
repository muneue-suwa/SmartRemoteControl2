#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 09:25:09 2018

@author: wincrantu
"""


import configparser
from os import path


class ReadSetting:
    def __init__(self, smartrc_dir):
        config = configparser.ConfigParser()
        setting_filename =\
            path.join(smartrc_dir, "setting/.smartrc.cfg")
        config.read(setting_filename)
        self.slack_token = config["SLACK"]["SLACK_API_TOKEN"]
        self.channel_id = config["SLACK"]["CHANNEL_ID"]
        self.location = config["BASIC"]["LOCATION"]
        self.mode = bool(config["BASIC"]["is_WITH_RECODER"])
        self.default_reply = config["SLACKBOT"]["DEFAULT_REPLY"]
        if self.mode:
            self.gpio_record = int(config["GPIO"]["RECORD"])
        self.gpio_playback = int(config["GPIO"]["PLAYBACK"])

    def show(self):
        print("self.slack_token: {}".format(self.slack_token))
        print("self.channel_id: {}".format(self.channel_id))
        print("self.location: {}".format(self.location))


# class InitializeSetting:
#     def __init__(self, smartrc_dir):
#         old_setting_filename =\
#             path.join(smartrc_dir, "setting/smartrc.cfg")
#         if not path.isfile(old_setting_filename):
#             raise FileNotFoundError("setting/smartrc.cfg is not found")
#         self.config = configparser.ConfigParser()
#
#         self.new_setting_filename =\
#             path.join(smartrc_dir, "setting/.smartrc.cfg")
#
#         self.config.read(old_setting_filename)
#         self.slack_token = self.config["SLACK"]["SLACK_API_TOKEN"]
#
#     def write_channel_id(self, channel_id):
#         self.config["SLACK"]["CHANNEL_ID"] = channel_id
#         with open(self.new_setting_filename, 'w') as configfile:
#             self.config.write(configfile)


if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    rs = ReadSetting(smartrc_dir)
    rs.show()
