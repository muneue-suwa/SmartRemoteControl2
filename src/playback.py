#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 22:16:48 2018

@author: crantu
"""

from irrp_2 import IRRP2
from os import path


def main(gpio_num, playback_id, smartrc_dir):
    filename = path.join(smartrc_dir, "data/irrp_2.json")
    irrp2 = IRRP2(PLAY=True, RECORD=False,
                  GPIO=gpio_num, FILE=filename, ID=playback_id)
    irrp2.main()


if __name__ == "__main__":
    main()
