#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 22:22:08 2018

@author: crantu
"""

import requests
from os import path

from get_latest_irrp_2_json import get_latest_irrp_2_json


def main(slack_token, channel_id, smartrc_dir):
    filename = get_latest_irrp_2_json(smartrc_dir)
    files = {'file': open(filename, 'r')}
    param = {
        'token': slack_token,
        'channels': channel_id,
        'filename': path.basename(filename),
        'title': "The backup file of irrp_2.json"
    }
    requests.post(url="https://slack.com/api/files.upload",
                  params=param, files=files)
