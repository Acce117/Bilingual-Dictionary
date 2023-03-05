from tkinter import *
from dictSpanishEnglish import *

main = Tk()
main_frame = Frame()
word_search_entry = Entry(master=main_frame)
search_button = Button(master=main_frame)
meaning_label = Label(master=main_frame)

def main_config():
    main.title("Cujae English-Spanish")
    main.resizable(False, False)

def main_frame_config():
    main_frame.config(width = 400, height = 400)
    main_frame.config(bg = "blue")
    main_frame.pack()
    
def word_search_entry_config():
    word_search_entry.config(width=42)
    word_search_entry.place(x=30, y=70)

def meaning_label_config():
    meaning_label.config(background="blue")
    meaning_label.place(x=40,y=110)

def search_button_command():
    meaning_label.config(text= get_word_meaning(word_search_entry.get()))

def search_button_config():
    search_button.config(width=10, height=1)
    search_button.config(text="Search")
    search_button.config(command=search_button_command)
    search_button.place(x=290, y=70)

main_config()
main_frame_config()
word_search_entry_config()
search_button_config()
meaning_label_config()

main.mainloop()