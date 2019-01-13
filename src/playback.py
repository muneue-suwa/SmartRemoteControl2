#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 22:16:48 2018

@author: crantu
"""

from irrp_with_class import IRRP
from os import path

from get_latest_irrp_filename import IRRPFile


def main(gpio_num, playback_id, smartrc_dir):
    irrpfile = IRRPFile(smartrc_dir=smartrc_dir)
    filename = path.join(irrpfile.get_latest_filename())
    irrp = IRRP(gpio=gpio_num, filename=filename)
    irrp.playback(playback_id)


if __name__ == "__main__":
    main()
