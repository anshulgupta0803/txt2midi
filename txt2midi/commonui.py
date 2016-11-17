import tkinter as tk
'''
--------------------------------------------------------------------------------
	Desc: UI Common operation methods
--------------------------------------------------------------------------------
'''
class CommonUIOperation:
	'''
	--------------------------------------------------------------------------------
		Desc: Hide the Passed Widget
	--------------------------------------------------------------------------------
	'''
	def hideWidget(self,widget):
		if (not hasattr(widget, 'pi') or widget.pi==None):
			widget.pi = widget.place_info();
			widget.place_forget();

	'''
	--------------------------------------------------------------------------------
		Desc: Display the Widget
	--------------------------------------------------------------------------------
	'''
	def showWidget(self,widget):
		if hasattr(widget, 'pi') and widget.pi!=None:
			widget.place(widget.pi);
			widget.pi=None;
