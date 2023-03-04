from tkinter import *

main = Tk()

frame = Frame()

def main_config():
    main.title("Cujae English-Spanish")
    main.resizable(False, False)

def frame_config():
    frame.config(width = 800, height = 600)
    frame.config(bg = "blue")
    frame.pack()
    frame.config(bd = 5)
    frame.config(relief = "sunken")

main_config()
frame_config()

main.mainloop()