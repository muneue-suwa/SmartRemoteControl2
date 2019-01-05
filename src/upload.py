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

from get_latest_irrp_2_json import get_latest_irrp_2_json


class Upload:
    def __init__(self, slack_client_class, setting_class, smartrc_dir):
        self.sc = slack_client_class
        self.setting = setting_class
        self.smartrc_dir = smartrc_dir

    def upload_text(self):
        filename = path.join(get_latest_irrp_2_json(self.smartrc_dir))
        with open(filename, "r") as irrp_2:
            json_file = json.load(irrp_2)
            string = str(json_file).replace("'", '"').replace(" ", "")

        string_len = len(string)
        for i in range(floor(string_len/1024)):
            print(string[:1024])
            string = string[1024:]
        print(string)

    def upload_file(self, channel_id, smartrc_dir):
        filename = path.join(get_latest_irrp_2_json(self.smartrc_dir))
        files = {'file': open(filename, 'r')}
        param = {
            'token': self.setting.slack_token,
            'channels': self.setting.channel_id,
            'filename': path.basename(filename),
            'title': "The backup file of irrp_2.json"
        }
        requests.post(url="https://slack.com/api/files.upload",
                      params=param, files=files)


if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    upload = Upload("For", "Debug", smartrc_dir)
    upload.upload_text()
