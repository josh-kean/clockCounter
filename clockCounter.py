#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 19:28:59 2018

@author: josh
"""

from tkinter import *





class Clock:
    def __init__(self, master):
        frame = Frame(master)
        frame.grid(row = '0', column = '0')
        leftFrame = Frame(master)
        leftFrame.grid(row = '0', column = '1')
        displayFrame = Frame(master)
        displayFrame.grid(row = '1')
        
        self.timeInput = [12.31, 08.23, 15.47]
                
        self.addTimeButton = Button(leftFrame, text = "Add time to list in ##.## format", command = self.appendTime)
        self.addTimeButton.pack(side = TOP)
        self.timeInputBox = Entry(leftFrame)
        self.timeInputBox.pack(side = BOTTOM)
        
        self.secondsButton = Button(frame, text = "print seconds", command = self.returnTotalSeconds)
        self.secondsButton.pack(side = TOP)
        self.minutesButton = Button(frame, text = "print minutes", command = self.returnTotalMinutes)
        self.minutesButton.pack(side = TOP)
        self.hoursButton = Button(frame, text = "print hours", command = self.returnTotalHours)
        self.hoursButton.pack(side = TOP)
        
        self.resultWindow = Text(displayFrame)
        self.resultWindow.pack()

        
               
    def appendTime(self):
        self.newTime = self.timeInputBox.get()
        self.timeInput.append(float(self.newTime))


    def returnTotalSeconds(self):
        self.resultWindow.delete('1.0', END)
        self.seconds = sum([(second - int(second)) for second in self.timeInput])
        self.minutes = sum([int(minute) for minute in self.timeInput])
        self.resultWindow.insert('1.0',str(self.minutes*60 + self.seconds))
        
    def returnTotalMinutes(self):
        self.resultWindow.delete('1.0', END)
        self.seconds = sum([(second - int(second)) for second in self.timeInput])
        self.minutes = sum([int(minute) for minute in self.timeInput])
        self.resultWindow.insert('1.0',str(self.minutes + self.seconds/60))
    
    def returnTotalHours(self):
        self.resultWindow.delete('1.0', END)
        self.seconds = sum([(second - int(second)) for second in self.timeInput])
        self.minutes = sum([int(minute) for minute in self.timeInput])
        self.resultWindow.insert('1.0',str((self.minutes/60+self.seconds/3600)))
        



root = Tk()


b = Clock(root)
        

root.mainloop()
    
