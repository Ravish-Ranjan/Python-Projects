from random import shuffle
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from tkinter import *
from tkinter import messagebox as msg
import ttkbootstrap as tkb
from time import sleep

win = tkb.Window(themename="superhero")
win.title("Sorting Visualizer Config")
win.geometry("400x150")

input_size = 0

count = 0
def bubble_sort(a):
    global X,Y,input_size,count
    if count < input_size-1:
        for j in range(input_size-count-1):
            if Y[j]>Y[j+1]:
                Y[j],Y[j+1] = Y[j+1],Y[j]
        axl.clear()
        axl.bar(X,Y)
        count += 1
    else:
        sleep(2)
        shuffle(Y)
        plt.close()
        win.destroy()
count = 1
def insertion_sort(i):
    global X,Y,input_size,count
    if count < input_size:
        key = Y[count]
        j = count-1
        while j >= 0 and key < Y[j] :
                Y[j + 1] = Y[j]
                j -= 1
        Y[j + 1] = key
        axl.clear()
        axl.bar(X,Y)
        count +=1
    else:
        sleep(2)
        shuffle(Y)
        plt.close()
        win.destroy()

count = 0
def selection_sort(i):
    global X,Y,input_size,count
    if count < input_size-1:
        min = count
        for j in range(count+1,input_size):
            if Y[min] > Y[j]:
                min = j
        if min!=count:
            Y[count],Y[min] = Y[min],Y[count]
        axl.clear()
        axl.bar(X,Y)
        count += 1
    else:
        sleep(2)
        shuffle(Y)
        plt.close()
        win.destroy()
  

algos = {
    "Bubble Sort" : bubble_sort,
    "Insertion Sort" : insertion_sort,
    "Selection Sort" : selection_sort,
}

speeds = {
    "slow":500,
    "medium":300,
    "fast":100
}

sorting_algo_opt = [
    "--select-algo--",
    "Bubble Sort",
    "Insertion Sort",
    "Selection Sort",
]

speed_opt = [
    "--select-speed--",
    "slow",
    "medium",
    "fast",
]

def start():
    global X,Y,input_size,fig,axl
    algo = algo_str_var.get()
    spd = speed_str_var.get()
    input_size = inpsz.get()
    if ("--select-spped--" == spd) or ("--select-algo--" == algo) or (input_size == ""):
        msg.showerror(title="Input Error",message="Some inputs are missing.\nPlease fill them up.")
    else:
        algo = algos[algo]
        spd = speeds[spd]
        input_size = int(input_size)

        X = [x for x in range(1,input_size+1)]
        Y = [x for x in range(1,input_size+1)]
        shuffle(Y)

        fig = plt.figure()
        axl = fig.add_subplot(1,1,1)
        axl.bar(X,Y)
        ani = anim.FuncAnimation(fig,algo,interval = spd)
        plt.show()

lab_input = tkb.Label(win,text="Input Size : ",bootstyle = "default")
lab_input.place(x = 20,y = 22)

inpsz = tkb.Entry(win,width=30)
inpsz.place(x = 120,y = 20)

algo_str_var = StringVar()
algo_str_var.set("--select-algo--")

speed_str_var = StringVar()
speed_str_var.set("--select-speed--")

drop_speed = tkb.OptionMenu(win,speed_str_var,*speed_opt,bootstyle = "info,outline")
drop_speed.place(x = 20,y = 60)
drop_speed.config(width = 21)

drop_algo = tkb.OptionMenu(win,algo_str_var,*sorting_algo_opt,bootstyle = "info,outline")
drop_algo.place(x = 210,y = 60)
drop_algo.config(width = 21)

play = tkb.Button(win,text="Play",width=25,bootstyle = "success,outline",command=start).place(x = 20,y = 100)
exit = tkb.Button(win,text="Exit",width=25,bootstyle = "danger,outline",command=win.destroy).place(x = 210,y = 100)
     
win.mainloop()