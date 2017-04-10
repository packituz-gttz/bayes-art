import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from matplotlib.figure import Figure
from numpy import arange, sin, pi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas    
from matplotlib.backends.backend_gtk3 import NavigationToolbar2GTK3 as NavigationToolbar

#~ Class that creates a child/sub window which contains a chart
class ChartWindow:

	def __init__(self) :
		self.build = Gtk.Builder()
		self.build.add_from_file("Chart_Windows.glade")
		self.window_child = self.build.get_object("chart_window")
		#~ connected delete-event signal to close window when x button is pressed
		self.window_child.connect("delete-event", self.destroy_my_window)
		self.sw = self.build.get_object("scrolled_child_chart")
		self.sw2 = self.build.get_object("scrolled_child_toolbar")
		
	def show_Cwindow(self) :
		pass
