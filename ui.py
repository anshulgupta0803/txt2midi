#!/usr/bin/python3.5

import tkinter as tk
from tkinter import font
from tkinter import filedialog
class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master);
		self.container=master;
		self.setWinProp(master);
		self.pack(fill='both', expand='yes')
		#appHighlightFont = font.Font(family='Helvetica', size=20, weight='bold')
		#font.families()
		self.createWidgets();

	def setWinProp(self,win):
		win.minsize(width=666, height=666);
		win.resizable(width=False, height=False);
		win.geometry("%dx%d+%d+%d" % (300, 300, 500, 0));

	def createWidgets(self):

		f_width=250;
		f_height=35;
		f_x=200;
		y_offset=10;
		f_y_inc=80;
		f_margin=30;
		helv36 = font.Font(family='Helvetica',size=18)
		row=-1;

		#row 1
		row+=1;
		#col 1 : lable
		self.lbl_src = tk.Label(self, text="Source file : ")
		self.lbl_src.config(font=helv36,fg="brown");
		self.lbl_src.place(x=40, y=y_offset)

		#col 2 :text
		self.txt_src_file_txtvar = tk.StringVar()
		self.txt_src_file= tk.Entry(self,textvariable=self.txt_src_file_txtvar);
		self.txt_src_file.config(font=helv36,fg="green",state='readonly');
		self.txt_src_file.place(x=f_x,y=y_offset+3,height=f_height, width=f_width)

		#col 3 : button
		self.btn_browse = tk.Button(self)
		self.btn_browse.config(font=helv36);
		self.btn_browse["text"] = "Browse"
		self.btn_browse["command"] = self.srcfileBrowse
		self.btn_browse.place(x=f_x+f_width+f_margin,y=y_offset+3,height=f_height, width=120)

		#row 2
		row+=1;
		#col1
		self.lbl_dst = tk.Label(self, text="Dst folder : ")
		self.lbl_dst.config(font=helv36,fg="brown");
		self.lbl_dst.place(x=40, y=y_offset+(f_y_inc*row))

		#col2 : txt
		self.txt_dst_file_txtvar = tk.StringVar()
		self.txt_dst_file= tk.Entry(self,textvariable=self.txt_dst_file_txtvar);
		self.txt_dst_file["width"]="20";
		self.txt_dst_file.config(font=helv36,fg="green",state='readonly');
		self.txt_dst_file.place(x=f_x,y=y_offset+((f_y_inc*row))+3,height=f_height, width=f_width)

		#col3 : button
		self.btn_dst_browse = tk.Button(self)
		self.btn_dst_browse.config(font=helv36);
		self.btn_dst_browse["text"] = "Browse"
		self.btn_dst_browse["command"] = self.dstfileBrowse
		self.btn_dst_browse.place(x=f_x+f_width+f_margin,y=y_offset+((f_y_inc*row))+3,height=f_height, width=120)

		self.quit = tk.Button(self, text="Close", fg="red",command=self.container.destroy)
		self.quit.pack(side="bottom")


	def srcfileBrowse(self):
		filename = filedialog.askopenfilename(filetypes = (("Text file", "*.txt"),("All files", "*.*") ));
		self.txt_src_file_txtvar.set(filename)

	def dstfileBrowse(self):
		filename = filedialog.askdirectory();
		self.txt_dst_file_txtvar.set(filename)

root = tk.Tk()
app = Application(master=root)
app.master.title("Converter : SaReGaMa")
app.mainloop()
