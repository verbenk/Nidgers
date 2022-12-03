
from tkinter import *
import os

# tk
root = Tk()
root['bg'] = 'green'
root.title('MAIN')
root.geometry('175x200')
root.resizable(width=False, height=False)

# cavnas
canvas = Canvas(root, width='175', height='200', bg='black')
canvas.pack()

# COM
def oneCOM():
    root.destroy()
    os.system('python kahoot.py')


def twoCOM():
    root.destroy()
    os.system('python ping-phong.py')

def ponosCOM():
    root.destroy()
    os.system('python zmia.py')

def yaderniiponosCOM():
    root.destroy()
    os.system('python teteriks.py')

def kakahaCOM():
    root.destroy()
    os.system('python slidepuzzle.py')

# elements
oneBut = Button(canvas, text='KAHOOT', bg='yellow', font=10, width=15, command=oneCOM)
oneBut.pack()
twoBut = Button(canvas, text='PING-PHONK', bg='white', font=10, width=15, command=twoCOM)
twoBut.pack()
ponosBut = Button(canvas, text='ZMIA', bg='blue', font=10, width=15, command=ponosCOM)
ponosBut.pack()
yaderniiponosCOM = Button(canvas, text='teteriks', bg='grey', font=10, width=15, command=yaderniiponosCOM)
yaderniiponosCOM.pack()
kakahaCOM = Button(canvas, text='slidepuzzle', bg='purple', font=10, width=15, command=kakahaCOM)
kakahaCOM.pack()
# tk
root.mainloop()