#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 09:12:02 2018

@author: wincrantu
"""


from os import path
from slackclient import SlackClient
from read_cfg import ReadSetting, InitializeSetting


class SmartRemoteControl:
    def __init__(self, smartrc_dir):
        self.smartrc_dir = smartrc_dir
        setting_filename =\
            path.join(smartrc_dir, "setting/.smartrc.cfg")
        if path.isfile(setting_filename):
            self.read_setting()

    def read_setting(self):
        self.setting = ReadSetting(smartrc_dir)
        self.sc = SlackClient(self.setting.slack_token)

    def init(self):
        init_setting = InitializeSetting(self.smartrc_dir)
        init_sc = SlackClient(init_setting.slack_token)
        channel_id = self.get_smartrc_channel_id(init_sc)
        init_setting.write_channel_id(channel_id)
        self.read_setting()
        msg =\
            "{} was added in '# smartrc' channel".format(self.setting.location)
        self.send_a_message(msg)

    def get_smartrc_channel_id(self, sc_class):
        channels_list = sc_class.api_call("channels.list")
        for channel in channels_list["channels"]:
            if channel["name"] == "smartrc":
                return channel["id"]

    def send_a_message(self, text):
        self.sc.api_call(
          "chat.postMessage",
          channel=self.setting.channel_id,
          text=text
        )


if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    smartrc = SmartRemoteControl(smartrc_dir)
    smartrc.init()
