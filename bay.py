import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

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
	#~ btn_filechooser_file_set_cb
	
	def btn_file_file_set_cb(self, widget) :
		textview = builder.get_object("textview")
		
		texto_buffer = builder.get_object("textbuffer1")
		
		file_txt = widget.get_filename()
		string_txt = ""
		for line in open(file_txt) :
			string_txt = string_txt + line
			
		texto_buffer.set_text(string_txt)
		
	
	
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
