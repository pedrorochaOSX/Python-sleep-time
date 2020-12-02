import os
import time
from tkinter import *

def Main():
  global message
  global statusMessage
  global status
  global timeEntry
  global fullTime
  global botao1
  global botao2
  global timeSec
  global timeMin
  global timeHour

  timeEntry = Entry(window, font='arial 14',fg='white',bg='#202021')
  timeEntry.place(height=30,width=125,x=62.5,y=145)

  status = 'No Sleep time'

  message = Label(window, text=('''SET THE TIME
(MINUTES)'''), background='#121212', font='arial 20',fg='white')
  message.pack()

  statusMessage = Label(window, text=('''
%s'''%(status)), background='#121212', font='arial 16',fg='light green')
  statusMessage.pack()

  botao1 = Button(window, text="START", background='green',font='arial 11 bold', command= Start)
  botao1.place(height=40,width=125,x=0,y=210)
  
  botao2 = Button(window, text="CANCEL",background='red',font='arial 11 bold', command= Cancel)
  botao2.place(height=40,width=125,x=125,y=210)

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
%s'''%(status)), background='#121212', font='arial 16',fg='light green')
    statusMessage.pack()

    os.system('shutdown -h %d' %(fullTime))

    fullTime *= 60

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
%s'''%(status)), background='#121212', font='arial 16',fg='light green')
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
%s'''%(status)), background='#121212', font='arial 16',fg='light green')
  statusMessage.pack()

  os.system('shutdown -c')

window = Tk()
window.title('Sleep time')
window.configure(background='#121212')
window.resizable(width = False, height = False)
window.minsize(width = 250, height = 250) 

Main()

window.mainloop()