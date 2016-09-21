#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
import tkMessageBox
import tableList
import clipboard
import time
import random


class reactionTimeGUI(Tkinter.Tk):
    windowExist = 1 #pour bypasser le self.mainloop()
    
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize() # An itialize function have been defined to generate all the widgets
       
    
    def initialize(self):
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.waitForStimulus = 0
        
        
        self.resizable(True,False)    
        self.grid() 
        self.grid_columnconfigure(0,weight=1)
        
        button1 = Tkinter.Button(self,text="Effacer toutes les données",command = self.clearData,bg = "green")
        button1.grid(column=1,row=0 )
        
        buttonDelLast = Tkinter.Button(self,text="Effacer la dernière donnée",command = self.clearLastData,bg = "green")
        buttonDelLast.grid(column=1,row=1 )
        
        button2 = Tkinter.Button(self,text="Copier les données dans le presse-papier !",command = self.processToClipBoard)
        button2.grid(column=1,row=2 )
        
      
        
        
        """
        label1Variable = Tkinter.StringVar()
        label1 = Tkinter.Label(self,textvariable = label1Variable)
        label1.grid(column=0,row=2,columnspan=3)
    
        
        label1Variable.set("\n\n\nCliquez le boutton «Commencer l'expérience» pour débuter\n\n\n")
        
        """
        self.button3 =  Tkinter.Button(self,text="Commencer l'expérience",command = self.reactionTimeExp)
        self.button3.grid(column=0,row=4,columnspan = 3,sticky = "WENS")
        
        self.experimentButton = Tkinter.Button(self,
                                               text = "Appuyer sur «Commencer l'expérience» pour débuter...",
                                               state = "disabled",
                                               command = self.experimentButtonCallBack)
        self.experimentButton.grid(column=0,row=5,columnspan=3,rowspan = 3,sticky = "WE")
        
        self.table = tableList.TableList(self, 
        background = "white",
        columns = (0, "Essai", 0, "Temps de réaction (s)"),
        stretch = "all",
        width = 50,
        setfocus = 1, ###this lets you use keyboard navigation
        activestyle = "none",
        takefocus = 0
        )
        self.table.grid(column = 2,row =0,rowspan = 3)
        self.table.insert("end",("1","Commencer l'expérience pour voir des données."))
        
        self.reactionTimeData = []
        self.rTExpOn = 0;
        self.start_time = 0
        self.waitForUser = 0
        
        
    def reactionTimeExp(self): #Début du reaction time Exp 
        print "reactionTimeExperiment"
        self.button3.config(state = "disabled")
        self.experimentButton.config(state = "normal",text = "Ne pas appuyer sur le boutton")
        
        self.waitForStimulus = 1
        self.stimulusTime = time.time()+1.5+random.random()*2
        print "time to wait = "+ str(self.stimulusTime)
        
        
        """
        
        if self.rTExpOn==0:
            self.start_time = time.time()
            self.rTExpOn=1
            return
        elapsedTime = time.time()-self.start_time
        print elapsedTime
        self.reactionTimeData.append(elapsedTime)
        self.writeDataToTable()
        self.rTExpOn = 0
        """    
        
    def experimentButtonCallBack(self):
        if self.waitForUser:
            elapsedTime = time.time()-self.stimulusTime
            print elapsedTime
            self.waitForUser = 0
            
            self.experimentButton.config(text = "Appuyer sur «Commencer l'expérience» pour débuter...",
                                               state = "disabled")
            self.button3.config(state = "normal")
            self.reactionTimeData.append(elapsedTime)
            self.writeDataToTable()
            
        else:
            self.experimentButton.config(text = "Essaies-tu de tricher? Recommence... ",
                                               state = "disabled")
            self.waitForUser = 0
            self.button3.config(state = "normal")
            self.waitForStimulus = 0
            
        
    def writeDataToTable(self):
        print "writing data"
        self.table.clear()
        dataLen = len(self.reactionTimeData)
        for a in range(dataLen):
            self.table.insert("end",(str(a+1),str(self.reactionTimeData[a])))
        self.table.see(dataLen-1)
    def clearData(self):
        self.reactionTimeData = []
        self.writeDataToTable()
    
    def clearLastData(self):
        self.reactionTimeData.pop()
        self.writeDataToTable()
    def processToClipBoard(self):
        string = ""
        for a in range(len(self.reactionTimeData)):
            string = string + str(self.reactionTimeData[a]) + "\n"
        clipboard.write_to_clipboard(string)
        print string
        
    def sortOfMainLoop(self): #fonction instaurée pour bypasser le mainloop pour que mon
        #code soit effectué à chaque fois que ce loop arrive.  
        
            
       
       
        while self.windowExist:
            if self.waitForStimulus==1:
                #print time.time()
            
                if time.time()>self.stimulusTime:
                    print "SWAG"
                    print time.time()
                    self.experimentButton.config(text = "APPUYEZ", fg = "green")
                    self.waitForStimulus = 0
                    self.waitForUser = 1
                    
                    
                    
            self.update()
        self.destroy()
        
    def on_closing(self):
        if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
            self.windowExist = 0 
      

        
if __name__ == "__main__":
    """
    appb = Tkinter.Tk()
    appb.parent = None
    appb.grid()
    """
    
    
    app = reactionTimeGUI(None)
    app.title("Votre temps de réaction")
    app.sortOfMainLoop()
   
    
    
    

    
    
        
        
        
        
