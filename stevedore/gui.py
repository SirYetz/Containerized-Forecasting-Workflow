"""
IBM Containerized Forecasting Workflow

DESCRIPTION

    This is a GUI for the IBM Containerized Forecasting Workflow
    See https://docs.python.org/2.7/library/tkinter.html#tkinter-modules for Tkinter module list
"""

import Tkinter as tk
import tkFont
import ScrolledText as st 


def gui():
    
    class App:
        a=5
            
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
            #Just a test of changing variables
            print("command")
            self.a=self.a+1
            print(self.a)
    
    root = tk.Tk()
    app = App(root)
    root.mainloop()