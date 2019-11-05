# -*- coding: utf-8 -*-

# Copyright (c) 2017 Feras A. Saad <fsaad@mit.edu>
# Released under the MIT License; refer to LICENSE.txt.

import sublime
import sublime_plugin

SETTINGS_PATH_USR = 'Preferences.sublime-settings'

SETTINGS_PATH_SYS = 'Packages/Default/Preferences.sublime-settings'
SETTINGS_RESOURCE = sublime.load_resource(SETTINGS_PATH_SYS)
SETTINGS_DICT = sublime.decode_value(SETTINGS_RESOURCE)
SETTINGS_KEYS = list(sorted(SETTINGS_DICT.keys()))

class prompt_get_setting(sublime_plugin.WindowCommand):

    def run(self, key=None):
        self.settings = sublime.load_settings(SETTINGS_PATH_USR)
        if key is not None:
            return self.on_done(key)
        if not hasattr(self, 'last'):
            self.last = None,
        self.window.show_quick_panel(SETTINGS_KEYS, self.on_done)

    def on_done(self, key):
        self.last = key
        if key == -1:
            return None
        elif isinstance(key, int):
            sett = SETTINGS_KEYS[key]
        elif isinstance(key, str):
            sett = key
        else:
            raise ValueError('Invalid key: %s' % (repr(key,)))
        if not self.settings.has(sett):
            sublime.status_message('No such setting {}'.format(sett,))
            return None
        value = self.settings.get(sett)
        message = '{}: {}'.format(sett, value)

        settings = sublime.load_settings('ViewSetting.sublime-settings')
        if settings.get('show_popup'):
            self.window.active_view().show_popup(message)
        if settings.get('show_status_bar'):
            sublime.status_message(message)
