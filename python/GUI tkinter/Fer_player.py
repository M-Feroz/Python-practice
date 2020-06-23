from tkinter import *
root= Tk()
root.geometry('400x400')
root.title("Fer_player")
root.iconbitmap(r'icon1.ico')

photo = PhotoImage(file = 'btn.png')
labelphoto = Label(root, image = photo)
labelphoto.pack()
root.mainloop()
