#!/usr/bin/env python
# -*- coding: utf-8 -*-
import curses
from GLXCurses.Widget import Widget

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
        self.set_name('Window')

        # Internal Widget Setting
        self.title = None

        self.widget_to_display = {}
        self.widget_to_display_id = ''

        # Make a Style heritage attribute
        if self.style.attribute:
            self.attribute = self.style.attribute

    def draw(self):
        parent_height, parent_width = self.get_parent().get_size()
        parent_y, parent_x = self.get_parent().get_origin()

        # min_size_width = (self.get_spacing() * 2) + 1
        # min_size_height = (self.get_spacing() * 2) + 1
        # height_ok = self.get_parent().get_height() >= min_size_height
        # width_ok = self.get_parent().get_width() >= min_size_width
        # if not height_ok or not width_ok:
        #     return

        drawing_area = self.get_parent().get_widget().subwin(
                parent_height - (self.get_spacing() * 2),
                parent_width - (self.get_spacing() * 2),
                parent_y + self.get_spacing(),
                parent_x + self.get_spacing()
        )

        self.draw_in_area(drawing_area)

    # GLXC Window Functions
    def draw_in_area(self, drawing_area):
        self.set_widget(drawing_area)

        # Apply the Background color
        self.get_widget().bkgdset(
            ord(' '),
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('text', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )
        self.get_widget().bkgd(
            ord(' '),
            curses.color_pair(self.get_style().get_curses_pairs(
                fg=self.get_attr('text', 'STATE_NORMAL'),
                bg=self.get_attr('bg', 'STATE_NORMAL'))
            )
        )

        # Check widgets to display
        if bool(self.widget_to_display):
            self.widget_to_display[self.widget_to_display_id].draw()
            self.widget_to_display[self.widget_to_display_id].set_style(self.get_style())

        # Creat a box and add the name of the windows like a king, who trust that !!!
        if self.get_decorated():
            self.get_widget().box()
            if self.get_title():
                self.get_widget().addstr(
                    0,
                    1,
                    resize_text(self.get_title(), self.get_width() - 2, '~')
                )
        else:
            if self.get_title():
                self.get_widget().addstr(
                    0,
                    0,
                    resize_text(self.get_title(), self.get_width() - 1, '~')
                )

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def add(self, glxc_widget):
        # set_parent is the set_parent from Widget common method
        # information's will be transmit by it method
        glxc_widget.set_parent(self)
        id_max = len(self.widget_to_display.keys())

        if bool(self.widget_to_display):
            self.widget_to_display[id_max] = glxc_widget
            self.widget_to_display_id = id_max
        else:
            self.widget_to_display[id_max + 1] = glxc_widget
            self.widget_to_display_id = id_max + 1

    def get_attr(self, elem, state):
        return self.attribute[elem][state]



