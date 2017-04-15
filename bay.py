import gi

import Orange
import random
from sklearn.metrics import confusion_matrix
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


#~ print("Accuracy: %.3f" % Orange.evaluation.scoring.CA(res)[0])
#~ print("AUC:      %.3f" % Orange.evaluation.scoring.AUC(res)[0])
#~ __________________
#~ En desarrollo-------------
class ChartWindow :
	def __init__(self) :
		self.build = Gtk.Builder()
		self.build.add_from_file("bay.glade")
		self.window_child = self.build.get_object("chart_window")
		self.window_child.connect("delete_event", self.destroy_my_window)
		self.sw = self.build.get_object("scrolled_child_chart")
		self.sw2 = self.build.get_object("scrolled_child_toolbar")
		
		
	def show_Cwindow(self) :
		plt.rc("figure", facecolor="white")
			
		
	

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
			self.data = Orange.data.Table(self.file_txt)
			nb = Orange.classification.NaiveBayesLearner()
			self.res = Orange.evaluation.CrossValidation(self.data, [nb], k=self.k_value)
			accurracy = Orange.evaluation.scoring.CA(self.res)
			auc = Orange.evaluation.scoring.AUC(self.res)
			precision = Orange.evaluation.scoring.Precision(self.res)
			recall = Orange.evaluation.scoring.Recall(self.res)
		
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
		
	
	
	def file_matriz_activate_cb(self, widget) :	
		c_values = self.data.domain.class_var.values
		print (c_values)
		expected = self.res.actual
		predicted = self.res.predicted[0]
		
		results = confusion_matrix(expected, predicted)
		print (results)
		
		filas = len(results)
		columnas = len(results[0])
		
		df_cm = pd.DataFrame(results, index = [ c_values [i] for i in range(0, len(results))],
									columns = [ c_values [i] for i in range(0, len(results))])
		sn.heatmap(df_cm, annot = True, fmt="d")
		plt.ylabel('Actual')
		plt.xlabel('Predicted')
		plt.show() 
		
		print (expected)
		print (predicted)
		
		N = 9
		x = [ elem + random.uniform(0,0.5) for elem in expected ]
		y = [ elem + random.uniform(0,0.5) for elem in predicted ]
		
		print (type(x))
		print (type(y))
		max_v = (max(predicted))
		min_v = (min(predicted))
		colors = []
		for value in predicted :
			value_c = float((value - min_v ) / ( max_v - min_v ))
			colors.append((value_c,0,value_c))
		#~ colors = np.random.rand(N)

		plt.scatter(y, x, s = 130.5, c=colors, alpha=0.5)
		plt.xlabel('Predicted')
		plt.ylabel('Actual')
		index = []
		for number in range(0,filas) :
			index.append(number + 0.25)
		plt.xticks(index, (i for i in c_values))
		plt.yticks(index, (i for i in c_values))
		plt.show() 
		
		#~ chart_window = ChartWindow() En desarrollo---
		#~ chart_window.show_Cwindow() En desarrollo---
		
		
	

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
