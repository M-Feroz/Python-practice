from tkinter import *
from pygame import mixer

root= Tk()

mixer.init() #intializing the mixer otherwise it doesnt work

root.geometry('400x400')
root.title("Fer_player")
root.iconbitmap(r'icon1.ico')

#button_1 = 
text =Label(root,text = "Feroz Music player")
text.pack()
play_photo = PhotoImage(file = 'btn.png')
#labelphoto = Label(root, image = photo)
#labelphoto.pack()
def play_music():
	mixer.music.load("happier.mp3")
	mixer.music.play()
	#print("hi it is play button")

playBtn = Button(root, image = play_photo,command = play_music)
playBtn.pack()

root.mainloop()

