from tkinter import *
from pygame import mixer

player_window= Tk()   #intializing the window 

mixer.init() #intializing the mixer otherwise it doesnt work

player_window.geometry('400x400')
player_window.title("Fer_player")
player_window.iconbitmap(r'icon1.ico')   #creat an icon for the window

#button_1 = 
text =Label(player_window,text = "Feroz Music Player, Click the bellow button to listen happier music")
text.pack()
play_photo = PhotoImage(file = 'btn.jpg')   #imported a photo, any formath accepted
#labelphoto = Label(player_window, image = photo)
#labelphoto.pack()
def play_music():
	mixer.music.load("happier.mp3")
	mixer.music.play()
	print("hi, Welcome to Feroz Music player")

playBtn = Button(player_window, image = play_photo,command = play_music)
playBtn.pack()

player_window.mainloop()

