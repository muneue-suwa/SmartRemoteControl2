#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:26:22 2019

@author: dongsiku
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
        self.make_smartrc_completion()

    def make_crontab(self):
        smartrc_bot_crontab = (r"@reboot python3 "
                               r"{install_sh_dirname}/src/run.py "
                               r"{install_sh_dirname}"
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
            for pc in pigpiod_crontab:
                f3.write(pc)
            f3.write("\n")
        print(pigpiod_crontab)

    def make_smartrc_file(self):
        smartrc_lines = ["#!/bin/bash\n",
                         "python3 {install_sh_dirname}/src/smartrc.py "
                         "{install_sh_dirname} $@"
                         "".format(install_sh_dirname=self.INSTALL_SH_DIRNAME)]

        with open(path.join(self.dir_name, "smartrc"), "w") as f2:
            for line in smartrc_lines:
                f2.write(line)
                f2.write("\n")
                print(line)

    def make_smartrc_completion(self):
        default_filename = path.join(self.INSTALL_SH_DIRNAME,
                                     "smartrc_completion.d",
                                     "smartrc_completion.default")
        new_filename = path.join(self.INSTALL_SH_DIRNAME,
                                 "smartrc_completion.d",
                                 "smartrc_completion")
        smartrc_completion_elements_filename =\
            path.join(self.INSTALL_SH_DIRNAME,
                      "smartrc_completion.d",
                      "smartrc_completion_elements")

        with open(default_filename, "r") as default_file:
            lines = default_file.readlines()
            with open(new_filename, "w") as new_file:
                new_file.write("#!/bin/bash\n\n")
                new_file.write("SMARTRC_COMPLETION_ELEMENTS_FILENAME=")
                new_file.write('"')
                new_file.write(smartrc_completion_elements_filename)
                new_file.write('"\n\n')
                for line in lines:
                    new_file.write(line)
                    print(line, end="")


if __name__ == "__main__":
    ist = Installation()
    ist.main()
