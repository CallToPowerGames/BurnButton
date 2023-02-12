#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2018-2023 Denis Meyer
#
# This file is part of the Burnbutton.
#

'''SoundCache'''

import logging

from PyQt5.QtMultimedia import QSound

from lib.Utils import load_sound


class SoundCache():

    _cache = {
        'burn1': None,
        'burn2': None
    }

    def __init__(self, basedir):
        '''Initializes

        :param basedir: The base path
        '''
        logging.debug('Initializing SoundCache')
        
        self.basedir = basedir

    def load_sound(self, key, name, path=None):
        '''Plays the sound

        :param sound: Sound to play
        '''
        val = self.get_sound(key)
        if not val:
            self.set_sound(key, load_sound(self.basedir, name, path))
            val = self.get_sound(key)

    def play(self, key, name, path=None):
        '''Plays the sound

        :param sound: Sound to play
        '''
        val = self.get_sound(key)
        if not val:
            self.set_sound(key, load_sound(self.basedir, name, path))
            val = self.get_sound(key)
        val.play()

    def get_sound(self, key, default=None):
        """Returns the value for the given key or - if not found - a default value

        :param key: The key
        :param default: The default if no value could be found for the key
        """
        try:
            return self._cache[key]
        except KeyError as exception:
            logging.error('Returning default for key "{}": "{}"'.format(key, exception))
            return default

    def set_sound(self, key, value, override=False):
        """Sets the value for the given key

        :param key: The key
        :param value: The value
        :param override: Whether to force override
        """
        if override or not key in self._cache or not self.get_sound(key):
            self._cache[key] = value
