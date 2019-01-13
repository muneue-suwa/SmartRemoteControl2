#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 09:45:25 2019

@author: crantu
"""

import requests
from os import path
from datetime import datetime
import json
from math import floor

from slacktools import SlackTools
<<<<<<< HEAD
from get_latest_irrp_filename import IRRPFile
=======
from irrp_file import IRRPFile
>>>>>>> Add irrp_file.py and move features of record and playback to smartrc.py


class Upload:
    def __init__(self, slack_client_class, setting_class, smartrc_dir):
        self.sc = slack_client_class
        self.setting = setting_class
        # self.smartrc_dir = smartrc_dir
        self.stool = SlackTools(self.sc, self.setting.channel_id)
        self.irrpfile = IRRPFile(smartrc_dir=smartrc_dir)

    def upload_text(self):
        filename = path.join(self.irrpfile.get_latest_filename())
        with open(filename, "r") as irrp_2:
            json_file = json.load(irrp_2)
            string = str(json_file).replace("'", '"').replace(" ", "")

        string_len = len(string)
        for i in range(floor(string_len/1024)):
            print(string[:1024])
            self.stool.send_a_message(string[:1024])
            string = string[1024:]
        print(string)
        self.stool.send_a_message(string)

    def upload_file(self, channel_id):
        filename = path.join(self.irrpfile.get_latest_filename())
        files = {'file': open(filename, 'r')}
        param = {
            'token': self.setting.slack_token,
            'channels': self.setting.channel_id,
            'filename': path.basename(filename),
            'title': "The backup file of smartrc.irrp"
        }
        requests.post(url="https://slack.com/api/files.upload",
                      params=param, files=files)


if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    upload = Upload("For", "Debug", smartrc_dir)
    upload.upload_text()
