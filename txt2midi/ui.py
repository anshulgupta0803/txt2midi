import tkinter as tk
import pygame
import time
from tkinter import font
from tkinter import filedialog
import os
from txt2midi.commonui import *
'''
--------------------------------------------------------------------------------
	Desc: UI of Converter
--------------------------------------------------------------------------------
'''
class UiApplication(tk.Frame):
	UiOp=CommonUIOperation();
	#Windows Properties
	window_width=800;
	window_height=525;
	window_xpos=500;
	window_ypos=0;

	#Font
	font_courier18 = None; #Init in __init_


	#Panel Properties
	border_width=5;
	panel_width=window_width-20;
	panel_xoffset=10;

	#colors Properties
	danger_bg_color="#ed9663";
	success_bg_color="#a9dd71"
	color_green="#abe03a";
	color_red="#ba4848";

	#Event handler : Function without parameter
	st_btn_convert_funhandler=None;
	status_btn_play_funhandler=None;

	'''
	--------------------------------------------------------------------------------
		Desc: Construtor
	--------------------------------------------------------------------------------
	'''
	def __init__(self, master=None):
		super().__init__(master);
		master.title("Converter : SaReGaMa")
		self.font_courier18 = font.Font(family='Arial',size=14);
		self.container=master;
		self.setFrameProp(master);
		self.pack(fill='both', expand='yes')
		self.createPanel();
		self.createWidgets();

	'''
	--------------------------------------------------------------------------------
		Desc: Set Main Window Properties
	--------------------------------------------------------------------------------
	'''
	def setFrameProp(self,win):
		win.minsize(width=self.window_width, height=self.window_height);
		win.resizable(width=False, height=False);
		win.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height, self.window_xpos, self.window_ypos));

	'''
	--------------------------------------------------------------------------------
		Desc: Create all panels
	--------------------------------------------------------------------------------
	'''
	def createPanel(self):

		# Panel 1 : Single Track
		st_panel_height=325;
		self.pan_single_track = tk.PanedWindow(self, orient=tk.VERTICAL,
							bd=self.border_width,
							width=self.panel_width,
							height=st_panel_height,
							relief=tk.RIDGE);
		self.pan_single_track.panel_bg_color="#4a76b2";
		self.pan_single_track.panel_text_color="#e5e5c5"
		self.pan_single_track.config(bg=self.pan_single_track.panel_bg_color)
		self.pan_single_track.place(x=self.panel_xoffset,y=20)

		# Panel 2 : Status
		status_panel_height=150;
		self.pan_status = tk.PanedWindow(self, orient=tk.VERTICAL,
							bd=self.border_width,
							width=self.panel_width,
							height=status_panel_height,
							relief=tk.RIDGE);
		self.pan_status.panel_bg_color="#a09f8d";
		self.pan_status.panel_text_color="#e5e5c5";
		self.pan_status.config(bg=self.pan_status.panel_bg_color)
		self.pan_status.place(x=self.panel_xoffset,y=40+st_panel_height);

	'''
	--------------------------------------------------------------------------------
		Desc: Creating Complete Widget
	--------------------------------------------------------------------------------
	'''
	def createWidgets(self):
		self.createPanelST();
		self.createPanelStatus();

	'''
	--------------------------------------------------------------------------------
		[Single Track]
		Desc: Ui of Single Track Panel
	--------------------------------------------------------------------------------
	'''
	def createPanelST(self):

		panel=self.pan_single_track;
		f_width=350;
		f_height=35;
		f_x=250;
		y_offset=10;
		f_y_inc=80;
		f_margin=30;
		row=-1;

		#-----------------------------------[row 1]----------------------------------------------
		row+=1;
		#col 1 : label
		panel.lbl_src = tk.Label(panel, text="Source file : ",bg=panel.panel_bg_color)
		panel.lbl_src.config(font=self.font_courier18,fg=panel.panel_text_color);
		panel.lbl_src.place(x=65, y=y_offset)

		#col 2 :text
		panel.txt_src_file_txtvar = tk.StringVar()
		panel.txt_src_file= tk.Entry(panel,textvariable=panel.txt_src_file_txtvar);
		panel.txt_src_file.config(font=self.font_courier18,fg="green",state='readonly');
		panel.txt_src_file.place(x=f_x,y=y_offset,height=f_height, width=f_width)

		#col 3 : button
		panel.btn_browse = tk.Button(panel)
		panel.btn_browse.config(font=self.font_courier18);
		panel.btn_browse["text"] = "Browse"
		panel.btn_browse["command"] = self.onClickSrcFileBrowse
		panel.btn_browse.place(x=f_x+f_width+f_margin,y=y_offset,height=f_height, width=120)

		#-----------------------------------[row 2]----------------------------------------------
		row+=1;
		#col1
		panel.lbl_dst = tk.Label(panel, text="Output folder : ",bg=panel.panel_bg_color)
		panel.lbl_dst.config(font=self.font_courier18,fg=panel.panel_text_color);
		panel.lbl_dst.place(x=50, y=y_offset+(f_y_inc*row))

		#col2 : txt
		panel.txt_dst_file_txtvar = tk.StringVar()
		panel.txt_dst_file= tk.Entry(panel,textvariable=panel.txt_dst_file_txtvar);
		panel.txt_dst_file.config(font=self.font_courier18,fg="green",state='readonly');
		panel.txt_dst_file.place(x=f_x,y=y_offset+((f_y_inc*row)),height=f_height, width=f_width)

		#col3 : button
		panel.btn_dst_browse = tk.Button(panel)
		panel.btn_dst_browse.config(font=self.font_courier18);
		panel.btn_dst_browse["text"] = "Browse"
		panel.btn_dst_browse["command"] = self.onClickDstFileBrowse
		panel.btn_dst_browse.place(x=f_x+f_width+f_margin,y=y_offset+((f_y_inc*row)),height=f_height, width=120)

		#-----------------------------------[row 3]----------------------------------------------
		row+=1;
		#col1 : label
		panel.lbl_trackname = tk.Label(panel, text="Track Name : ",bg=panel.panel_bg_color)
		panel.lbl_trackname.config(font=self.font_courier18,fg=panel.panel_text_color);
		panel.lbl_trackname.place(x=55, y=y_offset+(f_y_inc*row))

		#col2 : txt
		panel.txt_trackname_txtvar = tk.StringVar()
		panel.txt_trackname= tk.Entry(panel,textvariable=panel.txt_trackname_txtvar);
		panel.txt_trackname.config(font=self.font_courier18,fg="green");
		panel.txt_trackname.place(x=f_x,y=y_offset+((f_y_inc*row)),height=f_height, width=f_width);

		#-----------------------------------[row 4]----------------------------------------------
		row+=1;
		#col1 : button
		panel.btn_parase = tk.Button(panel,bg=self.success_bg_color,cursor="arrow")
		panel.btn_parase.config(font=self.font_courier18);
		panel.btn_parase["text"] = "Convert";
		panel.btn_parase["command"]=self.onClickConvert;
		panel.btn_parase.place(x=f_x,y=y_offset+((f_y_inc*row)),height=f_height, width=110)

		#col2 : button
		panel.btn_close = tk.Button(panel,bg=self.danger_bg_color,highlightcolor=self.danger_bg_color)
		panel.btn_close.config(font=self.font_courier18);
		panel.btn_close["text"] = "Close"
		panel.btn_close["command"] = self.container.destroy
		panel.btn_close.place(x=f_x+130,y=y_offset+((f_y_inc*row)),height=f_height, width=100)

	'''
	--------------------------------------------------------------------------------
		Desc: Generate Status Panel
	--------------------------------------------------------------------------------
	'''

	def createPanelStatus(self):
		panel=self.pan_status;
		y_offset=10;
		f_y_inc=40;
		f_margin=30;
		row=-1;

		#-----------------------------------[row 1]----------------------------------------------
		row+=1;
		#col 1 : label
		panel.lbl_status = tk.Label(panel, text="Status: ",bg=panel.panel_bg_color)
		panel.lbl_status.config(font=self.font_courier18,fg=panel.panel_text_color);
		panel.lbl_status.place(x=20, y=y_offset)

		#-----------------------------------[row 2]----------------------------------------------
		row+=1;
		#col 1 : label
		panel.lbl_msg = tk.Label(panel, text="",bg=panel.panel_bg_color)
		panel.lbl_msg.config(font=self.font_courier18,fg=panel.panel_text_color);
		panel.lbl_msg.place(x=20, y=y_offset++((f_y_inc*row)))

		#-----------------------------------[row 2]----------------------------------------------
		row+=1;
		#col1 : play button
		panel.btn_play = tk.Button(panel,bg=self.success_bg_color,cursor="arrow")
		panel.btn_play.config(font=self.font_courier18);
		panel.btn_play["text"] = u'\u25B6';
		panel.btn_play["command"]=self.onClickPlay;
		panel.btn_play.place(x=20,y=y_offset+((f_y_inc*row)),height=45, width=45)

		panel.btn_play.show=(lambda:self.UiOp.showWidget(panel.btn_play));
		panel.btn_play.hide=(lambda:self.UiOp.hideWidget(panel.btn_play));
		panel.btn_play.hide();

		#col1 : stop button
		panel.btn_stop = tk.Button(panel,bg=self.danger_bg_color,cursor="arrow")
		panel.btn_stop.config(font=self.font_courier18);
		panel.btn_stop["text"] = u'\u25FC';
		panel.btn_stop["command"]=self.onClickStop;
		panel.btn_stop.place(x=80,y=y_offset+((f_y_inc*row)),height=45, width=45)

		panel.btn_stop.show=(lambda:self.UiOp.showWidget(panel.btn_stop));
		panel.btn_stop.hide=(lambda:self.UiOp.hideWidget(panel.btn_stop));
		panel.btn_stop.hide();

	'''
	--------------------------------------------------------------------------------
		Desc: Init mixer for the wave file for palying the file.
	--------------------------------------------------------------------------------
	'''
	def intiWaveSound(self,wavefile):
		pygame.init();
		pygame.filename=wavefile;
		pygame.mixer.music.load(wavefile);
		pygame.is_playing=False;
		pygame.is_paused=False;

	'''
	--------------------------------------------------------------------------------
		Desc: Setting the filename of src file in text field
		Return: None
	--------------------------------------------------------------------------------
	'''
	def onClickSrcFileBrowse(self):
		filefullname = filedialog.askopenfilename(filetypes = (("JSON file", "*.json"),("All files", "*.*") ));
		if (len(filefullname)==0):
			return None;

		self.pan_single_track.txt_src_file_txtvar.set(filefullname);
		self.pan_single_track.txt_src_file.focus()
		self.pan_single_track.txt_src_file.xview_moveto(1)
		self.pan_single_track.txt_dst_file_txtvar.set(os.path.dirname(filefullname)+"/")
		self.pan_single_track.txt_dst_file.xview_moveto(1)
		filename=os.path.basename(filefullname);
		index_of_dot = os.path.basename(filename).index('.')
		filename_without_extension = filename[:index_of_dot]
		self.pan_single_track.txt_trackname_txtvar.set(filename_without_extension)

	'''
	--------------------------------------------------------------------------------
		Desc: Setting the folder of o/p file in text field
		Return: None
	--------------------------------------------------------------------------------
	'''
	def onClickDstFileBrowse(self):
		filename = filedialog.askdirectory();
		if (len(filename)==0):
			return None;
		self.pan_single_track.txt_dst_file_txtvar.set(filename);

	'''
	--------------------------------------------------------------------------------
		Desc: On Click for Convert function
	--------------------------------------------------------------------------------
	'''
	def onClickConvert(self):
		if(self.st_btn_convert_funhandler!=None):
			wavefile=self.st_btn_convert_funhandler();
			if(wavefile!=None and wavefile!=''):
				self.intiWaveSound(wavefile);
				self.pan_status.btn_play["text"] = u'\u25B6';

	'''
	--------------------------------------------------------------------------------
		Desc: On Click for Play
	--------------------------------------------------------------------------------
	'''
	def onClickPlay(self):
		if(hasattr(pygame, "is_playing") and pygame.is_playing==False and pygame.is_paused == False):
			pygame.mixer.music.play();
			pygame.is_playing=True;
			pygame.is_paused=False;
			self.pan_status.btn_play["text"] = u'\u23F8';
		elif(hasattr(pygame, "is_playing") and pygame.is_playing==True and pygame.is_paused == False):
			pygame.mixer.music.pause();
			pygame.is_playing=False;
			pygame.is_paused = True;
			self.pan_status.btn_play["text"] = u'\u25B6';
		elif(hasattr(pygame, "is_playing") and pygame.is_playing==False and pygame.is_paused == True):
			pygame.mixer.music.unpause();
			pygame.is_playing=True;
			pygame.is_paused = False;
			self.pan_status.btn_play["text"] = u'\u23F8';

	'''
	--------------------------------------------------------------------------------
		Desc: On Click for Stop
	--------------------------------------------------------------------------------
	'''
	def onClickStop(self):
		if(hasattr(pygame, "is_playing")):
			pygame.mixer.music.stop();
			self.intiWaveSound(pygame.filename);
			self.pan_status.btn_play["text"] = u'\u25B6';

if(__name__=="__main__"):
	root = tk.Tk()
	app = UiApplication(master=root)
	app.mainloop()
