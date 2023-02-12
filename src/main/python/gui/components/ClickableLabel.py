#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2018-2023 Denis Meyer
#
# This file is part of the Burnbutton.
#

"""Burnbutton - QClickableLabel"""

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QLabel

class QClickableLabel(QLabel):
    """A clickable QLabel"""

    mousePressed = pyqtSignal(object)
    mouseReleased = pyqtSignal(object)

    def __init__(self, parent=None):
        QLabel.__init__(self, parent)

    def mousePressEvent(self, event):
        self.mousePressed.emit(event)

    def mouseReleaseEvent(self, event):
        self.mouseReleased.emit(event)
