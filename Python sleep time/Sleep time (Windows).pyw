import os
from tkinter import *

def Main():
  global message
  global timeEntry
  global time
  global botao1
  global botao2

  timeEntry = Entry(window, font='arial 15 bold')
  timeEntry.place(height=30,width=150,x=125,y=80)

  message = Label(window, text='''SET THE TIME (SECONDS) 
  TO SHUTDOWN''',background='#3b5998', font='arial 18 bold',fg='white')
  message.pack()

  botao1 = Button(window, text="CONFIRM", background='light green',font='arial 11 bold', command= Confirm)
  botao1.place(height=50,width=100,x=75,y=125)

  botao2 = Button(window, text="CANCEL",background='red',font='arial 11 bold', command= Cancel)
  botao2.place(height=50,width=100,x=225,y=125)

def Confirm():
  global message
  global timeEntry
  global time
  global botao1
  global botao2

  time = int(timeEntry.get())
  os.system('shutdown /s /f /t %d' %(time))

def Cancel():
  global message
  global timeEntry
  global time
  global botao1
  global botao2

  os.system('shutdown /a')



window = Tk()
window.title('Shutdown')
window.configure(background='#3b5998')
window.resizable(width = False, height = False)
window.minsize(width = 400, height = 200) 

Main()

window.mainloop()