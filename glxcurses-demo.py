#!/usr/bin/env python
# -*- coding: utf-8 -*-
import GLXCurses
import sys
import curses
from random import randint

# It script it publish under GNU GENERAL PUBLIC LICENSE
# http://www.gnu.org/licenses/gpl-3.0.en.html
# Author: Jérôme ORNECH alias "Tuux" <tuxa@rtnp.org> all rights reserved
__author__ = 'Tuux'

if __name__ == '__main__':
    # Create the main Application
    app = GLXCurses.Application()
    app.set_name('Galaxie-Curse Demo')

    # Create a Menu
    menu = GLXCurses.MenuModel()
    menu.app_info_label = app.get_name()

    # Create a Window
    win1 = GLXCurses.Window()
    # win_main.set_title('My super Window 1')

    # Create a Window
    win_for_progressbar = GLXCurses.Window()
    win_for_progressbar.set_title('Progress Bar Widget')
    win_for_progressbar.set_decorated(1)
    win_for_progressbar.set_spacing(1)
    win_for_progressbar.override_background_color('CYAN')
    # Create a Window
    win6 = GLXCurses.Window()
    win6.set_title('Label Widget')
    win6.set_decorated(1)
    win6.set_spacing(1)

    # Create a Label
    label1 = GLXCurses.Label()
    label1.set_text('Super thing 1')
    label1.set_justify('RIGHT')
    label1.set_text('RED')
    label1.override_color('RED')
    label1.override_background_color('GREEN')

    label2 = GLXCurses.Label()
    label2.set_justify('RIGHT')
    label2.set_orientation('VERTICAL')
    label2.set_text('YELLOW')
    label2.override_color('YELLOW')

    label3 = GLXCurses.Label()
    label3.set_justify('LEFT')
    label3.set_text('CYAN')
    label3.override_color('CYAN')

    progressbar1 = GLXCurses.ProgressBar()
    progressbar1.set_spacing(0)
    progressbar1.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar1.get_value(), '%')
    progressbar1.set_text(value)
    progressbar1.set_show_text(1)
    progressbar1.set_position_type('BOTTOM')
    progressbar1.set_justify('CENTER')
    progressbar1.set_orientation('VERTICAL')
    progressbar1.set_inverted(0)

    progressbar2 = GLXCurses.ProgressBar()
    progressbar2.set_spacing(0)
    progressbar2.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar2.get_value(), '%')
    progressbar2.set_text(value)
    progressbar2.set_show_text(1)
    progressbar2.set_position_type('CENTER')
    progressbar2.set_justify('CENTER')
    progressbar2.set_orientation('VERTICAL')
    progressbar2.set_inverted(0)

    progressbar3 = GLXCurses.ProgressBar()
    progressbar3.set_spacing(0)
    progressbar3.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar3.get_value(), '%')
    progressbar3.set_text(value)
    progressbar3.set_show_text(1)
    progressbar3.set_position_type('TOP')
    progressbar3.set_justify('CENTER')
    progressbar3.set_orientation('VERTICAL')
    progressbar3.set_inverted(0)

    progressbar4 = GLXCurses.ProgressBar()
    progressbar4.set_spacing(0)
    progressbar4.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar4.get_value(), '%')
    progressbar4.set_text(value)
    progressbar4.set_show_text(1)
    progressbar4.set_position_type('TOP')
    progressbar4.set_justify('CENTER')
    progressbar4.set_orientation('VERTICAL')
    progressbar4.set_inverted(1)

    progressbar5 = GLXCurses.ProgressBar()
    progressbar5.set_spacing(0)
    progressbar5.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar5.get_value(), '%')
    progressbar5.set_text(value)
    progressbar5.set_show_text(1)
    progressbar5.set_position_type('CENTER')
    progressbar5.set_justify('CENTER')
    progressbar5.set_orientation('VERTICAL')
    progressbar5.set_inverted(1)

    progressbar6 = GLXCurses.ProgressBar()
    progressbar6.set_spacing(0)
    progressbar6.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar6.get_value(), '%')
    progressbar6.set_text(value)
    progressbar6.set_show_text(1)
    progressbar6.set_position_type('BOTTOM')
    progressbar6.set_justify('CENTER')
    progressbar6.set_orientation('VERTICAL')
    progressbar6.set_inverted(1)

    progressbar7 = GLXCurses.ProgressBar()
    progressbar7.set_spacing(0)
    progressbar7.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar7.get_value(), '%')
    progressbar7.set_text(value)
    progressbar7.set_show_text(1)
    progressbar7.set_position_type('CENTER')
    progressbar7.set_justify('CENTER')
    progressbar7.set_orientation('HORIZONTAL')
    progressbar7.set_inverted(0)

    progressbar8 = GLXCurses.ProgressBar()
    progressbar8.set_spacing(0)
    progressbar8.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar8.get_value(), '%')
    progressbar8.set_text(value)
    progressbar8.set_show_text(1)
    progressbar8.set_position_type('CENTER')
    progressbar8.set_justify('CENTER')
    progressbar8.set_orientation('HORIZONTAL')
    progressbar8.set_inverted(0)

    progressbar9 = GLXCurses.ProgressBar()
    progressbar9.set_spacing(0)
    progressbar9.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar9.get_value(), '%')
    progressbar9.set_text(value)
    progressbar9.set_show_text(1)
    progressbar9.set_position_type('CENTER')
    progressbar9.set_justify('CENTER')
    progressbar9.set_orientation('HORIZONTAL')
    progressbar9.set_inverted(0)

    progressbar10 = GLXCurses.ProgressBar()
    progressbar10.set_spacing(0)
    progressbar10.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar10.get_value(), '%')
    progressbar10.set_text(value)
    progressbar10.set_show_text(1)
    progressbar10.set_position_type('CENTER')
    progressbar10.set_justify('CENTER')
    progressbar10.set_orientation('HORIZONTAL')
    progressbar10.set_inverted(1)

    progressbar11 = GLXCurses.ProgressBar()
    progressbar11.set_spacing(0)
    progressbar11.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar11.get_value(), '%')
    progressbar11.set_text(value)
    progressbar11.set_show_text(1)
    progressbar11.set_position_type('CENTER')
    progressbar11.set_justify('CENTER')
    progressbar11.set_orientation('HORIZONTAL')
    progressbar11.set_inverted(1)

    progressbar12 = GLXCurses.ProgressBar()
    progressbar12.set_spacing(0)
    progressbar12.set_value(randint(0, 100))
    value = '{0:}{1:}'.format(progressbar12.get_value(), '%')
    progressbar12.set_text(value)
    progressbar12.set_show_text(1)
    progressbar12.set_position_type('CENTER')
    progressbar12.set_justify('left')
    progressbar12.set_orientation('HORIZONTAL')
    progressbar12.set_inverted(1)

    # Creat Button
    Button1 = GLXCurses.Button()
    Button1.set_application(app)
    Button1.set_text('Button1')

    Button2 = GLXCurses.Button()
    Button2.set_application(app)
    Button2.set_text('Button2')

    Button3 = GLXCurses.Button()
    Button3.set_application(app)
    Button3.set_text('Button3')

    vbox_button = GLXCurses.VBox()
    vbox_button.add(Button1)
    vbox_button.add(Button2)
    vbox_button.add(Button3)

    RadioButton1 = GLXCurses.RadioButton()
    RadioButton1.set_application(app)
    RadioButton1.set_text('RadioButton1')

    RadioButton2 = GLXCurses.RadioButton()
    RadioButton2.set_application(app)
    RadioButton2.set_text('RadioButton2')

    RadioButton3 = GLXCurses.RadioButton()
    RadioButton3.set_application(app)
    RadioButton3.set_text('RadioButton3')

    vbox_radio_button = GLXCurses.VBox()
    vbox_radio_button.add(RadioButton1)
    vbox_radio_button.add(RadioButton2)
    vbox_radio_button.add(RadioButton3)

    CheckButton1 = GLXCurses.CheckButton()
    CheckButton1.set_application(app)
    CheckButton1.set_text('CheckButton1')

    CheckButton2 = GLXCurses.CheckButton()
    CheckButton2.set_application(app)
    CheckButton2.set_text('CheckButton2')

    CheckButton3 = GLXCurses.CheckButton()
    CheckButton3.set_application(app)
    CheckButton3.set_text('CheckButton3')

    vbox_check_button = GLXCurses.VBox()
    vbox_check_button.add(CheckButton1)
    vbox_check_button.add(CheckButton2)
    vbox_check_button.add(CheckButton3)

    win_for_button = GLXCurses.Window()
    win_for_button.set_title('Button')
    win_for_button.set_decorated(1)
    win_for_button.add(vbox_button)

    win_for_radio_button = GLXCurses.Window()
    win_for_radio_button.set_title('RadioButton')
    win_for_radio_button.set_decorated(1)
    win_for_radio_button.add(vbox_radio_button)

    win_for_check_button = GLXCurses.Window()
    win_for_check_button.set_title('CheckButton')
    win_for_check_button.set_decorated(1)
    win_for_check_button.add(vbox_check_button)

    hbox_buttons = GLXCurses.HBox()
    hbox_buttons.set_spacing(1)
    hbox_buttons.add(win_for_button)
    hbox_buttons.add(win_for_radio_button)
    hbox_buttons.add(win_for_check_button)

    HSepartor = GLXCurses.HSeparator()
    HSepartor.set_spacing(0)
    # VSepartor.set_position_type('center')
    # Creat two Vertical Box contener
    vbox1 = GLXCurses.VBox()
    vbox1.subwins_spacing = 4

    vbox1.add(hbox_buttons)
    vbox1.add(win_for_progressbar)
    vbox1.add(win6)

    hbox_label = GLXCurses.HBox()
    hbox_label.subwins_spacing = 0
    hbox_label.add(label1)
    hbox_label.add(label2)
    hbox_label.add(label3)
    win6.add(hbox_label)

    # Creat a new Horizontal Box contener
    hbox = GLXCurses.HBox()
    hbox.subwins_spacing = 0
    hbox.add(vbox1)
    # hbox.add(vbox2)

    hbox_progress_widgets = GLXCurses.HBox()
    hbox_progress_widgets.set_spacing(1)
    hbox_progress = GLXCurses.HBox()
    vbox_progress = GLXCurses.VBox()

    hbox_progress_widgets.add(vbox_progress)
    hbox_progress_widgets.add(hbox_progress)

    hbox_progress.add(progressbar1)
    hbox_progress.add(progressbar2)
    hbox_progress.add(progressbar3)
    hbox_progress.add(progressbar4)
    hbox_progress.add(progressbar5)
    hbox_progress.add(progressbar6)

    vbox_progress.add(progressbar7)
    vbox_progress.add(progressbar8)
    vbox_progress.add(progressbar9)
    vbox_progress.add(progressbar10)
    vbox_progress.add(progressbar11)
    vbox_progress.add(progressbar12)

    win_for_progressbar.add(hbox_progress_widgets)

    # hbox.set_spacing(0)
    # hbox.add(win_for_progressbar)
    # hbox.add(win6)

    win1.add(hbox)

    # Creat a Status Bar
    toolbar = GLXCurses.Toolbar()
    toolbar.button_list = [
        'Help',
        'Normal',
        'Active',
        'Prelight',
        'Selected',
        'Insensitive',
        '',
        '',
        'Menu',
        'Quit'
    ]
    statusbar = GLXCurses.Statusbar()
    # Add Everything inside the Application
    app.add_menubar(menu)
    app.add_window(win1)
    app.add_statusbar(statusbar)
    app.add_toolbar(toolbar)

    # Main loop
    count = 1
    app.refresh()
    while True:
        message_text = ''
        input_event = app.getch()
        if curses.KEY_RESIZE:
            message_text += 'Screen Size:'
            message_text += str(app.get_parent_size())
            message_text += ' '

            # Status Bar Demo
            progressbar1.set_value(randint(0, 100))
            value = '{0:}{1:}'.format(progressbar1.get_value(), '%')
            progressbar1.set_text(value)

            progressbar2.set_value(randint(0, 100))
            value = '{0:}{1:}'.format(progressbar2.get_value(), '%')
            progressbar2.set_text(value)

            progressbar3.set_value(randint(0, 100))
            value = '{0:}{1:}'.format(progressbar3.get_value(), '%')
            progressbar3.set_text(value)

            progressbar4.set_value(randint(0, 100))
            value = '{0:}{1:}'.format(progressbar4.get_value(), '%')
            progressbar4.set_text(value)

            progressbar5.set_value(randint(0, 100))
            value = '{0:}{1:}'.format(progressbar5.get_value(), '%')
            progressbar5.set_text(value)

            progressbar6.set_value(randint(0, 100))
            value = '{0:}{1:}'.format(progressbar6.get_value(), '%')
            progressbar6.set_text(value)

            progressbar7.set_value(randint(0, 100))
            value = '{0:}{1:}'.format(progressbar7.get_value(), '%')
            progressbar7.set_text(value)

            progressbar8.set_value(randint(0, 100))
            value = '{0:}{1:}'.format(progressbar8.get_value(), '%')
            progressbar8.set_text(value)

            progressbar9.set_value(randint(0, 100))
            value = '{0:}{1:}'.format(progressbar9.get_value(), '%')
            progressbar9.set_text(value)

            progressbar10.set_value(randint(0, 100))
            value = '{0:}{1:}'.format(progressbar10.get_value(), '%')
            progressbar10.set_text(value)

            progressbar11.set_value(randint(0, 100))
            value = '{0:}{1:}'.format(progressbar11.get_value(), '%')
            progressbar11.set_text(value)

            progressbar12.set_value(randint(0, 100))
            value = '{0:}{1:}'.format(progressbar12.get_value(), '%')
            progressbar12.set_text(value)

            app.refresh()

        if input_event == curses.KEY_MOUSE:
            event = curses.getmouse()
            for Button in [Button1,
                           Button2,
                           Button3,
                           CheckButton1,
                           CheckButton2,
                           CheckButton3,
                           RadioButton1,
                           RadioButton2,
                           RadioButton3]:
                if Button.mouse_event(event):
                    message_text += Button.get_text()
                    message_text += ':('
                    message_text += Button.get_states()
                    message_text += ')'
                    statusbar.push(message_text)
                    app.refresh()

                    # if Button1.key_pressed(input_event):
                    #     pass

        # ToolBar
        if input_event == curses.KEY_F1:
            app.refresh()
        elif input_event == curses.KEY_F2:
            app.refresh()
        elif input_event == curses.KEY_F3:
            app.refresh()
        elif input_event == curses.KEY_F4:
            app.refresh()
        elif input_event == curses.KEY_F5:
            # Button1.set_is_focus(not Button1.get_is_focus())
            app.refresh()
        elif input_event == curses.KEY_F6:
            # Button1.set_sensitive(not Button1.get_sensitive())
            app.refresh()
        elif input_event == curses.KEY_F7:
            app.refresh()
        elif input_event == curses.KEY_F8:
            app.refresh()
        elif input_event == curses.KEY_F9:
            app.refresh()
        elif input_event == curses.KEY_F10:
            break
        elif input_event == ord('q'):
            break
        count += 1

    # App Close
    app.close()
    # THE END
    sys.exit(0)
