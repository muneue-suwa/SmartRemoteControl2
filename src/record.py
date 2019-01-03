#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 21:59:42 2018

@author: crantu
"""


from os import path
from datetime import datetime

from irrp_2 import IRRP2


def main(gpio_num, record_id, smartrc_dir):
    str_datetime = datetime.strftime(datetime.today(), "%Y%m%d_%H%M%S")
    filename = path.join(smartrc_dir,
                         "data/irrp_2_{}.json".format(str_datetime))
    irrp2 = IRRP2(PLAY=False, RECORD=True,
                  GPIO=gpio_num, FILE=filename, ID=record_id,
                  NO_CONFIRM=True, POST_MS=130)
    irrp2.main()


if __name__ == "__main__":
    main()
