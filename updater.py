#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
gi.require_version ('Gtk', '3.0')
from gi.repository import Gtk
import os

print("Simple Distribution Updater, v0.1")

class MainWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self)
		self.set_border_width(10)
		self.set_default_size(400, 50)
		
		hb = Gtk.HeaderBar()
		hb.set_show_close_button(True)
		hb.props.title = "Simple Distribution Updater"
		self.set_titlebar(hb)
		
		hbox = Gtk.Box(spacing=6)
		self.add(hbox)
		
		grid = Gtk.Grid()
		self.add(grid)
		
		label = Gtk.Label("Choose your distribution: ")
		hbox.pack_start(label, True, True, 0)
		
		button1 = Gtk.Button(label="Debian/Ubuntu")
		button1.connect("clicked", self.on_button1_clicked)
		hbox.pack_start(button1, True, True, 0)
		
		button2 = Gtk.Button(label="Arch")
		button2.connect("clicked", self.on_button2_clicked)
		hbox.pack_start(button2, True, True, 0)
		
		button3 = Gtk.Button(label="Fedora")
		button3.connect("clicked", self.on_button3_clicked)
		hbox.pack_start(button3, True, True, 0)
				
		grid.add(label)
		
		grid.add(button1)
		grid.attach_next_to(button2, button1, Gtk.PositionType.RIGHT, 1, 1)
		
		grid.add(button2)
		grid.attach_next_to(button3, button2, Gtk.PositionType.RIGHT, 1, 1)
		
	def on_button1_clicked(self, widget):
		os.system("sudo apt update && sudo apt upgrade")
		
	def on_button2_clicked(self, widget):
		os.system("sudo pacman -Syu")
		
	def on_button3_clicked(self, widget):
		os.system("sudo dnf update")
		
win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
