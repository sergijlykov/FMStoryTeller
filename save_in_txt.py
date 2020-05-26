import tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter.scrolledtext import ScrolledText

#writing entry to txt file named monte.txt
def writeFile():
    file = open('monte.txt', 'a+')
    file.write(metinF.get() + '\n' + '\n')
    file.close()
    metinF.delete(0, END)

#gui preferences
gui = Tk()
gui.title('FM Story Teller')
gui.iconbitmap('C:/Users/Sergo/PycharmProjects/FMStoryTeller/img/Icon_Books.ico')
gui.geometry('325x150')

# Label(gui, text="ScrolledText Box:").grid(row=1, column=0)
# st = ScrolledText(gui, height=5); st.grid(row=1, column=1)
# Button(gui, text="Print Text", command=(lambda: writeFile)).grid(row=1, column=2, sticky="EW")

#entry field size and position
metinF = Entry(gui, width = 50)
metinF.grid(row=9, column=1, padx = 10, pady = 10)

#button to save entry text in monte.txt
buttonWrite = Button(gui)
buttonWrite.config(text='Сохранить в файл',padx = 10, pady = 10, command = writeFile)
buttonWrite.grid(row=10, column=1)

gui.mainloop()

