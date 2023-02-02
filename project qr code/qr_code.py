from tkinter import *
from tkinter.font import Font
import pyqrcode
import cv2 
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image,ImageTk

win=Tk()
win.config(bg="#D0E9F1")
win.geometry("540x140")
win.title("Qr Code Generator")
# win.iconbitmap("C:\\ravish\\photos\\icon2.ico")

font1=Font(family='impact',size=35,weight='normal',slant='roman',underline=0,overstrike=0)
font2=Font(family='impact',size=15,weight='normal',slant='roman',underline=0,overstrike=0)
font3=Font(family='impact',size=30,weight='normal',slant='roman',underline=0,overstrike=0)
font4=Font(family='impact',size=12,weight='normal',slant='roman',underline=0,overstrike=0)
font5=Font(family='impact',size=14,weight='normal',slant='roman',underline=0,overstrike=0)

Lab_qrcode=Label(win,text="QR CODE ",bg="#D0E9F1",fg="#095C27",font=font3,padx=25,pady=25).place(x=0,y=0)
Lab_generator=Label(win,text="GENERATOR",bg="#D0E9F1",fg="#2C5788",font=font3,padx=25,pady=0).place(x=0,y=78)
Lab_url= Label(win,text="URL :",bg="#D0E9F1",fg="#2C5788",font = font2,padx=25,pady=25).place(x=200,y=8)

enter1=Entry(win,width=37,borderwidth=3)
enter1.place(x=280,y=38)

def gener():
    s = enter1.get()
    path = filedialog.asksaveasfilename(title="Save QR Code",filetypes = (("png file",".png"),("jpg file",".jpg"),("jpeg file",".jpeg"),("all files","*.*")))
    if path == "":
        print(path)
        if path.endswith(".png") or path.endswith(".jpg") or path.endswith(".jpeg") :
            getqr = pyqrcode.create(s,)
            getqr.png(path,scale = 8) 
        else:
            path += ".png"
            getqr = pyqrcode.create(s,)
            getqr.png(path,scale = 6) 

        global getimg
        getimg = ImageTk.PhotoImage(Image.open(path))
        Lab_img = Label(win,image=getimg).place(x = 112,y = 148)
        win.geometry("540x500")
    url = pyqrcode.create(s)
    url.png('myqr.png', scale = 6)
    img = cv2.imread("C:\\sem4\\vs code\\myqr.png")
    cv2.imshow(s,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def clear():
    win.geometry("540x140")

But_exit=Button(win,text="EXIT",bg="#8EBFCF",fg="#2F5967",font=font4,padx=15,pady=0,borderwidth=3,command=win.destroy).place(x=440,y=85)
But_generate=Button(win,text="GENERATE",bg="#8EBFCF",fg="#2F5967",font=font4,padx=15,pady=0,borderwidth=3,command=gener).place(x=225,y=85)
But_Clear=Button(win,text="CLEAR",bg="#8EBFCF",fg="#2F5967",font=font4,padx=15,pady=0,borderwidth=3,command=clear).place(x=343,y=85)
win.mainloop()