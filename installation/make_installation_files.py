#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:26:22 2019

@author: wincrantu
"""

from os import path
import sys

from config import ReadSetting


class Installation:
    def __init__(self):
        pass

    def main(self):
        self.INSTALL_SH_DIRNAME = sys.argv[1]
        self.setting = ReadSetting(self.INSTALL_SH_DIRNAME)
        self.dir_name = path.dirname(path.abspath(__file__))
        self.make_crontab()
        self.make_smartrc_file()

    def make_crontab(self):
        smartrc_bot_crontab = (r"@reboot python3 "
                               r"{install_sh_dirname}/src/run.py"
                               r" >> {install_sh_dirname}/log/"
                               r"smartrc_bot_$(date +\%Y\%m\%d_\%H\%M\%S).log"
                               r" 2>&1")
        pigpiod_crontab = [r"@reboot until "
                           "echo 'm {playback} w   w {playback} 0"
                           "".format(playback=self.setting.gpio_playback),
                           r"' > /dev/pigpio; do sleep 1s; done"]
        if self.setting.mode:
            pigpiod_crontab.insert(1, r"   m {record} r   pud {record} u"
                                   "".format(record=self.setting.gpio_record))
        smartrc_bot_crontab =\
            smartrc_bot_crontab.format(
                    install_sh_dirname=self.INSTALL_SH_DIRNAME)

        with open(path.join(self.dir_name, "smartrc_bot.crontab"), "w") as f1:
            f1.write(smartrc_bot_crontab)
            f1.write("\n")
        print(smartrc_bot_crontab)

        with open(path.join(self.dir_name, "pigpiod.crontab"), "w") as f3:
            # f3.write(r"@reboot pigpiod")
            # f3.write("\n")
            for pc in pigpiod_crontab:
                f3.write(pc)
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
