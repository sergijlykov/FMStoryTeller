import tkinter
from tkinter import *

def writeFile():
    file = open('monte.txt', 'a+')
    file.write(metinF.get() + '\n' + '\n')
    file.close()

gui = Tk()

metinF = Entry(gui, width = 50)
metinF.grid(row=9, column=1)

buttonWrite = Button(gui)
buttonWrite.config(text='Сохранить в файл', command = writeFile)
buttonWrite.grid(row=8, column=1)

gui.mainloop()

