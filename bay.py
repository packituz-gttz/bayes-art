import gi

import Orange
import random

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#~ Orange _____
data = Orange.data.Table("iris")
nb = Orange.classification.NaiveBayesLearner()
res = Orange.evaluation.CrossValidation(data, [nb], k=5)
accurancy = Orange.evaluation.scoring.CA(res)
auc = Orange.evaluation.scoring.AUC(res)
print (accurancy[0])
print (auc[0])
#~ print("Accuracy: %.3f" % Orange.evaluation.scoring.CA(res)[0])
#~ print("AUC:      %.3f" % Orange.evaluation.scoring.AUC(res)[0])
#~ __________________

class Dialog :
		#~ Constructor de los dialogos
	def __init__(self) :
		self.build = Gtk.Builder()
		self.build.add_from_file("bay.glade")
		self.dialog = self.build.get_object("dialog_save")
		
		
	def run(self):
		response = self.dialog.run()
		#~ Verificamos si se dio "cancelar" o "OK"
		if response == -5 :
			myfile = self.dialog.get_filename()
			self.dialog.destroy()
			return True, myfile
		self.dialog.destroy()
		return False
		
		

		
class Handler:
	
	def btn_file_file_set_cb(self, widget) :
		#~ textview = builder.get_object("textview")
		#~ texto_buffer = builder.get_object("textbuffer1")
		
		file_txt = widget.get_filename()
		string_txt = ""
		for line in open(file_txt) :
			string_txt = string_txt + line
			
			
		#~ Mostrar texto de archivo en ventana	-----------------------
		#~ texto_buffer.set_text(string_txt)
		
	
	
	def onDeleteWindow(self, *args):
		Gtk.main_quit(*args)




builder = Gtk.Builder()
builder.add_from_file("bay.glade")
builder.connect_signals(Handler())

window = builder.get_object("main_window")
window.connect("delete-event", Gtk.main_quit)
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
