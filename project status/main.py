from customtkinter import *
import os
win = CTk()
set_appearance_mode("system")
set_default_color_theme("blue")
win.title("")
# win.iconbitmap("C:/sem4/vs code/import files/icons/icon.ico")
win.geometry("570x300")

font1=CTkFont(family='impact',size=25,weight='normal',slant='roman',underline=0,overstrike=0)
font2=CTkFont(family='impact',size=15,weight='normal',slant='roman',underline=0,overstrike=0)

from psutil import sensors_battery as battery       #battery().percent
import screen_brightness_control as brightness      #brightness().get_brightness() / setbrihgtness()
#----------------------------------------------------------------------------------------

brt_frame = CTkFrame(win,width=150,height = 280,corner_radius=10,fg_color="#444444").place(x = 10,y = 10)

def bright(value):
    brightness.set_brightness(bright_slide.get())
    bright_entry.delete(0,END)
    bright_entry.insert(0,"     "+str(int(bright_slide.get()))+"%")

def incr():
    current = round(brightness.get_brightness()[0],-1)
    current = current + 10
    if current > 100:
        current = 100
    brightness.set_brightness(current)
    bright_slide.set((current))
    bright_entry.delete(0,END)
    bright_entry.insert(0,"     "+str(int(bright_slide.get()))+"%")
def decr():
    current = round(brightness.get_brightness()[0],-1)
    current = current - 10
    if current < 0:
        current = 0
    brightness.set_brightness(current)
    bright_slide.set(current)
    bright_entry.delete(0,END)
    bright_entry.insert(0,"     "+str(int(bright_slide.get()))+"%")


lab_bright = CTkLabel(brt_frame,text="Brightness",bg_color = "#444444",font=font1).place(x = 25,y = 25)
bright_slide = CTkSlider(brt_frame,width=20,orientation=VERTICAL,from_=0,to=100,height=200,bg_color="#666666",number_of_steps=100,command=bright)
bright_slide.place(x = 20,y = 80)
bright_slide.set(brightness.get_brightness()[0])
bright_entry = CTkEntry(brt_frame,width=80,font=font2)
bright_entry.place(x = 60,y = 80)
bright_entry.insert(0,"     "+str(int(bright_slide.get()))+"%")
bright_but = CTkButton(brt_frame,text="+",font=font1,width=80,command=incr).place(x = 60,y = 160)
bright_but = CTkButton(brt_frame,text="-",font=font1,width=80,command=decr).place(x = 60,y = 200)
#----------------------------------------------------------------------------------------

bat_frame = CTkFrame(win,width=180,height = 280,corner_radius=10,fg_color="#444444").place(x = 180,y = 10)

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

def update():
    bat_val1.delete(0,END)
    bat_val1.insert(0,str(battery().percent)+"%")
    bat_val3.delete(0,END)
    val = battery().power_plugged
    if val != 0:
        val = "yes"
        bat_val2.delete(0,END)
        bat_val2.insert(0,"charging")
    else:
        val = "no"
        bat_val2.delete(0,END)
        bat_val2.insert(0,convertTime(battery().secsleft))
    bat_val3.insert(0,val)
    bat_val.configure(state = ACTIVE)
    bat_val.set(battery().percent)
    bat_val.configure(state = DISABLED)

lab_battery = CTkLabel(bat_frame,text="Battery",bg_color="#444444",font=font1).place(x = 230,y = 25)
bat_lab1 = CTkLabel(bat_frame,text="Percentage",bg_color = "#444444",font=font2).place(x = 190,y = 70)
bat_lab2 = CTkLabel(bat_frame,text="Time Left",bg_color = "#444444",font=font2).place(x = 190,y = 100)
bat_lab3 = CTkLabel(bat_frame,text="Is Plugged",bg_color = "#444444",font=font2).place(x = 190,y = 130)
bat_val1 = CTkEntry(bat_frame,width=80,font=font2)
bat_val1.place(x = 270,y = 70)
bat_val2 = CTkEntry(bat_frame,width=80,font=font2)
bat_val2.place(x = 270,y = 100)
bat_val3 = CTkEntry(bat_frame,width=80,font=font2)
bat_val3.place(x = 270,y = 130)
bat_val = CTkSlider(bat_frame,width=150,height=20,from_=0,to=100,bg_color = "#666666",orientation="HORIZONTAL")
bat_val.place(x = 200,y = 200)
bat_val.set(battery().percent)
bat_val.configure(state = DISABLED)
but = CTkButton(bat_frame,text="Refresh",font=font2,command= update).place(x = 200,y = 250)
update()
#----------------------------------------------------------------------------------------
snd_frame = CTkFrame(win,width=180,height = 130,corner_radius=10,fg_color="#444444").place(x = 380,y = 10)

def opener_snd():
    os.startfile("C:\Windows\System32\SndVol.exe")

lab_sound = CTkLabel(snd_frame,text="Sound",bg_color="#444444",font=font1).place(x = 435,y = 25)
but_snd = CTkButton(snd_frame,text="Sound Control",font=font2,command=opener_snd).place(x = 400,y = 75)
#----------------------------------------------------------------------------------------
mor_frame = CTkFrame(win,width=180,height = 130,corner_radius=10,fg_color="#444444").place(x = 380,y = 160)

def opener_mor():
    os.startfile("C:\Windows\System32\mblctr.exe")

lab_mor = CTkLabel(mor_frame,text="More",bg_color="#444444",font=font1).place(x = 435,y = 175)
but_mor = CTkButton(mor_frame,text="More Control",font=font2,command=opener_mor).place(x = 400,y = 225)
#---------------------------------------------------------------------------------------------------------------------
mor_frame = 19

win.mainloop()