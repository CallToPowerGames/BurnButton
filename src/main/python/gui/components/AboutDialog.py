#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2018-2023 Denis Meyer
#
# This file is part of the Burnbutton.
#

"""Burnbutton - About dialog"""

import logging

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QDialog, QDesktopWidget, QGridLayout, QLabel

class AboutDialog(QDialog):
    """Main window GUI"""

    def __init__(self, appconfig, image_cache):
        """Initializes the about dialog

        :param appconfig: The AppConfig
        :param image_cache: The image cache
        """
        super().__init__()

        logging.debug('Initializing AboutDialog')

        self.appconfig = appconfig
        self.image_cache = image_cache
        
        self.image_cache.get_or_load_pixmap('img.logo_app', 'logo-app.png')

        self.setModal(True)

    def init_ui(self):
        """Initiates about dialog UI"""
        self.setWindowTitle('About Burnbutton')

        self.resize(450, 210)
        
        self.font_label = QFont()
        self.font_label.setBold(True)

        self._center()
        self._init_ui()

    def _init_ui(self):
        """Initializes the UI"""
        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.label_empty = QLabel(' ')
        self.label_author = QLabel('Author')
        self.label_author.setFont(self.font_label)
        self.label_author_val = QLabel(self.appconfig.author)
        self.label_copyright = QLabel('Copyright')
        self.label_copyright.setFont(self.font_label)
        self.label_copyright_val = QLabel(self.appconfig.copyright)
        self.label_version = QLabel('Version')
        self.label_version.setFont(self.font_label)
        self.label_version_val = QLabel(self.appconfig.version)

        pm = self.image_cache.get_or_load_pixmap('img.logo_app', 'logo-app.png')
        if pm is not None:
            self.label_img = QLabel()
            self.label_img.setPixmap(QPixmap(pm).scaled(280, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            curr_gridid = 1
            self.grid.addWidget(self.label_img, curr_gridid, 1, 1, 2)

            curr_gridid += 1
            self.grid.addWidget(self.label_empty, curr_gridid, 0, 1, 3)
        else:
            curr_gridid = 0

        curr_gridid += 1
        self.grid.addWidget(self.label_author, curr_gridid, 0)
        self.grid.addWidget(self.label_author_val, curr_gridid, 1, 1, 3)

        curr_gridid += 1
        self.grid.addWidget(self.label_copyright, curr_gridid, 0)
        self.grid.addWidget(self.label_copyright_val, curr_gridid, 1, 1, 3)

        curr_gridid += 1
        self.grid.addWidget(self.label_version, curr_gridid, 0)
        self.grid.addWidget(self.label_version_val, curr_gridid, 1, 1, 3)

        self.setLayout(self.grid)

    def _center(self):
        """Centers the window on the screen"""
        screen = QDesktopWidget().screenGeometry()
        self.move(int((screen.width() - self.geometry().width()) / 2),
                  int((screen.height() - self.geometry().height()) / 2))
