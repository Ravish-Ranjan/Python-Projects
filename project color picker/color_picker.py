from tkinter import *
from tkinter import colorchooser

def opener():
    color_code = colorchooser.askcolor(title ="Choose color")
    clip = Tk() 
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(color_code)
    clip.destroy()

win = Tk()
win.title("Color Picker")
win.geometry("550x350")
win.config(bg="#D0E9F1")
# win.iconbitmap("C:\\sem4\\vs code\\import files\\color-logo.ico")
font1 = "system",15
font2 = "impact",12
font3 = "impact",27
font4 = "impact",25

def rgb_to_hex(r,g,b):
    return "{:02x}{:02x}{:02x}".format(r,g,b)

def rgb_to_pms(r,g,b):
    print()
def rgb_to_cmyk(r, g, b):
    if (r, g, b) == (0, 0, 0):
        return 0, 0, 0, 100
    c = 1 - r / 255
    m = 1 - g / 255
    y = 1 - b / 255
    min_cmy = min(c, m, y)
    c = int((((c - min_cmy) / (1 - min_cmy))*100)//1)
    m = int((((m - min_cmy) / (1 - min_cmy))*100)//1)
    y = int((((y - min_cmy) / (1 - min_cmy))*100)//1)
    k = int(((min_cmy)*100)//1)
    return "("+str(c)+"%,"+str(m)+"%,"+str(y)+"%,"+str(k)+"%)"

def slider(value):
    r = red_scale.get()
    g = green_scale.get()
    b = blue_scale.get()

    rgb_entry_cmyk.delete(0,END)
    rgb_entry_cmyk.insert(0,(rgb_to_cmyk(r,g,b)))

    rgb_entry_rgb.delete(0,END)
    rgb_entry_rgb.insert(0,("RGB("+str(r)+","+str(g)+","+str(b)+")"))

    rgb = rgb_to_hex(r,g,b).upper()
    dis_code = "#%02x%02x%02x"%(r,g,b)
    colorlabel.config(bg = dis_code)

    rgb_entry_hex.delete(0,END)
    rgb_entry_hex.insert(0,"#"+rgb)

    

def onClick1():
    clip = Tk() 
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(rgb_entry_hex.get())
    clip.destroy()

def onClick2():
    r = red_scale.get()
    g = green_scale.get()
    b = blue_scale.get()
    clip = Tk() 
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append("RGB("+str(r)+","+str(g)+","+str(b)+")")
    clip.destroy()


def onClick4():
    clip = Tk() 
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(rgb_entry_cmyk.get())
    clip.destroy()

Lab_Logs1=Label(win,text="COLOR",bg="#D0E9F1",fg="#095C27",font=font3).place(x=40,y=20)
Lab_Logs2=Label(win,text="PICKER",bg="#D0E9F1",fg="#008A9C",font=font4).place(x=40,y=60)

fixlabel = Label(win,bg = "#2C5788",width = 19,height=5,pady = 8,bd = 1)
fixlabel.place(x = 27,y = 117)

colorlabel = Label(win,bg = "black",width = 18,height=5,pady = 5,bd = 1)
colorlabel.place(x = 30,y = 120)

red_label = Label(win,text = "Red" , fg = "red" ,bg="#D0E9F1",font = (font1))
red_label.place(x = 190 , y = 33)

red_scale = Scale(win,from_=0,to = 255,fg = "red",length=256,bg="#D0E9F1",orient=HORIZONTAL,command = slider)
red_scale.place(x = 240 , y = 20)

green_label = Label(win,text = "Green" , fg = "green" ,bg="#D0E9F1",font = (font1))
green_label.place(x = 190 , y = 73)

green_scale = Scale(win,from_=0,to = 255,fg = "green",length=256,bg="#D0E9F1",orient=HORIZONTAL,command = slider)
green_scale.place(x = 240 , y = 70)

blue_label = Label(win,text = "Blue" , fg = "blue" ,bg="#D0E9F1",font = (font1))
blue_label.place(x = 190 , y = 123)

blue_scale = Scale(win,from_=0,to = 255,fg = "blue",length=256,bg="#D0E9F1",orient=HORIZONTAL,command = slider)
blue_scale.place(x = 240 , y = 120)

rgb_label_hex = Label(win,text = "HEX CODE",fg = "#095C27",bg="#D0E9F1",font = (font2))
rgb_label_hex.place(x = 172 , y = 177)
rgb_entry_hex = Entry(win,width = 17,borderwidth=3,font = (font1))
rgb_entry_hex.place(x = 252 , y = 180)

rgb_label_rgb = Label(win,text = "RGB CODE",fg = "#095C27",bg="#D0E9F1",font = (font2))
rgb_label_rgb.place(x = 172 , y = 217)
rgb_entry_rgb = Entry(win,width = 17,borderwidth=3,font = (font1))
rgb_entry_rgb.place(x = 252 , y = 220)

rgb_label_cmyk = Label(win,text = "CMYK CODE",fg = "#095C27",bg="#D0E9F1",font = (font2))
rgb_label_cmyk.place(x = 172 , y = 257)
rgb_entry_cmyk = Entry(win,width = 17,borderwidth=3,font = (font1))
rgb_entry_cmyk.place(x = 252 , y = 260)

rgb_entry_hex.insert(END,'#000000')
rgb_entry_rgb.insert(END,'RGB(0,0,0)')
rgb_entry_cmyk.insert(END,'(0%,0%,0%,100%)')

copy1 = Button(win,text = "COPY HEX" ,bg = "#A9C1C9",font = (font2),padx =17,command = onClick1)
copy1.place(x = 420 , y = 175)

copy2 = Button(win,text = "COPY RGB" ,bg = "#A9C1C9",font = (font2),padx =15,command = onClick2)
copy2.place(x = 420 , y = 215)

copy3 = Button(win,text = "COPY CMYK",bg = "#A9C1C9",font = (font2),padx =10,command = onClick4)
copy3.place(x = 420 , y = 255)

but_picker = Button(win,text = "Color Wheel",bg = "#A9C1C9",font = (font2),padx =10,command = opener)
but_picker.place(x = 27 , y = 295)

exit = Button(win,text = "EXIT",bg = "#A9C1C9",font = (font2),padx =19,command = win.destroy)
exit.place(x = 27 , y = 255)

win.mainloop()