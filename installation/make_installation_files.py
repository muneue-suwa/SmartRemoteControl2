#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:26:22 2019

@author: wincrantu
"""

from os import path
import sys


class Installation:
    def __init__(self):
        pass

    def main(self):
        self.INSTALL_SH_DIRNAME = sys.argv[1]
        self.dir_name = path.dirname(path.abspath(__file__))
        self.make_crontab()
        self.make_smartrc_file()

    def make_crontab(self):
        smartrc_bot_crontab = (r"@reboot python3 "
                               r"{install_sh_dirname}/src/run.py"
                               r" >> {install_sh_dirname}/log/"
                               r"smartrc_bot_$(date +\%Y\%m\%d_\%H\%M\%S).log"
                               r" 2>&1")
        pigpiod_crontab = (r"@reboot pigpiod"
                           r" > {install_sh_dirname}/log/"
                           r"start_pigpiod_$(date +\%Y\%m\%d_\%H\%M\%S).log"
                           r" 2>&1")

        smartrc_bot_crontab =\
            smartrc_bot_crontab.format(
                    install_sh_dirname=self.INSTALL_SH_DIRNAME)
        pigpiod_crontab = pigpiod_crontab.format(
                install_sh_dirname=self.INSTALL_SH_DIRNAME)

        with open(path.join(self.dir_name, "smartrc_bot.crontab"), "w") as f1:
            f1.write(smartrc_bot_crontab)
            f1.write("\n")
        print(smartrc_bot_crontab)

        with open(path.join(self.dir_name, "pigpiod.crontab"), "w") as f3:
            f3.write(pigpiod_crontab)
            f3.write("\n")
        print(pigpiod_crontab)

    def make_smartrc_file(self):
        smartrc_lines = ["#!/bin/bash\n",
                         "python3 {install_sh_dirname}/src/smartrc.py $@"
                         "".format(install_sh_dirname=self.INSTALL_SH_DIRNAME)]

        with open(path.join(self.dir_name, "smartrc"), "w") as f2:
            for line in smartrc_lines:
                f2.write(line)
                f2.write("\n")
                print(line)


if __name__ == "__main__":
    ist = Installation()
    ist.main()
