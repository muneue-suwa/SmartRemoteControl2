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

from smartrc import SmartRemoteControl


class RunSmartrcBot(SmartRemoteControl):
    def __init__(self, smartrc_dir):
        super().__init__(smartrc_dir)
        if not self.is_settingfile:
            raise FileNotFoundError("smartrc setting file is not found")
        self.smartrc_pattern = re.compile(r'smartrc.*')

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
                            print("msg_raw:", msg)
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
        if self.smartrc_pattern.match(message):
            splited_msg = message.split()
            try:
                if splited_msg[1] == "send" or splited_msg[1] == "playback":
                    self.print_std_sc(self.send(playback_id=splited_msg[2]))
                elif splited_msg[1] == "list":
                    self.print_std_sc(self.show_id_list())
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
        responce = requests.post(url="https://slack.com/api/chat.postMessage",
                                 params=param)
        print("Connected to slack")
        print(param)
        print("Connected to slack")
        return responce


if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    bot = RunSmartrcBot(smartrc_dir)
    bot.main()
