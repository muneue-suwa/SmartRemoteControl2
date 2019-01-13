#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 21:59:42 2018

@author: crantu
"""


from os import path
from datetime import datetime

from irrp_with_class import IRRP


def main(gpio_num, record_id, smartrc_dir):
    str_datetime = datetime.strftime(datetime.today(), "%Y%m%d_%H%M%S")
    filename = path.join(smartrc_dir,
                         "data/smartrc_{}.irrp".format(str_datetime))
    irrp = IRRP(gpio=gpio_num, filename=filename, post=130, no_confirm=True)
    irrp.record(record_id)


if __name__ == "__main__":
    main()
