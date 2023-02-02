from tkinter import *           #pip install tk
from tkinter.font import Font
from datetime import datetime
win = Tk()
win.config(bg="#D0E9F1")
win.geometry("440x165")
win.title("Log")
font1=Font(family='impact',size=35,weight='normal',slant='roman',underline=0,overstrike=0)
font4=Font(family='impact',size=12,weight='normal',slant='roman',underline=0,overstrike=0)
Lab_Logs=Label(win,text="Logs",bg="#D0E9F1",fg="#095C27",font=font1,padx=25,pady=25).place(x=0,y=0)
But_exit=Button(win,text="EXIT",bg="#8EBFCF",fg="#2F5967",font=font4,padx=15,pady=0,borderwidth=3,command=win.destroy).place(x=23,y=115)
enter1=Entry(win,width=45,borderwidth=3)
enter1.place(x=135,y=50)
def write():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    wrt = enter1.get()
    file = "C:/projectfiles/logs.txt" #file path of text file where you want to save the logs
    f_ob = open(file,'a+')
    f_ob.write(date_time)
    f_ob.write('\n')
    f_ob.write(wrt)
    f_ob.write('\n')
    f_ob.write('\n')
    f_ob.close()
    win.destroy()
But_write=Button(win,text="WRITE",bg="#8EBFCF",fg="#2F5967",font=font4,padx=15,pady=0,borderwidth=3,command=write).place(x=332,y=115)
win.mainloop()