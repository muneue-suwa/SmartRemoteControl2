#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 22:22:08 2018

@author: crantu
"""

import requests
from os import path
from datetime import datetime
import json

from get_latest_irrp_2_json import get_latest_irrp_2_json


def main(slack_token, channel_id, smartrc_dir):
    filename = path.join(get_latest_irrp_2_json(smartrc_dir))
    with open(filename, "r") as irrp_2:
        json_file = json.load(irrp_2)
        string = str(json_file).replace("'", '"').replace(" ", "")
    print("len:", len(string))
    print("string:", string)

    files = {'file': open(filename, 'r')}
    param = {
        'token': slack_token,
        'channels': channel_id,
        'filename': "irrp_2_{}.json".format(str_datetime),
        'title': "The backup file of irrp_2.json"
    }
    requests.post(url="https://slack.com/api/files.upload",
                  params=param, files=files)
