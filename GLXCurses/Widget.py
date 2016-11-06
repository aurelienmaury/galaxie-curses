#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Style import Style
# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'


class Widget(object):
    def __init__(self):
        self.type = 'Widget'

        # Widget Setting
        # Widgets can be named, which allows you to refer to them from a GLXCStyle
        self.name = 'Widget'

        # Color's and Style
        #self.override_background_color = 0

        # State
        self.state = dict()
        self.state['NORMAL'] = 1
        self.state['ACTIVE'] = 0
        self.state['PRELIGHT'] = 0
        self.state['SELECTED'] = 0
        self.state['INSENSITIVE'] = 0
        self.state['INCONSISTENT'] = 0
        self.state['FOCUSED'] = 0

        self.widget = ''
        self.widget_spacing = 0
        self.widget_decorated = 0
        self.attribute = ''

        self.screen = ''

        # Each Widget come with it own Style by default
        # It can receive parent Style() or a new Style() during a set_parent() / un_parent() call
        # GLXCApplication is a special case where it have no parent, it role is to impose it own style to each Widget
        self.style = Style()
        self.style_backup = None

        # Widget Parent Information's
        self.parent = None

    # Common Widget mandatory
    def get(self):
        return self.widget

    def get_origin(self):
        return self.widget.getbegyx()

    def get_size(self):
        return self.widget.getmaxyx()

    def set_spacing(self, spacing):
        self.widget_spacing = spacing

    def get_spacing(self):
        return self.widget_spacing

    def set_decorated(self, decorated):
        self.widget_decorated = decorated

    def get_decorated(self):
        return self.widget_decorated

    # Each Galaxie Curses Component's must have a draw method
    def refresh(self):
        self.draw()

    def show(self):
        self.draw()

    def show_all(self):
        self.draw()
        self.parent.draw()

    # Parent Management
    def get_parent(self):
        if self.parent:
            return self.parent
        else:
            return self

    def get_parent_size(self):
        return self.get_parent().widget.getmaxyx()

    def get_parent_origin(self):
        return self.parent.widget.getbegyx()

    def _set_parent(self, parent):
        self.parent = parent

    def set_parent(self, parent):

        self._set_parent(parent)

        self.screen = self.get_parent().get_screen()

        # Widget start with own Style, and will use the Style of it parent when it add to a contener
        # GLXCApplication Widget is a special case where it parent is it self.

        self.style_backup = self.get_style()
        self.set_style(self.get_parent().get_style())

    def un_parent(self):
        self.parent = None
        self.set_style(self.style_backup)

    def get_parent_spacing(self):
        return self.get_parent().get_spacing()

    def get_parent_style(self):
        return self.get_parent().get_style()

    def get_screen(self):
        return self.screen

    def set_widget(self, widget):
        self.widget = widget

    # Name management use for GLXCStyle color's
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_style(self, style):
        self.style = style

    def get_style(self):
        return self.style

    def override_color(self, color):
        self.style.attribute['text']['STATE_NORMAL'] = str(color).upper()

    def override_background_color(self, color):
        self.style.attribute['bg']['STATE_NORMAL'] = str(color).upper()
