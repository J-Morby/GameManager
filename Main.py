from tkinter import *

class GameObject:

    def __init__(self):
        self.icon = ""
        self.location = ""
        self.x = 0
        self.y = 0



WindowName = "GameManager"

window = Tk()

window.title(f"{WindowName}")
window.geometry('500x500')

window.mainloop()