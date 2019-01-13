#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:26:22 2019

@author: wincrantu
"""

from os import path
import sys


def make_crontab():
    INSTALL_SH_DIRNAME = sys.argv[1]
    smartrc_bot_crontab = (r"@reboot bash "
                           r"{install_sh_dirname}/src"
                           r" >> {install_sh_dirname}/log/"
                           r"smartrc_bot_$(date +\%Y\%m\%d_\%H\%M\%S).log"
                           r" 2>&1")

    dir_name = path.dirname(path.abspath(__file__))

    smartrc_bot_crontab =\
        smartrc_bot_crontab.format(install_sh_dirname=INSTALL_SH_DIRNAME)

    with open(path.join(dir_name, "smartrc_bot.crontab"), "w") as f1:
        f1.write(smartrc_bot_crontab)
        f1.write("\n")
    print(smartrc_bot_crontab)


if __name__ == "__main__":
    make_crontab()
