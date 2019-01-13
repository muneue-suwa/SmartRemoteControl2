#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 22:36:06 2018

@author: crantu
"""


from time import sleep
from os import path
import re

from smartrc import SmartRemoteControl


class RunSmartrcBot(SmartRemoteControl):
    def __init__(self, smartrc_dir):
        super().__init__(smartrc_dir)
        if not self.is_settingfile:
            raise FileNotFoundError("smartrc setting file is not found")
        self.smartrc_pattern = re.compile(r'smartrc.*')
        # self.commands = ["backup", "share", "send", "playback",
        #                  "learn", "record", "recovery", "init", "update"]

    def main(self):
        if self.sc.rtm_connect():
            while self.sc.server.connected is True:
                try:
                    msg = self.sc.rtm_read()
                    print("msg_raw:", msg)
                    if "text" in msg[0]:
                        print("msg_human:", msg[0]["text"])
                        self.analyze_message(msg[0]["text"])
                    elif "attachments" in msg[0]:
                        print("msg_bot:", msg[0]["attachments"][0]["fallback"])
                        self.analyze_message(msg[0]["attachments"][0]["fallback"])
                except IndexError:
                    pass
                except KeyError:
                    pass
                finally:
                    sleep(1)
        else:
            print("Connection Failed")

    def analyze_message(self, message):
        if self.smartrc_pattern.match(message):
            print(message)
            splited_msg = message.split()
            try:
                if splited_msg[1] == "backup":
                    pass
                elif splited_msg[1] == "share":
                    pass
                elif splited_msg[1] == "send" or splited_msg[1] == "playback":
                    if splited_msg[2] in self.irrpfile.get_id_list():
                        self.send(playback_id=splited_msg[2])
                elif splited_msg[1] == "learn" or splited_msg[1] == "record":
                    pass
                elif splited_msg[1] == "recovery":
                    pass
                elif splited_msg[1] == "init":
                    pass
                elif splited_msg[1] == "update":
                    pass
            except IndexError:
                pass


if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    bot = RunSmartrcBot(smartrc_dir)
    bot.main()
