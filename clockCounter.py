"""
Created on Wed Sep 19 19:28:59 2018

@author: josh
"""

from tkinter import *


class Clock:
    def __init__(self, master):
#frame for time buttons
        frame = Frame(master)
        frame.grid(row = '0', column = '0')
#frame for add time button
        rightFrame = Frame(master)
        rightFrame.grid(row = '0', column = '1')
        rightFrame.bind('<G>', self.appendTime)
#frame to show results
        displayFrame = Frame(master)
        displayFrame.grid(row = '1', columnspan = 2)

#function to map master to 'enter' button
        self.timeInput = []
        self.timeResults = [0,0,0]
        self.seconds = sum([(second - int(second))*10 for second in self.timeInput])
        self.minutes = sum([int(minute) for minute in self.timeInput])
        self.hours = self.minutes/60+self.seconds/3600

        self.addTimeButton = Button(rightFrame, text = "Add time to list in ##.## format", command = self.appendTime)
        rightFrame.bind('<Return>', self.appendTime)
        self.addTimeButton.pack(side = TOP)
        self.timeInputBox = Entry(rightFrame)
        self.timeInputBox.pack(side = BOTTOM)

        self.secondsButton = Button(frame, text = "print seconds", command = self.returnTotalSeconds)
        self.secondsButton.pack(side = TOP)
        self.minutesButton = Button(frame, text = "print minutes", command = self.returnTotalMinutes)
        self.minutesButton.pack(side = TOP)
        self.hoursButton = Button(frame, text = "print hours", command = self.returnTotalHours)
        self.hoursButton.pack(side = LEFT)

        self.resultLabel = Label(displayFrame, text = "Time")
        self.resultLabel.grid(row = '0', column = '0')

        self.timeListLabel = Label(displayFrame, text = "List of Inputs")
        self.timeListLabel.grid(row = '0', column = '1')

        self.resultWindow = Text(displayFrame)
        self.resultWindow.grid(row = '1', column = '0')
        self.timeStringWindow = Text(displayFrame)
        self.timeStringWindow.grid(row = '1', column = '1')

        self.timeStringWindow.insert('1.0', 'total time is: ')
        self.timeStringWindow.insert('2.0', self.timeInput)

        self.csvButton = Button(csvFrame, text = "Generate CSV File", command = self.generateCSV)
        self.csvButton.pack()


    def formatTime(self, time):
        if len(time) == 5:
            return time
        elif len(time) == 3:
            return '0'+time+'0'
        elif len(time) == 4 and time[2] == '.':
            return time+'0'
        elif len(time) == 4 and time[1] == '.':
            return '0'+time
        elif '.' not in time:
            return time+'.00'
        elif time[0] == '.':
            return '00'+time
        else:
            return '00.00'

    def appendTime(self):
        self.timeStringWindow.delete('1.0', END)
        self.newTime = self.timeInputBox.get()
        self.newTime = self.formatTime(self.newTime)
        self.timeInput.append(float(self.newTime))
        self.timeStringWindow.insert('1.0', 'total time is: ')
        self.timeStringWindow.insert('2.0', self.timeInput)
        self.seconds = sum([(second - int(second)) for second in self.timeInput])
        self.minutes = sum([int(minute) for minute in self.timeInput])
        self.hours = self.minutes/60+self.seconds/3600
        self.timeInputBox.delete(0, 'end')

    def returnTotalSeconds(self):
        self.resultWindow.delete('1.0', END)
        self.seconds = sum([(second - int(second))*100 for second in self.timeInput])
        self.minutes = sum([int(minute) for minute in self.timeInput])
        self.hours = self.minutes/60+self.seconds/3600
        self.resultWindow.insert('0.0',str(self.minutes*60 + self.seconds))
        self.timeResults[0] = self.seconds
        self.resultLabel.config(text ="time in seconds")

    def returnTotalMinutes(self):
        self.resultWindow.delete('1.0', END)
        self.seconds = sum([(second - int(second))*100 for second in self.timeInput])
        self.minutes = sum([int(minute) for minute in self.timeInput])
        self.hours = self.minutes/60+self.seconds/3600
        self.value = self.minutes + self.seconds/60
        self.resultWindow.insert('1.0', "{:.2f}".format(self.value))
        self.resultLabel.config(text ="time in minutes")

    def returnTotalHours(self):
        self.resultWindow.delete('1.0', END)
        self.seconds = sum([(second - int(second))*100 for second in self.timeInput])
        self.minutes = sum([int(minute) for minute in self.timeInput])
        self.hours = self.minutes/60+self.seconds/3600
        self.value = self.minutes/60+self.seconds/3600
        self.resultWindow.insert('1.0', "{:.2f}".format(self.value))
        self.resultLabel.config(text ="time in hours")

root = Tk()
b = Clock(root)
root.mainloop()
