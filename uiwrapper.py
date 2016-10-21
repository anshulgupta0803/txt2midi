#!/usr/bin/python3.5

from ui import UiApplication;
import tkinter as tk;

'''
--------------------------------------------------------------------------------
	Desc: Wrapper Interface for the UI Application
--------------------------------------------------------------------------------
'''
class UiWrapper:
	__ui=None;#private variable

	'''
	--------------------------------------------------------------------------------
		Desc: Render UI
	--------------------------------------------------------------------------------
	'''
	def renderUI(self):
		root = tk.Tk();
		self.__ui = UiApplication(master=root);

	'''
	--------------------------------------------------------------------------------
		Desc: Show the UI on screen
	--------------------------------------------------------------------------------
	'''
	def showUI(self):
		self.__ui.mainloop();
	'''
	--------------------------------------------------------------------------------
		[Single Track]
		Desc: Gives the full file name i.e filename with path selected by user
		Return: (string) full file name
	--------------------------------------------------------------------------------
	'''
	def getSrcFullFileName(self):
		return self.__ui.pan_single_track.txt_src_file_txtvar.get();

	'''
	--------------------------------------------------------------------------------
		[Single Track]
		Desc: Gives the track name entered by user
		Return: (string) track name
	--------------------------------------------------------------------------------
	'''
	def getTrackName(self):
		return self.__ui.pan_single_track.txt_trackname_txtvar.get();

	'''
	--------------------------------------------------------------------------------
		[Single Track]
		Desc: Gives the instrument name entered by user
		Return: (string) instrument name
	--------------------------------------------------------------------------------
	'''
	def setInstrument(self):
		return self.__ui.pan_single_track.opt_inst_txtvar.get();

	'''
	--------------------------------------------------------------------------------
		[All Track]
		Desc: Set the success msg
	--------------------------------------------------------------------------------
	'''
	def setSucessMsg(self,msg):
		self.__ui.pan_status.lbl_msg["text"]="Success: "+msg;
		self.__ui.pan_status.lbl_msg.config(fg=self.__ui.color_green);
		self.__ui.pan_status.btn_play.show()

	'''
	--------------------------------------------------------------------------------
		[All Track]
		Desc: Set the success msg
	--------------------------------------------------------------------------------
	'''
	def setErrorMsg(self,msg):
		self.__ui.pan_status.lbl_msg["text"]="Error: "+msg;
		self.__ui.pan_status.lbl_msg.config(fg=self.__ui.color_red);
		self.__ui.pan_status.btn_play.hide()


	'''
	--------------------------------------------------------------------------------
		[All Tracks]
		Desc: Gives the output entered by user
		Return: (string) output folder
	--------------------------------------------------------------------------------
	'''
	def getOutputFolder(self):
		return self.__ui.pan_single_track.txt_dst_file_txtvar.get();

	'''
	--------------------------------------------------------------------------------
		[All Tracks]
		Desc: Binds the on click event to the convert button
	--------------------------------------------------------------------------------
	'''
	def bindConvertOnClick(self,lamda_fun_handler):
		self.__ui.st_btn_convert_funhandler=lamda_fun_handler;
def prt(obj):
	print("o/p:"+obj.getOutputFolder());
	print("inst:"+obj.setInstrument());
	print("src:"+obj.getSrcFullFileName());
	print("track:"+obj.getTrackName());
	obj.setSucessMsg("File Converted Success fully.");
	obj.setErrorMsg("Failed in converting");

wrapper=UiWrapper();
wrapper.renderUI();
wrapper.bindConvertOnClick(lambda:prt(wrapper));
wrapper.showUI();
