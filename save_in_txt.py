import tkinter
from tkinter import *
from PIL import ImageTk,Image

def writeFile():
    file = open('monte.txt', 'a+')
    file.write(metinF.get() + '\n' + '\n')
    file.close()
    metinF.delete(0, END)

gui = Tk()
gui.title('FM Story Teller')
gui.iconbitmap('C:/Users/Sergo/PycharmProjects/FMStoryTeller/img/Icon_Books.ico')
gui.geometry('300x150')

metinF = Entry(gui, width = 50)
metinF.grid(row=9, column=1)


buttonWrite = Button(gui)
buttonWrite.config(text='Сохранить в файл', command = writeFile)
buttonWrite.grid(row=10, column=1)

gui.mainloop()

