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
        self.commands = ["backup", "share", "send", "playback",
                         "learn", "record", "recovery", "init", "update"]
        self.command_patterns =\
            {command: re.compile(r'smartrc\s{}\s'.format(command))
                for command in self.commands}

    def main(self):
        if self.sc.rtm_connect():
            while self.sc.server.connected is True:
                try:
                    msg = self.sc.rtm_read()
                    print("msg:", msg[0]["text"])
                    self.analyze_message(msg[0]["text"])
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
            if self.command_patterns["backup"]:
                pass
            elif self.command_patterns["share"]:
                pass
            elif self.command_patterns["send"]:
                pass
            elif self.command_patterns["playback"]:
                pass
            elif self.command_patterns["learn"]:
                pass
            elif self.command_patterns["record"]:
                pass
            elif self.command_patterns["recovery"]:
                pass
            elif self.command_patterns["init"]:
                pass
            elif self.command_patterns["update"]:
                pass


if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    bot = RunSmartrcBot(smartrc_dir)
    bot.main()
