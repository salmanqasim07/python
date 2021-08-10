from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk
#from pathlib import path
import vlc
import pathlib
filetoplay= ''
def open_file():
	global filetoplay
	fln=filedialog.askopenfilename(pathlib.path.cwd(),
	title="Select Music", filetype=(("Music FIle mp3", "*.mp3"),("All Files", "*.*")))
	fls.set("Track: "+pathlib.path.basename(fln))
	filetoplay = fln

def play_music():
	if filetoplay == '':
		messagebox.showerror(title="Track Error!",
		message="No Track Selected")

	track = vlc_obj.media_new(fln)
	player.set_media(track)
	player.play()

def stop_music():
	player.stop()

root=Tk()
fls=StringVar()
fls.set("Track: No Track Select")
root.title("Music Player By Salman and Sadaqt")

wrapper = LabelFrame(root, text="Music Player")
wrapper.pack(fill="both",expand="yes", padx=10, pady=10)

label = Label(wrapper, textvariable=fls)
label.pack()

button1=Button(wrapper, text="Track", command=open_file)
button1.pack(side=tk.LEFT, padx=15,)
button2=Button(wrapper, text="Play", command=play_music)
button2.pack(side=tk.LEFT, padx=15,)
button3=Button(wrapper, text="Stop", command=stop_music)
button3.pack(side=tk.LEFT, padx=15)
button4=Button(wrapper, text="Exit", command=lambda: exit())
button4.pack(side=tk.LEFT, padx=15)



root.geometry("400x150")
root.resizable(False,False)
root.mainloop()
