from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk
#from pathlib import path
import vlc
import pathlib
import os

filetoplay= ''
current_volume = 70  # Default volume level

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
		return

	track = vlc_obj.media_new(filetoplay)
	player.set_media(track)
	player.play()
	
def stop_music():
	player.stop()
	
def volume_up():
	global current_volume
	if current_volume < 100:
		current_volume += 10
		player.audio_set_volume(current_volume)
		volume_var.set(f"Volume: {current_volume}%")
		
def volume_down():
	global current_volume
	if current_volume > 0:
		current_volume -= 10
		player.audio_set_volume(current_volume)
		volume_var.set(f"Volume: {current_volume}%")

# Initialize VLC instance
vlc_obj = vlc.Instance()
player = vlc_obj.media_player_new()

root=Tk()
fls=StringVar()
volume_var=StringVar()
volume_var.set(f"Volume: {current_volume}%")
fls.set("Track: No Track Select")
root.title("Music Player By Salman and Sadaqt")

wrapper = LabelFrame(root, text="Music Player")
wrapper.pack(fill="both",expand="yes", padx=10, pady=10)

label = Label(wrapper, textvariable=fls)
label.pack()

volume_label = Label(wrapper, textvariable=volume_var)
volume_label.pack()

button1=Button(wrapper, text="Track", command=open_file)
button1.pack(side=tk.LEFT, padx=15,)
button2=Button(wrapper, text="Play", command=play_music)
button2.pack(side=tk.LEFT, padx=15,)
button3=Button(wrapper, text="Stop", command=stop_music)
button3.pack(side=tk.LEFT, padx=15)
button4=Button(wrapper, text="Vol+", command=volume_up)
button4.pack(side=tk.LEFT, padx=15)
button5=Button(wrapper, text="Vol-", command=volume_down)
button5.pack(side=tk.LEFT, padx=15)
button6=Button(wrapper, text="Exit", command=lambda: exit())
button6.pack(side=tk.LEFT, padx=15)

root.geometry("550x180")
root.resizable(False,False)
root.mainloop()
