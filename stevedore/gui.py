"""
IBM Containerized Forecasting Workflow

DESCRIPTION

    This is a GUI for the IBM Containerized Forecasting Workflow
    See https://docs.python.org/2.7/library/tkinter.html#tkinter-modules for Tkinter module list
"""
import sys
import argparse
from datetime import datetime, timedelta as td
import stevedore
import Tkinter as tk
import tkFont
import ScrolledText as st 


def gui():
    
    #Stevedore arguments
    start="2017-08-12"
    end="2017-08-12"
    length=6
    lat=29.434
    long=-98.499

    #Options
    ngridew=100
    ngridns=100
    nvertlevels=40
    ndomains=3
    gridratio=3
    gridspacinginner=1.5
    timestep=10
    wpsmapproj='lambert'
    sitefile=None
    tslistfile=None
    ncores=2
    history_interval=[60]
    phys_mp=17
    phys_ralw=4
    phys_rasw=4
    phys_cu=0
    phys_pbl=1
    phys_sfcc=1
    phys_sfc=2
    phys_urb=0
    runshort=0
    auxhist7=False
    auxhist2=False
    feedback=False
    adaptivets=False
    nopreprocess=False
    projectdir="undefined"
    norunwrf=False
    is_analysis=False
    altftpserver=None
    initialConditions=['GFS']
    boundaryConditions=['GFS']
    inputData=[]

    # create date objects
    hour_start = 0
    #get the start date expecting it to be in the format YYYY-MM-DD
    date_start = datetime.strptime(str(start)+':'+str(hour_start),
                                '%Y-%m-%d:%H')
    #get the end date expecting it to be in the format YYYY-MM-DD
    date_end = datetime.strptime(end+':'+str(hour_start),
                                '%Y-%m-%d:%H')
    #calculate the difference between the two dates.
    date_delta = date_end - date_start
    forecast_length = int(length)

    #Note print off what is going on to aid in debugging
    print "Running "+ str(date_delta.days+1) +" individual simulation each being "\
    +str(forecast_length) +" hours in length. UTC start is "+ str(hour_start)

    # loop over days to create forecasts
    for i in range(date_delta.days + 1):

        # current date of loop
        date_i = date_start + td(days=i)

        stevedore_instance = stevedore.Stevedore(date_i,
                                    forecast_length, lat, long,
                                    ncores=int(ncores),
                                    ndomains=int(ndomains),
                                    timestep=int(timestep),
                                    gridratio=int(gridratio),
                                    gridspacinginner=float(gridspacinginner),
                                    ngridew=ngridew,
                                    ngridns=ngridns,
                                    nvertlevels=int(nvertlevels),
                                    phys_mp=int(phys_mp),
                                    phys_ralw=int(phys_ralw),
                                    phys_rasw=int(phys_rasw),
                                    phys_cu=phys_cu,
                                    phys_pbl=int(phys_pbl),
                                    phys_sfcc=int(phys_sfcc),
                                    phys_sfc=int(phys_sfc),
                                    phys_urb=int(phys_urb),
                                    wps_map_proj=wpsmapproj,
                                    runshort=int(runshort),
                                    auxhist7=auxhist7,
                                    auxhist2=auxhist2,
                                    feedback=feedback,
                                    adaptivets=adaptivets,
                                    projectdir=projectdir,
                                    norunwrf=norunwrf,
                                    is_analysis=is_analysis,
                                    altftpserver=altftpserver,
                                    initialConditions=initialConditions,
                                    boundaryConditions=boundaryConditions,
                                    inputData=inputData,
                                    tsfile=tslistfile,
                                    history_interval=history_interval)
    class App:
        
            
        def __init__(self, root):
            #setting title
            root.title("undefined")
            #setting window size
            width=800
            height=500
            screenwidth = root.winfo_screenwidth()
            screenheight = root.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            root.geometry(alignstr)
            root.resizable(width=False, height=False)

            Button_start=tk.Button(root)
            Button_start["bg"] = "#efefef"
            ft = tkFont.Font(family='Times',size=10)
            Button_start["font"] = ft
            Button_start["fg"] = "#000000"
            Button_start["justify"] = "center"
            Button_start["text"] = "Start WRF"
            Button_start.place(x=700,y=450,width=70,height=25)
            Button_start["command"] = self.Button_start_command

            # Creating scrolled text area 
            # widget with Read only by 
            # disabling the state 
            text_area = st.ScrolledText(root, 
                                        width = width,  
                                        height = 10,  
                                        font = ("Times New Roman", 
                                                10)) 
            
            text_area.grid(column = 0, pady = 10, padx = 0) 
            
            # Inserting Text which is read only 
            text_area.insert(tk.INSERT, "This is where I want the WRF output ") 
            
            # Making the text read only 
            text_area.configure(state ='disabled')

        def Button_start_command(self):
            stevedore_instance.execute_ncview("/opt/deepthunder/data","test.nc")

    
    root = tk.Tk()
    app = App(root)
    root.mainloop()