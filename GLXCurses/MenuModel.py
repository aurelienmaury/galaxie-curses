#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from Widget import Widget
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class MenuModel(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.name = 'MenuModel'

        # Internal Widget Setting
        self.app_info_label = None

        # Make a Style heritage attribute
        if self.get_style().attribute:
            self.attribute = self.get_style().attribute

    def draw(self):
        actual_x_size, actual_y_size = self.get_screen().getmaxyx()
        app_info_label = self.app_info_label
        self.widget = self.get_screen().subwin(0, 0, 0, 0)

        if curses.has_colors():
            self.widget.addstr(
                    0,
                    0,
                    str(' ' * int(actual_y_size)),
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('dark', 'STATE_NORMAL'),
                        bg=self.get_attr('light', 'STATE_NORMAL'))
                    )
                )
            self.widget.bkgdset(
                    ord(' '),
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('dark', 'STATE_NORMAL'),
                        bg=self.get_attr('light', 'STATE_NORMAL'))
                    )
                )
        if self.app_info_label:
            if not actual_y_size + 1 <= len(app_info_label):
                self.widget.addstr(
                    0,
                    (actual_y_size - 1) - len(str(app_info_label[:-1])),
                    app_info_label[:-1],
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('dark', 'STATE_NORMAL'),
                        bg=self.get_attr('light', 'STATE_NORMAL'))
                    )
                )
                self.widget.insstr(
                    0,
                    actual_y_size - 1,
                    app_info_label[-1:],
                    curses.color_pair(self.get_style().get_curses_pairs(
                        fg=self.get_attr('dark', 'STATE_NORMAL'),
                        bg=self.get_attr('light', 'STATE_NORMAL'))
                    )
                )

    def get_attr(self, elem, state):
        return self.attribute[elem][state]
