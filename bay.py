import gi

import Orange
import random

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


#~ print("Accuracy: %.3f" % Orange.evaluation.scoring.CA(res)[0])
#~ print("AUC:      %.3f" % Orange.evaluation.scoring.AUC(res)[0])
#~ __________________

class Dialog :
		#~ Constructor de los dialogos
	def __init__(self) :
		self.build = Gtk.Builder()
		self.build.add_from_file("bay.glade")
		self.dialog = self.build.get_object("dialog_chosee_file_warning")
		
		
	def run(self):
		response = self.dialog.run()
		#~ Verificamos si se dio "cancelar" o "OK"
		self.dialog.destroy()
		if response == -5 :
			return "ok"
		else :
			return "cancel"
		

		
class Handler:
	
	def __init__(self) :
		list_model_K = builder.get_object("liststore1")
		list_model_K.append([2])
		list_model_K.append([5])
		list_model_K.append([7])
		list_model_K.append([10])
		list_model_K.append([15])
		list_model_K.append([20])
		combo_USB_List = builder.get_object("combo_kFolds")
		combo_USB_List.set_active(1)
		
		self.k_value = 5
		
	def combo_kFolds_changed_cb(self, combo) :
		tree_iter = combo.get_active_iter()
		if tree_iter != None :
			model = combo.get_model()
			self.k_value = model[tree_iter][0]
			print (self.k_value)

	
	def btn_file_file_set_cb(self, widget) :
		#~ textview = builder.get_object("textview")
		#~ texto_buffer = builder.get_object("textbuffer1")
		
		self.file_txt = widget.get_filename()
		string_txt = ""
		for line in open(self.file_txt) :
			string_txt = string_txt + line
			
		#~ Mostrar texto de archivo en ventana	-----------------------
		#~ texto_buffer.set_text(string_txt)
		
	def file_bayes_activate_cb(self, widget) :
		textViewAUC = builder.get_object("textViewAUC")
		textViewAccurrancy = builder.get_object("textViewAccurracy")
		textViewPrecision = builder.get_object("label_precision")
		textViewRecall = builder.get_object("label_recall")
		
		try:
			#~ Orange _____
			data = Orange.data.Table(self.file_txt)
			nb = Orange.classification.NaiveBayesLearner()
			res = Orange.evaluation.CrossValidation(data, [nb], k=self.k_value)
			accurracy = Orange.evaluation.scoring.CA(res)
			auc = Orange.evaluation.scoring.AUC(res)
			precision = Orange.evaluation.scoring.Precision(res)
			recall = Orange.evaluation.scoring.Recall(res)
		
			print (accurracy[0])
			print (auc[0])
			print (recall[0])
			textViewAUC.set_text(str(auc))
			textViewAccurrancy.set_text(str(accurracy))
			textViewPrecision.set_text(str(precision))
			textViewRecall.set_text(str(recall))
		
		except AttributeError:
			print ("Elige primero un archivo")	
			my_dialog = Dialog()
			response = my_dialog.run()
		
		
	

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
