from tkinter import *
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk,Image

gui = Tk()
gui.title('FM Story Teller')
gui.iconbitmap('C:/Users/Sergo/PycharmProjects/FMStoryTeller/img/Icon_Books.ico')

def writeFile():
    file = open('Story.txt', 'a+')
    file.write(scrtxt.get("1.0", END) + '\n' + '\n')
    file.close()
    scrtxt.delete("1.0", END)

scrtxt = ScrolledText(gui, height=5, padx = 10, pady = 10); scrtxt.grid(row=1, column=1)

#button to save text.txt
buttonWrite = Button(gui)
buttonWrite.config(text='Save text',padx = 10, pady = 10, command = writeFile)
buttonWrite.grid(row=10, column=1)

gui.mainloop()