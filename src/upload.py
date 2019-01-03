#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 22:22:08 2018

@author: crantu
"""

import requests
from os import path
from datetime import datetime


def main(slack_token, channel_id, smartrc_dir):
    filename = path.join(smartrc_dir, "data/irrp_2.json")
    str_datetime = datetime.strftime(datetime.today(), "%Y%m%d_%H%M%S")

    files = {'file': open(filename, 'r')}
    param = {
        'token': slack_token,
        'channels': channel_id,
        'filename': "irrp_2_{}.json".format(str_datetime),
        'title': "The backup file of irrp_2.json"
    }
    requests.post(url="https://slack.com/api/files.upload",
                  params=param, files=files)
