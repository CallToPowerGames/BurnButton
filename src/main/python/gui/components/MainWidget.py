#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2018-2023 Denis Meyer
#
# This file is part of the Burnbutton.
#

"""Burnbutton - Main widget"""

import logging
import os
import json
import csv

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QSizePolicy

from .ClickableLabel import QClickableLabel

class MainWidget(QWidget):
    """Main widget GUI"""

    def __init__(self, appconfig, image_cache, sound_cache):
        """Initializes the main widget

        :param appconfig: The AppConfig
        :param image_cache: The image cache
        :param sound_cache: The sound cache
        """
        super().__init__()

        logging.debug('Initializing MainWidget')

        self.appconfig = appconfig
        self.image_cache = image_cache
        self.sound_cache = sound_cache
        self.components = []

        self.font_label_header = QFont()
        self.font_label_header.setBold(True)

        self.image_cache.get_or_load_pixmap('img.button_up', 'button-up.png')
        self.image_cache.get_or_load_pixmap('img.button_down', 'button-down.png')
        self.sound_cache.load_sound('burn1', 'burn1.wav', 'sounds')
        self.sound_cache.load_sound('burn2', 'burn2.wav', 'sounds')

    def init_ui(self):
        """Initiates application UI"""
        logging.debug('Initializing MainWidget GUI')

        self.grid = QGridLayout()
        self.grid.setSpacing(0)

        initX, initY = 500, 500

        self._setImg(initX, initY)

        self.label = QClickableLabel()
        self.label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(False)
        self.label.resize(initX, initY)
        self.label.setPixmap(self.img_button_up)

        self.label.mousePressed.connect(self._on_mousepressed) 
        self.label.mouseReleased.connect(self._on_mousereleased)

        self.grid.addWidget(self.label)

        self.setLayout(self.grid)

    def resizeEvent(self, event):
        """On widget resize

        :param event: The event
        """
        logging.debug('Resized: {}x{}'.format(self.width(), self.height()))
        self.label.resize(self.width(), self.height())
        self._setImg(self.label.width(), self.label.height())
        self.label.setPixmap(self.img_button_up)

    def _setImg(self, scaleX, scaleY):
        """Sets the image size

        :param scaleX: The x scale
        :param scaleY: The y scale
        """
        gap = 40
        self.img_button_up = QPixmap(self.image_cache.get_or_load_pixmap('img.button_up', 'button-up.png')).scaled(scaleX - gap, scaleY - gap, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.img_button_down = QPixmap(self.image_cache.get_or_load_pixmap('img.button_down', 'button-down.png')).scaled(scaleX - gap, scaleY - gap, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def _on_mousepressed(self, event):
        """On mouse pressed

        :param event: The event
        """
        logging.debug('_on_mousepressed')
        self.label.setPixmap(self.img_button_down)
        print(event.button())
        if event.button() == Qt.LeftButton:
            self.sound_cache.play('burn2', 'burn2.wav', 'sounds')
        elif event.button() == Qt.RightButton:
            self.sound_cache.play('burn1', 'burn1.wav', 'sounds')

    def _on_mousereleased(self, event):
        """On mouse released

        :param event: The event
        """
        logging.debug('_on_mousereleased')
        self.label.setPixmap(self.img_button_up)
