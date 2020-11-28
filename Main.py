#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 23:20:08 2020

@author: piyush
"""








class mainWindow():
    def __init__(self,root,heightMain,widthMain):
        root.geometry(""+str(widthMain)+"x"+str(heightMain))
        root.title("Activities logger")
        cnvsStruct = Canvas(root)
        cnvsStruct.place(x=0,y=0,width=widthMain,height=heightMain)

        #Placeholder for showing top 4 suggested categories by machine learning algorithm
        cnvsStruct.create_rectangle(((widthMain*80)/100),0,widthMain,(heightMain/4),fill="#003d66",outline="")
        cnvsStruct.create_rectangle(((widthMain*80)/100),(heightMain/4),widthMain,(heightMain/2),fill="#0099ff",outline="")
        cnvsStruct.create_rectangle(((widthMain*80)/100),(heightMain/2),widthMain,((heightMain*75)/100),fill="#80ccff",outline="")
        cnvsStruct.create_rectangle(((widthMain*80)/100),((heightMain*75)/100),widthMain,heightMain,fill="#e6f5ff",outline="")
        cnvsStruct.create_rectangle(0,((heightMain*60)/100),((widthMain*80)/100),heightMain,fill="#bfbfbf",outline="")

        strVar = StringVar()
        strVar.set("Hours")

        #Entry widget for hours and minutes
        inHrs = Entry(root,bg="#e6ecff",font=("Times",50))
        inHrs.place(x=5,y=30,width=80,height=50)

        lblSep = Label(root,text=":",font=("Times",30))
        lblSep.place(x=100,y=40,width=15,height=25)

        inMns = Entry(root,bg="#e6ecff",font=("Times",50))
        inMns.place(x=125,y=30,width=100,height=50)

        #Label widget for hours and minutes
        lblHrs = Label(root,text="Hours",font=("Times",20,"bold"))
        lblHrs.place(x=15,y=10,height=20)

        lblMns = Label(root,text="Minutes",font=("Times",20,"bold"))
        lblMns.place(x=130,y=10,height=20)

        #Entry widget for Title/Summary
        inTitle = Entry(root,bg="#e6ecff",font=("Times",25))
        inTitle.place(x=5,y=100,width=500,height=40)

        lblTitle = Label(root,text="Title/Summary",font=("Times",18,"bold"))
        lblTitle.place(x=15,y=82,height=20)


from tkinter import *

root = Tk()


#Height and Width of main window
heightMain=600
widthMain=800

mainWindow(root,heightMain,widthMain)

root.mainloop()


 
