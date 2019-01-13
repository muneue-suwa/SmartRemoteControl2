#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:55:57 2019

@author: wincrantu
"""


from glob import glob
from os import path
from datetime import datetime


def get_latest_irrp_2_json(smartrc_dir):
    filenames = glob(path.join(smartrc_dir, "data/irrp_2_*.json"))
    datetime_list = []
    for filename in filenames:
        datetime_list.append(datetime.strptime(path.basename(filename),
                                               "irrp_2_%Y%m%d_%H%M%S.json"))
    if not len(datetime_list) > 0:
        print("No data file")
        return None

    str_datetime = datetime.strftime(max(datetime_list), "%Y%m%d_%H%M%S")
    return path.join(smartrc_dir, "data/irrp_2_{}.json".format(str_datetime))


if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    print(get_latest_irrp_2_json(smartrc_dir))
