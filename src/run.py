#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 22:36:06 2018

@author: crantu
"""


from time import sleep
from os import path

from smartrc import SmartRemoteControl


class RunSmartrcBot(SmartRemoteControl):
    def __init__(self, smartrc_dir):
        super().__init__(smartrc_dir)

    def main(self):
        if self.sc.rtm_connect():
            while self.sc.server.connected is True:
                print(self.sc.rtm_read())
                sleep(1)
        else:
            print("Connection Failed")


if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    bot = RunSmartrcBot(smartrc_dir)
    bot.main()
