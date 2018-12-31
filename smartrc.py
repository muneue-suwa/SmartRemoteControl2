#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 09:12:02 2018

@author: wincrantu
"""


from os import path
from slackclient import SlackClient
from setting.read_cfg import ReadSetting, InitializeSetting

from smartrc_slackbot.src import record, playback


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
        self.make_slackbot_settings()
        msg =\
            "{} was added in '# smartrc' channel".format(self.setting.location)
        self.send_a_message(msg)

    def get_smartrc_channel_id(self, sc_class):
        channels_list = sc_class.api_call("channels.list")
        for channel in channels_list["channels"]:
            if channel["name"] == "smartrc":
                return channel["id"]

    def make_slackbot_settings(self):
        filename =\
            path.join(self.smartrc_dir,
                      "smartrc_slackbot/slackbot_settings.py")
        msg = ("#!/usr/bin/env python3\n"
               "# -*- coding: utf-8 -*-\n\n"
               'API_TOKEN = "{api_token}"\n'
               'DEFAULT_REPLY = "{default_reply}"\n'
               'PLUGINS = ["src"]\n')
        with open(filename, "w", encoding="utf-8") as f:
            f.write(msg.format(api_token=self.setting.slack_token,
                               default_reply=self.setting.default_reply))

    def send_a_message(self, text):
        self.sc.api_call(
          "chat.postMessage",
          channel=self.setting.channel_id,
          text=text
        )

    def learn(self, record_id):
        record.main(gpio_num=self.setting.gpio_record,
                    record_id=record_id,
                    smartrc_dir=self.smartrc_dir)

    def send(self, playback_id):
        playback.main(gpio_num=self.setting.gpio_record,
                      playback_id=playback_id,
                      smartrc_dir=self.smartrc_dir)

if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    smartrc = SmartRemoteControl(smartrc_dir)
    smartrc.init()
