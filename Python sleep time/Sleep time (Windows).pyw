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

  timeEntry = Entry(window, font='arial 14')
  timeEntry.place(height=30,width=150,x=125,y=130)

  status = 'No Sleep Time'

  message = Label(window, text=('''SET THE TIME (SECONDS) 
  TO SHUTDOWN'''), background='#3b5998', font='arial 20',fg='white')
  message.pack()

  statusMessage = Label(window, text=('%s'%(status)), background='#3b5998', font='arial 16',fg='light green')
  statusMessage.pack()

  botao1 = Button(window, text="CONFIRM", background='light green',font='arial 11 bold', command= Confirm)
  botao1.place(height=50,width=100,x=75,y=175)
  
  botao2 = Button(window, text="CANCEL",background='red',font='arial 11 bold', command= Cancel)
  botao2.place(height=50,width=100,x=225,y=175)

def Confirm():
  global statusMessage
  global timeEntry
  global fullTime
  global timeSec
  global timeMin
  global timeHour
  global status

  fullTime = int(timeEntry.get())

  if(fullTime > 0):
    timeMin = fullTime // 60
    timeSec = fullTime % 60
    timeHour = timeMin // 60
    timeMin = timeMin % 60

    status = ('%.2d:%.2d:%.2d' %(timeHour, timeMin, timeSec))
    statusMessage.destroy()
    statusMessage = Label(window, text=('%s'%(status)), background='#3b5998', font='arial 16',fg='light green')
    statusMessage.pack()

    os.system('shutdown /s /f /t %d' %(fullTime))

    Countdown()

  else:
    status = ('Set a valid number')
    statusMessage.destroy()
    statusMessage = Label(window, text=('%s'%(status)), background='#3b5998', font='arial 16',fg='red')
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
    statusMessage = Label(window, text=('%s'%(status)), background='#3b5998', font='arial 16',fg='light green')
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
  global message
  global statusMessage
  global timeEntry
  global fullTime
  global timeSec
  global timeMin
  global timeHour
  global status

  fullTime = 0

  status = 'No Sleep time'
  statusMessage.destroy()
  statusMessage = Label(window, text=('%s'%(status)), background='#3b5998', font='arial 16',fg='light green')
  statusMessage.pack()

  os.system('shutdown /a')

window = Tk()
window.title('Sleep time')
window.configure(background='#3b5998')
window.resizable(width = False, height = False)
window.minsize(width = 400, height = 250) 

Main()

window.mainloop()