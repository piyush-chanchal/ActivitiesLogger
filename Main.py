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



        #Entry widget for hours and minutes
        self.inHrs = Entry(root,bg="#f2f2f2",font=("Times",50))
        self.inHrs.place(x=5,y=30,width=80,height=50)

        lblSep = Label(root,text=":",font=("Times",30))
        lblSep.place(x=100,y=40,width=15,height=25)

        self.inMns = Entry(root,bg="#f2f2f2",font=("Times",50))
        self.inMns.place(x=125,y=30,width=100,height=50)

        #Label widget for hours and minutes
        lblHrs = Label(root,text="Hours",font=("Times",20,"bold"))
        lblHrs.place(x=15,y=10,height=20)

        lblMns = Label(root,text="Minutes",font=("Times",20,"bold"))
        lblMns.place(x=130,y=10,height=20)


        #Entry and label widget for Title/Summary
        self.inTitle = Entry(root,bg="#f2f2f2",font=("Times",25))
        self.inTitle.place(x=5,y=111,width=500,height=40)

        lblTitle = Label(root,text="Summary",font=("Times",18,"bold"))
        lblTitle.place(x=15,y=92,height=20)


        #Label and Entry widget of Description
        lblDesc = Label(root,text="Detail",font=("Times",18,"bold"))
        lblDesc.place(x=15,y=165,height=20)

        self.inDesc = Text(root,bg="#f2f2f2",font=("Times",20))
        self.inDesc.place(x=5,y=185,height=165,width=350)

        #Submit button widget
        #bg option not working in mac so used highlightbackground instead
        self.btnSubmit = Button(root,highlightbackground="gray",text="Submit",font=("Times",50,"bold"), command = self.submitButAction)
        self.btnSubmit.place(x=370,y=180,height=178,width=268)

        #Date and Time label widget
        lblHeader = Label(root,text="Activity done at:\n",fg="#000000",font=("Times",15,"bold"))
        lblHeader.place(x=240,y=0)

        
        self.lblDateTime = Label(root,font=("Times",18))
        self.lblDateTime.place(x=240,y=20) 
        
        #rendering time dynamically
        self.time()

        btnDateChange = Button(root,text="Change",highlightbackground="#e6e6e6",font=("Times",12,"bold"),command=self.changeButAction)
        btnDateChange.place(x=310,y=40,height=20)

        
        #rendering main category drop down list
        self.mainCatList = ttk.Combobox(root,font=("Times",18))
        self.mainCatList.place(x=400,y=10,width=230)
        self.mainCatList['values'] = ('*Select Main Category','Cat2','Cat3')
        self.mainCatList.current(0)

        #rendering sub category level 1
        self.sub1CatList = ttk.Combobox(root)
        self.sub1CatList.place(x=420,y=50)
        self.sub1CatList['values'] = ('Select Sub Category 1','Cat2','Cat3')
        self.sub1CatList.current(0)

        #rendering sub category level 2
        self.sub2CatList = ttk.Combobox(root)
        self.sub2CatList.place(x=420,y=80)
        self.sub2CatList['values'] = ('Select Sub Category 2','Cat2','Cat3')
        self.sub2CatList.current(0)




    
    def time(self):
        self.dateTimeNow = datetime.now()
        self.strDateTime = str(self.dateTimeNow.strftime("%x"))+"\n"+str(self.dateTimeNow.strftime("%X"))
        self.lblDateTime.config(text=self.strDateTime)
        self.lblDateTime.after(1000,self.time)

    def changeButAction(self):
        print("Change button has been pressed")


    def submitButAction(self):
        print("Submit button has been pressed")
        self.strYYYYMMDD = str(self.dateTimeNow.strftime("%Y"))+str(self.dateTimeNow.strftime("%m"))+str(self.dateTimeNow.strftime("%d"))
        print(self.strYYYYMMDD)

        self.sNum=1


        ##Retrieving all fields data and saving into variables. Then writing it into csv files
        self.hours=str(self.inHrs.get())
        self.minutes=str(self.inMns.get())
        self.totalMinutes=(int(self.hours)*60)+int(self.minutes)
        self.actDoneOn=str(self.lblDateTime.cget("text")[0:self.lblDateTime.cget("text").find("\n")])
        self.actDoneAt=str(self.lblDateTime.cget("text")[self.lblDateTime.cget("text").find("\n")+1:])
        self.actLoggedOn=str(self.dateTimeNow.strftime("%x"))
        self.actLoggedAt=str(self.dateTimeNow.strftime("%X"))
        self.lblDispDateTime = self.lblDateTime["text"]
        self.lblDispTimeHrs=int(self.lblDispDateTime[int(self.lblDispDateTime.find("\n")+1):self.lblDispDateTime.find(":")])
        self.lblDispTimeMins=int(self.lblDispDateTime[self.lblDispDateTime.find(":")+1:self.lblDispDateTime.rfind(":")])
        self.lblDispTimeSec=int(self.lblDispDateTime[self.lblDispDateTime.rfind(":")+1:])
        self.ActivityDoneTimeNumeric=self.lblDispTimeHrs + (self.lblDispTimeMins/60) + (self.lblDispTimeSec/(60*60))
        self.catValue=self.mainCatList.get()
        self.subcat1Value=self.sub1CatList.get()
        self.subcat2Value=self.sub2CatList.get()
        self.titleText=self.inTitle.get()
        self.desText=self.inDesc.get("1.0","end-1c")
        self.csvWrite()



    def csvWrite(self):
        with open(self.strYYYYMMDD + ".csv", 'w', newline='') as csvfile:
            inData = csv.writer(csvfile)
            inData.writerow(['S. No.', 'hours', 'Minutes', 'TotalMinutes','Activity done on(date)', 'Activity done at(time)','ActivityDoneTimeNumeric','Activity logged on(date)', 'Activity logged at(time)','Category','Sub Category 1','Sub Category 2','Title','Description'])
            inData.writerow([self.sNum,self.hours, self.minutes, self.totalMinutes,self.actDoneOn,self.actDoneAt,self.actLoggedOn,self.actLoggedAt,self.ActivityDoneTimeNumeric,self.catValue,self.subcat1Value,self.subcat2Value,self.titleText,self.desText])


from tkinter import *
from datetime import datetime
from tkinter import ttk
import csv

root = Tk()


#Height and Width of main window
heightMain=600
widthMain=800

mainWindow(root,heightMain,widthMain)

root.mainloop()


 
