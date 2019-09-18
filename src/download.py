#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 18:09:27 2019

@author: crantu
"""

from os import path


class DownloadText:
    def __init__(self, smartrc_dir, timeout_sec=300):
        self.timeout = timeout_sec
        self.smartrc_dir = smartrc_dir
        self.initialization()

    def initialization(self):
        self.filename = ""
        self.lines = []
        self.figure = -1
        self.dl_start_time = -1

    def dl_start(self, filename):
        self.filename = filename
        self.dl_start_time = 0
        return True

    def dl_continue(self, filename, line, figure):
        self.figure += 1
        if not self.check_filename_figure(filename, figure):
            return False
        self.lines.append(line)
        print("Recieved text: {}".format(line))
        return True

    def dl_end(self, filename, figure):
        if not self.check_filename_figure(filename, figure):
            return False
        with open(path.join(self.smartrc_dir, "data", self.filename),
                  "w") as new_irrp:
            for line in self.lines:
                new_irrp.write(line)
        print("{} was successfully downloaded".format(self.filename))
        self.initialization()
        return True

    def check_filename_figure(self, filename, figure):
        if self.figure < 0:
            return False
        elif self.filename != filename:
            print("Filename Error: DownloadText")
            self.initialization()
            return False
        elif self.figure != int(figure):
            print("Data figure Error: DownloadText")
            self.initialization()
            return False
        return True

    def check_timeout(self):
        if self.dl_start_time > -1:
            self.dl_start_time += 1
            if self.dl_start_time > self.timeout:
                print("Timeout: DownloadText")
                self.initialization()
