#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 22:19:28 2019

@author: crantu
"""


class SlackTokenAuthError(Exception):
    """Exception raised for errors in the slack token.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message


class SlackError(Exception):
    """Exception raised for errors in the slack token.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, received_json):
        self.received_json = received_json


class SlackClassNotFound(Exception):
    """Exception raised for errors that slack class was not found.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message
