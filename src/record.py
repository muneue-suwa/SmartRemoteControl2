#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 21:59:42 2018

@author: crantu
"""

from .irrp_2 import IRRP2
from os import path


def main(gpio_num, record_id, smartrc_dir):
    filename = path.join(smartrc_dir, "data/irrp_2.json")
    irrp2 = IRRP2(PLAY=False, RECORD=True,
                  GPIO=gpio_num, FILE=filename, ID=record_id,
                  NO_CONFIRM=True, POST_MS=130)
    irrp2.main()


if __name__ == "__main__":
    main()
