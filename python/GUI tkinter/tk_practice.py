from tkinter import *
window = Tk()
window.geometry("300x300")
window.title("TK tutorial")

label_1 = Label(window,text="Welcome to the TK Tutorial",fg ='blue', bg='pink',relief = "solid", font = ("arial",12,"bold"))
label_1.pack()

button_1 = Button(window,text="Demo",fg ='yellow', bg='brown',relief = RAISED, font = ("arial",12,"bold"))
button_1.place(x=110,y=110)                     #GROOVE, RIDGE, SUNKEN, RAISED
window.mainloop()
