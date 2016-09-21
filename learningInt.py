#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
version = "1.0"

import Tkinter, time 

class simpleapp_tk(Tkinter.Tk): #simpleapp_tk is a subclass from Tkinter.Tk
    def __init__(self,parent): 
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize() # An itialize function have been defined to generate all the widgets
        self.clicked  = 0  
    def initialize(self):
        
        self.resizable(True,False) # horiz vert. 
        
        self.grid() #Protocol to align every widgets. 
        self.grid_columnconfigure(0,weight=1)
        
        
        
        ## Creation of the entry widget 
        self.entryVariable = Tkinter.StringVar() #Special variable for managing sting in widget
        self.entry = Tkinter.Entry(self,textvariable = self.entryVariable) #Linking the text of entry to self.entryVariable
        self.entry.grid(column=0,row=0,sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set("Enter your textô here")
        
        button = Tkinter.Button(self,text=u"Click me !",command = self.OnButtonClick)
        
        
        
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable = self.labelVariable)
                              #anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

        self.TextZone = Tkinter.Text(self,height = 2, width = 30)
       
        self.TextZone.insert(Tkinter.END,"pinis")
        self.TextZone.grid(column =0,row =2,sticky = 'EW')
        self.TextZone.config(state = Tkinter.DISABLED)
        
    def OnButtonClick(self):
        if self.clicked == 1:
            elapsed_time = time.time()-self.start_time
            print elapsed_time
            self.clicked = 0
            self.labelVariable.set("click the button again")
        elif self.clicked == 0: 
            print "You clicked the button...wait"
            self.labelVariable.set("You clicked the button...wait")
            self.update()
            #self.entry.focus_set()
            self.entry.selection_range(0, Tkinter.END)
            time.sleep(2)
            self.labelVariable.set("PRESS ENTER")
            self.start_time = time.time()
            self.update()
            self.clicked = 1
        #raw_input("")
        
        
        
        

            
    def OnPressEnter(self,event):
            print "You pressed enter"
            print event
            
            self.labelVariable.set(self.entryVariable.get() + "pinis the enter")
            self.entry.focus_set()
            self.entry.selection_range(0, Tkinter.END)
            #self.OnButtonClick()
            #self.OnButtonClick()
            if self.clicked == 1:
                elapsed_time = time.time()-self.start_time
                print elapsed_time
                self.clicked = 0
                self.labelVariable.set("click the button again")
            elif self.clicked == 0: 
                print "You clicked the button...wait"
                self.labelVariable.set("You clicked the button...wait")
                self.update()
            #self.entry.focus_set()
                self.entry.selection_range(0, Tkinter.END)
                time.sleep(2)
                self.labelVariable.set("PRESS ENTER")
                self.start_time = time.time()
                self.update()
                self.clicked = 1    
            
def sortOfMainLoop(parent):
    while 1:
        parent.update()
    
        


if __name__ == "__main__":
    app = simpleapp_tk(None) #Initialization of an object of the class simpleapp_tk
                            #without parent. 
    app.title('gdis v'+version) 
    #app.mainloop()
    sor
    
    