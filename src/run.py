#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 22:36:06 2018

@author: dongsiku
"""


from time import sleep
from os import path
import re
import requests
import json
import sys

from smartrc import SmartRemoteControl
from exceptions import SlackTokenAuthError, SlackError
from gdrive import GDrive


class RunSmartrcBot(SmartRemoteControl):
    def __init__(self, smartrc_dir=None):
        if smartrc_dir is None:
            smartrc_dir = sys.argv[1]
        super().__init__(smartrc_dir)
        if not self.is_settingfile:
            raise FileNotFoundError("smartrc setting file is not found")
        self.smartrc_pattern = re.compile(r'smartrc.*')
        self.gdrive = GDrive(smartrc_dir=smartrc_dir)

    def main(self):
        is_tryConnection = True
        while is_tryConnection:
            is_tryConnection = False
            try:
                self.try_connection()
                if self.sc.rtm_connect(timeout=1):
                    while self.sc.server.connected is True:
                        try:
                            msg = self.sc.rtm_read()
                            # print("msg_raw:", msg)
                            if "text" in msg[0]:
                                message = msg[0]["text"]
                                print("msg:", message)
                                self.analyze_message(message)
                        except IndexError as index_err:
                            pass
                            # print("IndexError: {}".format(index_err))
                        except KeyError as key_err:
                            print("KeyError: {}".format(key_err))
                        except TimeoutError as time_err:
                            print("TimeoutError: {}".format(time_err))
                            sleep(60)
                            is_tryConnection = True
                            break
                        finally:
                            sleep(1)
                else:
                    print("Connection Failed")
            except requests.exceptions.ConnectionError as err:
                print("ConnectionError: {}".format(err))
                sleep(60)
                is_tryConnection = True

    def analyze_message(self, message):
        try:
            if self.smartrc_pattern.match(message):
                splited_msg = message.split()
                if splited_msg[1] == "send" or splited_msg[1] == "playback":
                    self.print_std_sc(self.playback(
                                      playback_id=splited_msg[2]))
                elif splited_msg[1] == "list":
                    self.print_std_sc(self.show_id_list())
                elif splited_msg[1] == "download_irrp_files":
                    print("gdrive downloading...")
                    self.gdrive.download()
        except IndexError:
            pass
            # print("IndexError: {}".format(index_err))

    def print_std_sc(self, message):
        print(message)
        self.stool.send_a_message(message)

    def try_connection(self):
        param = {
            'token': self.setting.slack_token,
            'channel': self.setting.channel_id,
            'text': "{} was connected to slack".format(self.setting.location),
            'as_user': "false",
            'username': self.setting.location
        }
        raw_responce =\
            requests.post(url="https://slack.com/api/chat.postMessage",
                          params=param)
        responce = json.loads(raw_responce.text)
        print("responce :", responce)
        if responce["ok"] is False:
            if responce["error"] == "invalid_auth":
                raise SlackTokenAuthError("Invalid authorization")
            else:
                raise SlackError(responce)
        elif responce["ok"] is True:
            print("Connected to slack")
        return responce


if __name__ == "__main__":
    bot = RunSmartrcBot()
    bot.main()
