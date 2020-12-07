import os
import time
from tkinter import *

def Main():
  global message
  global statusMessage
  global status
  global timeEntry
  global fullTime
  global botaoStart
  global botaoCancel
  global timeSec
  global timeMin
  global timeHour
  global botao1
  global botao2
  global botao3
  global botao4
  global botao5
  global botao6
  global botao7
  global botao8
  global botao9
  global botao0
  global botaoBack


  timeEntry = Entry(window, font='arial 14',fg='white',bg='#202021')
  timeEntry.place(height=30,width=225,x=37.5,y=145)

  status = 'No Sleep time'

  message = Label(window, text=('''SET THE TIME
(MINUTES)'''), background='#121212', font='arial 20',fg='white')
  message.pack()

  statusMessage = Label(window, text=('''
%s'''%(status)), background='#121212', font='arial 16',fg='#c72344')
  statusMessage.pack()

  botao1 = Button(window, text="1", background='#1a1a1a',font='arial 14',fg='#ffffff',command=key1)
  botao1.place(height=40,width=100,x=0,y=210)

  botao2 = Button(window, text="2", background='#1a1a1a',font='arial 14',fg='#ffffff',command=key2)
  botao2.place(height=40,width=100,x=100,y=210)

  botao3 = Button(window, text="3", background='#1a1a1a',font='arial 14',fg='#ffffff',command=key3)
  botao3.place(height=40,width=100,x=200,y=210)

  botao4 = Button(window, text="4", background='#1a1a1a',font='arial 14',fg='#ffffff',command=key4)
  botao4.place(height=40,width=100,x=0,y=250)

  botao5 = Button(window, text="5", background='#1a1a1a',font='arial 14',fg='#ffffff',command=key5)
  botao5.place(height=40,width=100,x=100,y=250)

  botao6 = Button(window, text="6", background='#1a1a1a',font='arial 14',fg='#ffffff',command=key6)
  botao6.place(height=40,width=100,x=200,y=250)

  botao7 = Button(window, text="7", background='#1a1a1a',font='arial 14',fg='#ffffff',command=key7)
  botao7.place(height=40,width=100,x=0,y=290)

  botao8 = Button(window, text="8", background='#1a1a1a',font='arial 14',fg='#ffffff',command=key8)
  botao8.place(height=40,width=100,x=100,y=290)

  botao9 = Button(window, text="9", background='#1a1a1a',font='arial 14',fg='#ffffff',command=key9)
  botao9.place(height=40,width=100,x=200,y=290)

  botao0 = Button(window, text="0", background='#1a1a1a',font='arial 14',fg='#ffffff',command=key0)
  botao0.place(height=40,width=100,x=100,y=330)

  botaoBack = Button(window, text="BACKSPACE", background='#1a1a1a',font='arial 10 bold',fg='#ffffff',command=backspace)
  botaoBack.place(height=40,width=100,x=200,y=330)                  

  botaoStart = Button(window, text="START", background='green',font='arial 11 bold', fg='#ffffff',command= Start)
  botaoStart.place(height=40,width=150,x=0,y=370)
  
  botaoCancel = Button(window, text="CANCEL",background='red',font='arial 11 bold', fg='#ffffff',command= Cancel)
  botaoCancel.place(height=40,width=150,x=150,y=370)

def key1():
  global timeEntry

  timeEntry.insert(END, '1')
  print('1')

def key2():
  global timeEntry

  timeEntry.insert(END, '2')

def key3():
  global timeEntry

  timeEntry.insert(END, '3')

def key4():
  global timeEntry

  timeEntry.insert(END, '4')

def key5():
  global timeEntry

  timeEntry.insert(END, '5')

def key6():
  global timeEntry

  timeEntry.insert(END, '6')

def key7():
  global timeEntry

  timeEntry.insert(END, '7')

def key8():
  global timeEntry

  timeEntry.insert(END, '8')

def key9():
  global timeEntry
  
  timeEntry.insert(END, '9')

def key0():
  global timeEntry

  timeEntry.insert(END, '0')    

def backspace():
  global timeEntry

  finalNum = len(timeEntry.get()) -1  
  timeEntry.delete(int(finalNum))


def Start():
  global statusMessage
  global timeEntry
  global fullTime
  global timeSec
  global timeMin
  global timeHour
  global status

  fullTime = int(timeEntry.get())

  if(fullTime > 0):
    timeHour = fullTime // 60
    timeMin = fullTime % 60
    timeSec = 0

    status = ('%.2d:%.2d:%.2d' %(timeHour, timeMin, timeSec))

    statusMessage.destroy()
    statusMessage = Label(window, text=('''
%s'''%(status)), background='#121212', font='arial 16',fg='#c72344')
    statusMessage.pack()

    fullTime *= 60

    os.system('shutdown /s /f /t %d' %(fullTime))

    Countdown()

  else:
    status = ('Set a valid number')
    statusMessage.destroy()
    statusMessage = Label(window, text=('''
%s'''%(status)), background='#121212', font='arial 16',fg='red')
    statusMessage.pack()

def Countdown():
  global statusMessage
  global fullTime
  global timeSec
  global timeMin
  global timeHour
  global status

  while(fullTime > 0):
    status = ('%.2d:%.2d:%.2d' %(timeHour, timeMin, timeSec)) 

    statusMessage.destroy()
    statusMessage = Label(window, text=('''
%s'''%(status)), background='#121212', font='arial 16',fg='#c72344')
    statusMessage.pack()

    window.update()
    
    time.sleep(1)

    if(timeSec >= 0):
      timeSec -= 1

    if(timeSec < 0 and timeMin > 0):
      timeMin -= 1
      timeSec = 59

    if(timeSec < 0 and timeMin == 0 and timeHour > 0):
      timeHour -= 1
      timeSec = 59
      timeMin = 59

    fullTime -= 1

def Cancel():
  global statusMessage
  global fullTime
  global status

  fullTime = 0

  status = 'No Sleep time'
  
  statusMessage.destroy()
  statusMessage = Label(window, text=('''
%s'''%(status)), background='#121212', font='arial 16',fg='#c72344')
  statusMessage.pack()

  os.system('shutdown /a')

window = Tk()
window.title('Sleep time')
window.configure(background='#121212')
window.resizable(width = False, height = False)
window.minsize(width = 300, height = 410) 

Main()

window.mainloop()