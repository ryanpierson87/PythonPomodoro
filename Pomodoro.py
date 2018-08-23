# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:37:58 2018

@author: 502755426
"""

from tkinter import *

from tkinter import ttk

from time import *

import os





class PomTimer:

    work_time = 20

    rest_time = 5

    iterations = 1





#---alternates the timer phase between Work and Rest

    def runthru(self):

        global timer

        global display

        #Determines the phase

            #Rest

        if self.iterations % 2 == 0:

            self.timer = "Rest"

            self.display = self.rest_time

            self.workCount.set(self.rest_time)

        else:

            #Work

            self.timer = "Work"

            self.display = self.rest_time

            self.workCount.set(self.work_time)

       #Sets the timer

        self.countdown = (self.workCount.get() * 60)

        #Sets the format

        self.countDisplay.set("{:02d}:{:02d}".format(*divmod(self.countdown, 60)))

        self.countTime = self.workCount.get()

        root.update()



#---Increases timer values

    def value_inc(self, x):

        #Work Timer

        if x == "work_timer":

            self.dispCount, workIn = self.countDisplay, self.workCount

            self.workCount.set(workIn.get() + 1)

            self.workTime.configure(text=workIn.get())

            self.work_time += 1

            self.runthru()

            root.update()

        else:

        #Rest Phase

            self.dispCount, restIn = self.countDisplay, self.restCount

            self.restCount.set(restIn.get() + 1)

            self.restTime.configure(text=restIn.get())

            self.rest_time += 1

            self.runthru()

            root.update()



#decreases timer values

    def value_dec(self, x):

        #Work Timer

        if x == "work_timer":

            self.dispCount, workDec = self.countDisplay, self.workCount

            if workDec.get() > 0:

                self.workCount.set(workDec.get() - 1)

                self.workTime.configure(text=workDec.get())

                self.work_time -= 1

            self.runthru()

            root.update()

        else:

            #Rest Timer

            self.dispCount, restDec = self.countDisplay, self.restCount

            if restDec.get() > 0:

                self.restCount.set(restDec.get() - 1)

                self.restTime.configure(text=restDec.get())

                self.rest_time -= 1

            self.runthru()

            root.update()





    # --timer count down

    def run_time(self):

        if self.countTime > 0:

            for t in range(self.countTime * 60, -1, -1):

                count = "{:02d}:{:02d}".format(*divmod(t, 60))

                self.countDisplay.set(count)

                root.update()

                sleep(1)

    #---Alarm

        duration = 1

        freq = 440

        os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))

        self.iterations += 1

        self.runthru()





#---initializes the object

    def __init__(self, root):

        self.iterations = 1

        self.restCount, self.workCount = IntVar(root, self.rest_time), IntVar(root, self.work_time)

        self.countdown = self.workCount.get() * 60

        self.countTime = self.countdown

        self.countDisplay = StringVar()

        self.countDisplay.set("{:02d}:{:02d}".format(*divmod(self.countdown, 60)))

        self.workCount.set("20")

    # ---Style---



        root.title("Pomodoro Timer")

        root.geometry("250x125")

        root.resizable(width=False, height=True)

        style = ttk.Style()

        style.configure("TLabel", font="Serif 25")



#---Layout classes

#

# ---Labels---

    # --- Timer Label

        self.countEntry = ttk.Label(root,

                                    textvariable=self.countDisplay, anchor="center", width=5)

        self.countEntry.grid(row=0, column=2)



    #--- Work

        self.WorkLabel = ttk.Label(root, text="Work", width=6, anchor="center", font="Serif 15")

        self.WorkLabel.grid(row=1, column=0)



    #---Rest

        self.RestLabel = ttk.Label(root, text="Rest", width=6, anchor="center", font="Serif 15")

        self.RestLabel.grid(row=1, column=3)



    #---Alternating Label

        self.TimerLabel = ttk.Label(root, text="Work", width=6, anchor="center", font="Serif 20")

        self.TimerLabel.grid(row=3, column=2)



# ---Timer Value Displays

    #---Work Minute Value

        self.workTime = ttk.Label(root, text=self.workCount.get(), anchor="center")

        self.workTime.grid(column=0, row=0)



    #---Rest Minute Value

        self.restTime = ttk.Label(root, text=self.restCount.get(), anchor="center")

        self.restTime.grid(column=3, row=0)



# ---Buttons---

    #Work UP

        self.button_wkUp = ttk.Button(root,

                                      text="up",

                                      command=lambda: self.value_inc("work_timer")).grid(row=2, column=0)

    #Work Down

        self.button_wkDown = ttk.Button(root, text="down",

                                        command=lambda: self.value_dec("work_timer")).grid(row=3, column=0)

    #Rest Up

        self.button_rstUp = ttk.Button(root, text="up",

                                       command=lambda: self.value_inc("rest_timer")).grid(row=2, column=3)

    #Rest Down

        self.button_rstDown = ttk.Button(root, text="down",

                                         command=lambda: self.value_dec("rest_timer")).grid(row=3, column=3)

    #Start Timer

        self.button_start = ttk.Button(root, text="Start",

                                       command=lambda: self.run_time()).grid(row=2, column=2)





def on_closing():

    root.destroy()







#---Object creation

root = Tk()

pom = PomTimer(root)

print(PomTimer.work_time)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()



root.quit()