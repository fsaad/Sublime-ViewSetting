# -*- coding: utf-8 -*-

# Copyright (c) 2017 Feras A. Saad <fsaad@mit.edu>
# Released under the MIT License; refer to LICENSE.txt.

import sublime
import sublime_plugin

SETTINGS_PATH = 'Preferences.sublime-settings'

class prompt_get_setting(sublime_plugin.WindowCommand):

    def run(self, **kwargs):
        if not hasattr(self, 'last'):
            self.last = ''
        self.settings = sublime.load_settings(SETTINGS_PATH)
        self.window.show_input_panel(
            'Select setting', self.last, self.on_done, None, None)

    def on_done(self, key):
        self.last = key
        if not self.settings.has(key):
            sublime.status_message('No such setting {}'.format(key,))
            return None
        value = self.settings.get(key)
        sublime.status_message('{}: {}'.format(key, value))
