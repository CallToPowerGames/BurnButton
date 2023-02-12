#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2018-2023 Denis Meyer
#
# This file is part of the Burnbutton.
#

"""Burnbutton - Main window"""

import logging
import platform

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QMenuBar, QAction
from gui.components.MainWidget import MainWidget
from gui.components.AboutDialog import AboutDialog

class MainWindow(QMainWindow):
    """Main window GUI"""

    def __init__(self, appconfig, image_cache, sound_cache):
        """Initializes the main window

        :param appconfig: The AppConfig
        :param image_cache: The image cache
        :param sound_cache: The sound cache
        """
        super().__init__()

        logging.debug('Initializing MainWindow')

        self.appconfig = appconfig
        self.image_cache = image_cache
        self.sound_cache = sound_cache

    def init_ui(self):
        """Initiates application UI"""
        logging.debug('Initializing MainWindow GUI')

        self._init_menu()

        self.setWindowTitle('Burnbutton')

        self.mainwidget = MainWidget(self.appconfig, self.image_cache, self.sound_cache)
        self.mainwidget.init_ui()
        self.setCentralWidget(self.mainwidget)

        self.resize(500, 500)

        self._center()
        self._init()

    def _show_about_dialog(self):
        """Displays the about dialog"""
        logging.debug('Displaying AboutDialog')
        about = AboutDialog(self.appconfig, self.image_cache)
        about.init_ui()
        about.exec_()

    def _quit_application(self):
        """Quits the application"""
        logging.debug('Quitting')
        QCoreApplication.exit(0)

    def _init_menu(self):
        """Initializes the menu bar"""
        logging.debug('Initializing the menu bar')

        if platform.uname().system.startswith('Darw'):
            logging.debug('Platform is Mac OS')
            self.menu_bar = QMenuBar()
        else :
            logging.debug('Platform is not Mac OS')
            self.menu_bar = self.menuBar()

        menu_application = self.menu_bar.addMenu('Burnbutton')

        action_about = QAction('About', self)
        action_about.setShortcut('Ctrl+A')
        action_about.triggered.connect(self._show_about_dialog)

        action_quit = QAction('Quit', self)
        action_quit.setShortcut('Ctrl+Q')
        action_quit.triggered.connect(self._quit_application)

        menu_application.addAction(action_about)
        menu_application.addAction(action_quit)

    def _init(self):
        logging.debug('Initializing MainWindow defaults')

    def _center(self):
        """Centers the window on the screen"""
        screen = QDesktopWidget().screenGeometry()
        self.move(int((screen.width() - self.geometry().width()) / 2),
                  int((screen.height() - self.geometry().height()) / 2))
