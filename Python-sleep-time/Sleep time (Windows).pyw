import os
import time
from tkinter import *

class SleepTime:
  def __init__ (self):

    self.timeEntry = Entry(window, font='arial 14',fg='white',bg='#202021')
    self.timeEntry.place(height=30,width=225,x=37.5,y=145)

    self.status = 'No Sleep time'

    self.message = Label(window, text=('''SET THE TIME
  (MINUTES)'''), background='#121212', font='arial 20',fg='white')
    self.message.pack()

    self.statusMessage = Label(window, text=('''
  %s'''%(self.status)), background='#121212', font='arial 16',fg='#c72344')
    self.statusMessage.pack()

    self.botao1 = Button(window, text="1", background='#1a1a1a',font='arial 14',fg='#ffffff',command=self.key1)
    self.botao1.place(height=40,width=100,x=0,y=210)

    self.botao2 = Button(window, text="2", background='#1a1a1a',font='arial 14',fg='#ffffff',command=self.key2)
    self.botao2.place(height=40,width=100,x=100,y=210)

    self.botao3 = Button(window, text="3", background='#1a1a1a',font='arial 14',fg='#ffffff',command=self.key3)
    self.botao3.place(height=40,width=100,x=200,y=210)

    self.botao4 = Button(window, text="4", background='#1a1a1a',font='arial 14',fg='#ffffff',command=self.key4)
    self.botao4.place(height=40,width=100,x=0,y=250)

    self.botao5 = Button(window, text="5", background='#1a1a1a',font='arial 14',fg='#ffffff',command=self.key5)
    self.botao5.place(height=40,width=100,x=100,y=250)

    self.botao6 = Button(window, text="6", background='#1a1a1a',font='arial 14',fg='#ffffff',command=self.key6)
    self.botao6.place(height=40,width=100,x=200,y=250)

    self.botao7 = Button(window, text="7", background='#1a1a1a',font='arial 14',fg='#ffffff',command=self.key7)
    self.botao7.place(height=40,width=100,x=0,y=290)

    self.botao8 = Button(window, text="8", background='#1a1a1a',font='arial 14',fg='#ffffff',command=self.key8)
    self.botao8.place(height=40,width=100,x=100,y=290)

    self.botao9 = Button(window, text="9", background='#1a1a1a',font='arial 14',fg='#ffffff',command=self.key9)
    self.botao9.place(height=40,width=100,x=200,y=290)

    self.botao0 = Button(window, text="0", background='#1a1a1a',font='arial 14',fg='#ffffff',command=self.key0)
    self.botao0.place(height=40,width=100,x=100,y=330)

    self.botaoBack = Button(window, text="BACKSPACE", background='#1a1a1a',font='arial 10 bold',fg='#ffffff',command=self.backspace)
    self.botaoBack.place(height=40,width=100,x=200,y=330)                  

    self.botaoStart = Button(window, text="START", background='green',font='arial 11 bold', fg='#ffffff',command= self.Start)
    self.botaoStart.place(height=40,width=150,x=0,y=370)
    
    self.botaoCancel = Button(window, text="CANCEL",background='red',font='arial 11 bold', fg='#ffffff',command= self.Cancel)
    self.botaoCancel.place(height=40,width=150,x=150,y=370)

  def key1(self):
    self.timeEntry.insert(END, '1')

  def key2(self):
    self.timeEntry.insert(END, '2')

  def key3(self):
    self.timeEntry.insert(END, '3')

  def key4(self):
    self.timeEntry.insert(END, '4')

  def key5(self):
    self.timeEntry.insert(END, '5')

  def key6(self):
    self.timeEntry.insert(END, '6')

  def key7(self):
    self.timeEntry.insert(END, '7')

  def key8(self):
    self.timeEntry.insert(END, '8')

  def key9(self):
    self.timeEntry.insert(END, '9')

  def key0(self):
    self.timeEntry.insert(END, '0')    

  def backspace(self):
    finalNum = len(self.timeEntry.get()) -1  
    self.timeEntry.delete(int(finalNum))


  def Start(self):

    self.fullTime = int(self.timeEntry.get())

    if(self.fullTime > 0):
      self.timeHour = self.fullTime // 60
      self.timeMin = self.fullTime % 60
      self.timeSec = 0

      self.status = ('%.2d:%.2d:%.2d' %(self.timeHour, self.timeMin, self.timeSec))

      self.statusMessage.destroy()
      self.statusMessage = Label(window, text=('''
  %s'''%(self.status)), background='#121212', font='arial 16',fg='#c72344')
      self.statusMessage.pack()

      self.fullTime *= 60

      os.system('shutdown /s /f /t %d' %(self.fullTime))
      print('Started Shutdown (%s)' %(self.status))
      self.Countdown()

    else:
      self.status = ('Set a valid number')
      self.statusMessage.destroy()
      self.statusMessage = Label(window, text=('''
  %s'''%(self.status)), background='#121212', font='arial 16',fg='red')
      self.statusMessage.pack()

  def Countdown(self):

    while(self.fullTime > 0):
      self.status = ('%.2d:%.2d:%.2d' %(self.timeHour, self.timeMin, self.timeSec)) 

      self.statusMessage.destroy()
      self.statusMessage = Label(window, text=('''
  %s'''%(self.status)), background='#121212', font='arial 16',fg='#c72344')
      self.statusMessage.pack()

      window.update()
      
      time.sleep(1)

      if(self.timeSec >= 0):
        self.timeSec -= 1

      if(self.timeSec < 0 and self.timeMin > 0):
        self.timeMin -= 1
        self.timeSec = 59

      if(self.timeSec < 0 and self.timeMin == 0 and self.timeHour > 0):
        self.timeHour -= 1
        self.timeSec = 59
        self.timeMin = 59

      self.fullTime -= 1

  def Cancel(self):

    self.fullTime = 0

    print('Canceled Shutdown (%s)' %(self.status))

    self.status = 'No Sleep time'
    
    self.statusMessage.destroy()
    self.statusMessage = Label(window, text=('''
  %s'''%(self.status)), background='#121212', font='arial 16',fg='#c72344')
    self.statusMessage.pack()

    os.system('shutdown /a')

window = Tk()
window.title('Sleep time')
window.configure(background='#121212')
window.resizable(width = False, height = False)
window.minsize(width = 300, height = 410) 

SleepTime()

window.mainloop()