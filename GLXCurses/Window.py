#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from Widget import Widget

from Style import Style
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


def resize_text(text, max_width, separator='~'):
    if max_width < len(text):
        return text[:(max_width / 2) - 1] + separator + text[-max_width / 2:]
    else:
        return text


class Window(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.name = 'Window'

        # Internal Widget Setting
        self.title = ''

        self.widget_to_display = {}
        self.widget_to_display_id = ''

        # Make a Style heritage attribute
        if self.style.attribute:
            self.attribute = self.style.attribute

    def draw(self):

        parent_height, parent_width = self.parent.get_size()
        parent_y, parent_x = self.parent.get_origin()
        self.parent_spacing = self.parent.get_spacing()

        drawing_area = self.parent.widget.subwin(
                parent_height - (self.widget_spacing * 2),
                parent_width - (self.widget_spacing * 2),
                parent_y + self.widget_spacing,
                parent_x + self.widget_spacing
        )

        self.draw_in_area(drawing_area)

    # GLXC Window Functions
    def draw_in_area(self, drawing_area):
        self.widget = drawing_area
        if self.attribute:
            text_fg = self.attribute['text']['STATE_NORMAL']
            widget_bg = self.attribute['bg']['STATE_NORMAL']
            color_normal = self.style.get_curses_pairs(fg=text_fg, bg=widget_bg)

        else:
            color_normal = 0

        widget_height, widget_width = self.widget.getmaxyx()

        if curses.has_colors():
            # Apply the Background color
            self.widget.bkgdset(
                ord(' '),
                curses.color_pair(color_normal)
            )
            self.widget.bkgd(
                ord(' '),
                curses.color_pair(color_normal)
            )

            # Check widgets to display
            if bool(self.widget_to_display):
                self.widget_to_display[self.widget_to_display_id].draw()
                self.widget_to_display[self.widget_to_display_id].set_style(self.style)

        # Creat a box and add the name of the windows like a king, who trust that !!!
        if self.widget_decorated > 0:
            drawing_area.box()
            if not self.title == '':
                drawing_area.addstr(
                    0,
                    1,
                    resize_text(self.title, widget_width - 2, '~')
                )
        else:
            if not self.title == '':
                drawing_area.addstr(
                    0,
                    0,
                    resize_text(self.title, widget_width - 1, '~')
                )

    def set_title(self, title):
        self.title = title

    def add(self, widget):
        # set_parent is the set_parent from Widget common method
        # information's will be transmit by it method
        widget.set_parent(self)
        id_max = len(self.widget_to_display.keys())

        if bool(self.widget_to_display):
            self.widget_to_display[id_max] = widget
            self.widget_to_display_id = id_max
        else:
            self.widget_to_display[id_max + 1] = widget
            self.widget_to_display_id = id_max + 1


