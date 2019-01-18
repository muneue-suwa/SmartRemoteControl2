#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 09:45:25 2019

@author: crantu
"""

import requests
from os import path

from slacktools import SlackTools
from irrp_file import IRRPFile


class Upload:
    def __init__(self, slack_client_class, setting_class, smartrc_dir):
        self.sc = slack_client_class
        self.setting = setting_class
        # self.smartrc_dir = smartrc_dir
        self.stool = SlackTools(self.sc, self.setting)
        self.irrpfile = IRRPFile(smartrc_dir=smartrc_dir)

    def upload_text(self):
        """ how to upload text to slack channel
        from_smartrc_bot [filename] START_IRRP_FILE
        from_smartrc_bot [filename] CONTINUE_IRRP_FILE 0
        from_smartrc_bot [filename] CONTINUE_IRRP_FILE 1
        from_smartrc_bot [filename] CONTINUE_IRRP_FILE n
        from_smartrc_bot [filename] END_IRRP_FILE n
        And whitespace will replace to '+'
        """
        descriptions = ["START_IRRP_FILE",
                        "CONTINUE_IRRP_FILE+{line}+{figure}",
                        "END_IRRP_FILE+{figure}"]
        upload_formats = []
        filename = path.join(self.irrpfile.get_latest_filename())
        for description in descriptions:
            upload_formats.append("from_smartrc_bot+{filename}"
                                  "+{description}".format(
                                          filename=path.basename(filename),
                                          description=description))
        with open(filename, "r") as irrp:
            lines = irrp.readlines()
        self.stool.send_a_message(upload_formats[0])
        for i, line in enumerate(lines):
            self.stool.send_a_message(upload_formats[1].format(line=line,
                                                               figure=i))
        self.stool.send_a_message(upload_formats[2].format(figure=i))

    def upload_file(self):
        filename = path.join(self.irrpfile.get_latest_filename())
        files = {'file': open(filename, 'r')}
        param = {
            'token': self.setting.slack_token,
            'channels': self.setting.channel_id,
            'filename': path.basename(filename),
            'title': "The backup file of smartrc.irrp"
        }
        requests.post(url="https://slack.com/api/files.upload",
                      params=param, files=files)


if __name__ == "__main__":
    smartrc_dir = path.expanduser("~/Git/SmartRemoteControl2")
    upload = Upload("For", "Debug", smartrc_dir)
    upload.upload_text()
