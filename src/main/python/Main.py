#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2018-2023 Denis Meyer
#
# This file is part of the Burnbutton.
#

"""Burnbutton - Main"""

import os
import logging

from lib.AppConfig import AppConfig
from gui.MainGui import GUI

def _initialize_logger():
    logging_loglevel = logging.DEBUG
    logging_datefmt = '%d-%m-%Y %H:%M:%S'
    logging_format = '[%(asctime)s] [%(levelname)-5s] [%(module)-20s:%(lineno)-4s] %(message)s'
    logging.basicConfig(level=logging_loglevel,
                        format=logging_format,
                        datefmt=logging_datefmt)

if __name__ == '__main__':
    print('Current working directory: {}'.format(os.getcwd()))

    _initialize_logger()

    basedir = os.path.dirname(__file__)

    appconfig = AppConfig()
    gui = GUI(appconfig, basedir)
    gui.run()
