#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2018-2023 Denis Meyer
#
# This file is part of the Burnbutton.
#

"""Burnbutton - GUI"""

import logging
import sys

from PyQt5 import QtWidgets

from lib.ImageCache import ImageCache
from lib.SoundCache import SoundCache
from gui.components.MainWindow import MainWindow

class GUI():
    """Main GUI"""

    def __init__(self, appconfig, basedir):
        """Initializes the GUI

        :param basedir: The base directory
        :param appconfig: The AppConfig
        """
        logging.debug('Initializing MainGUI')

        self.appconfig = appconfig
        self.basedir = basedir

        self.image_cache = ImageCache(self.basedir)
        self.sound_cache = SoundCache(self.basedir)

    def run(self):
        """Initializes and shows the GUI"""
        logging.debug('Initializing Main GUI')

        app = QtWidgets.QApplication(sys.argv)

        self.main_window = MainWindow(self.appconfig, self.image_cache, self.sound_cache)
        self.main_window.init_ui()
        self.main_window.show()

        app.exec()

        sys.exit(0)
