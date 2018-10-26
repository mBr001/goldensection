#!/usr/bin/python3
'''
   Copyright 2017 Mirko Brombin (brombinmirko@gmail.com)

   This file is part of goldensection.

    goldensection is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    goldensection is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with goldensection.  If not, see <http://www.gnu.org/licenses/>.
'''

import gi
import locale
import gettext
import argparse
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gio, Gdk, Granite, GObject
import constants as cn
import window as wn

class Application(Granite.Application):

    def do_activate(self):
        self.win = wn.Window()
        self.win.set_default_size(600, 600) 
        self.win.connect("delete-event", Gtk.main_quit)

        parser = argparse.ArgumentParser(description = cn.App.application_description)
        parser.add_argument('--about', action='store_true', help='About '+cn.App.application_name)
        args = parser.parse_args()  
        if args.about == True:
            self.show_about(self.win)
        else:
            self.win.show_all()

        Gtk.main()

app = Application()

stylesheet = """
    @define-color colorPrimary """+cn.Colors.primary_color+""";
    @define-color textColorPrimary """+cn.Colors.primary_text_color+""";
    @define-color textColorPrimaryShadow """+cn.Colors.primary_text_shadow_color+""";
""";

style_provider = Gtk.CssProvider()
style_provider.load_from_data(bytes(stylesheet.encode()))
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

app.application_id = cn.App.application_id
app.flags = Gio.ApplicationFlags.FLAGS_NONE
app.program_name = cn.App.application_name
app.build_version = cn.App.application_version
app.about_documenters = cn.App.about_documenters
app.about_authors = cn.App.about_authors
app.about_comments = cn.App.about_comments
app.app_years = cn.App.app_years
app.build_version = cn.App.application_version;
app.app_icon = cn.App.application_id
app.main_url = cn.App.main_url
app.bug_url = cn.App.bug_url
app.help_url = cn.App.help_url
app.translate_url = cn.App.translate_url

app.run("", Gio.ApplicationFlags.FLAGS_NONE)
