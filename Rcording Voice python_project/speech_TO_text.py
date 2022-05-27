import tkinter as tk
from tkinter  import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sounddevice as sound
from scipy.io.wavfile import write
import time
import random
import wavio as wv
from playsound import playsound
#pip3 install sounddevice
#pip3 install scipy
#pip3 install wavio
root= Tk()
root .geometry("660x600")
#root.resizable(False,False)
root.title("SPEECH TO TEXT")
root.configure(background="white")

#function

def play():   
    playsound('record.wav')

def blind():
    color=['pink','yellow','red','blue','green']
    #import random
    Animation=random.choice(color)
    label_a.configure(bg=Animation)
    label_a.after(200,blind)

def record():
     freq=44100
     durat=int(duration.get() )
     recording =sound.rec(durat* freq,samplerate=freq,channels=2)
     #use Timer
     try:
         tim=int(duration.get())
     except:
             print("value not valide !!\n try agin ")
     while tim >0:
         root.update()
         time.sleep(1)
         tim=tim-1
         if(tim==0):
            messagebox.showinfo("Timing countdown","Up Timing")
         Label(root,text=f"{str(tim)}",font="arial 30",width=3,bg="gold",fg="black").place(x=250,y=480)
     sound.wait()
     write("record.wav",freq,recording)
label_a=Label(root,text="Playing and Recording Sound in Python",font='arial 15')
label_a.place(x=0,y=0,relwidth=1)
image_icon=PhotoImage(file="C:/Users/lenovo/Downloads/Tp1/python_test1/python_test2/home.png")
root.iconphoto(False,image_icon)
#create icon
# Create a photoimage object of the image in the path
path3="C:/Users/lenovo/Downloads/Tp1/python_test1/python_test2/i3.png"
img1 = ImageTk.PhotoImage(Image.open(path3))
lebel_1=Label(root,bd=0,image=img1)
lebel_1.place(x=170,y=90)

#name_text 
label_2=Label(text ="Recorder voice",font="arial 30 bold ",bg="white",fg="gold" )
label_2.place(x=140,y=30)
#box entry number second
duration =StringVar()
duration.set("")
input_duration=Entry(root,width=17, font="arial 20 bold ",bg="blue",fg="white", textvariable=duration)
input_duration.place(x=160,y=340)
label_3=Label(text =" Please Enter time in seeconds",font="arial 15  ",bg="white",fg="gold" )
label_3.place(x=145,y=380)
#button record compound=LEFT,width=180,activebackground='Gold',bd=10,
button_icon1=PhotoImage(file="C:/Users/lenovo/Downloads/Tp1/python_test1/python_test2/i5.png")
root.iconphoto(False,button_icon1)

record= Button(root,font="arial 20",compound=LEFT,width=180,text="Recording", bg="#111111",fg="white",image=button_icon1, bd=5,activebackground="gold",command=record)
record.place(x=460,y=340)

button_icon2=PhotoImage(file="C:/Users/lenovo/Downloads/Tp1/python_test1/python_test2/i10.png")
root.iconphoto(False,button_icon2)

play= Button(root,font="arial 20",compound=LEFT,width=180,text="Play", bg="#111111",fg="white",image=button_icon2, bd=5,activebackground="gold",command=play)
play.place(x=460,y=440)
blind()
root.mainloop()

