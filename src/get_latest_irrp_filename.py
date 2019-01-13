#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:55:57 2019

@author: wincrantu
"""


from glob import glob
from os import path
from datetime import datetime


def get_latest_irrp_filename(smartrc_dir):
    filenames = glob(path.join(smartrc_dir, "data/smartrc_*.irrp"))
    datetime_list = []
    for filename in filenames:
        datetime_list.append(datetime.strptime(path.basename(filename),
                                               "smartrc_%Y%m%d_%H%M%S.irrp"))
    if not len(datetime_list) > 0:
        print("No data file")
        return None

    str_datetime = datetime.strftime(max(datetime_list), "%Y%m%d_%H%M%S")
    return path.join(smartrc_dir, "data/smartrc_{}.irrp".format(str_datetime))


if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    print(get_latest_irrp_filename(smartrc_dir))
