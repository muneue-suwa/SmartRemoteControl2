#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 09:41:35 2019

@author: crantu
"""


class SendMessageToSlack:
    def __init__(self, slack_client_class):
        self.sc = slack_client_class

    def send_a_message(self, text):
        self.sc.api_call(
          "chat.postMessage",
          channel=self.setting.channel_id,
          text=text
        )
