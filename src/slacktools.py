#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 09:41:35 2019

@author: crantu
"""


class SlackTools:
    def __init__(self, slack_client_class, channel_id):
        self.sc = slack_client_class
        self.channel_id = channel_id

    def send_a_message(self, text):
        self.sc.api_call(
          "chat.postMessage",
          channel=self.channel_id,
          text=text
        )
