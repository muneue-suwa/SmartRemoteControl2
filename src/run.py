#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 22:36:06 2018

@author: crantu
"""


from time import sleep
from os import path
import re
import requests
import json

from smartrc import SmartRemoteControl
from exceptions import SlackTokenAuthError, SlackError
from download import DownloadText


class RunSmartrcBot(SmartRemoteControl):
    def __init__(self, smartrc_dir):
        super().__init__(smartrc_dir)
        if not self.is_settingfile:
            raise FileNotFoundError("smartrc setting file is not found")
        self.smartrc_pattern = re.compile(r'smartrc.*')
        self.fromsmartrcbot_pattern = re.compile(r'from_smartrc_bot.*')
        self.downloadtext = DownloadText(smartrc_dir=smartrc_dir)

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
                            self.downloadtext.check_timeout()
                            if "text" in msg[0]:
                                message = msg[0]["text"]
                                print("msg_human:", message)
                                self.analyze_message(message)
                            elif "attachments" in msg[0]:
                                message = msg[0]["attachments"][0]["fallback"]
                                print("msg_bot:", message)
                                self.analyze_message(message)
                        except IndexError:
                            pass
                        except KeyError:
                            pass
                        except TimeoutError as err:
                            print("TimeoutError: {}".format(err))
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
                    self.print_std_sc(self.send(playback_id=splited_msg[2]))
                elif splited_msg[1] == "list":
                    self.print_std_sc(self.show_id_list())
            elif (not self.setting.mode and
                  self.fromsmartrcbot_pattern.match(message)):
                splited_msg = message.split("+")
                if splited_msg[2] == "START_IRRP_FILE":
                    res = self.downloadtext.dl_start(filename=splited_msg[1])
                elif splited_msg[2] == "CONTINUE_IRRP_FILE":
                    res =\
                        self.downloadtext.dl_continue(filename=splited_msg[1],
                                                      line=splited_msg[-2],
                                                      figure=splited_msg[-1])
                elif splited_msg[2] == "END_IRRP_FILE":
                    res = self.downloadtext.dl_end(filename=splited_msg[1],
                                                   figure=splited_msg[-1])
                print(res)
                # print(splited_msg)
        except IndexError:
            pass

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
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    bot = RunSmartrcBot(smartrc_dir)
    bot.main()
