import tkinter as tk
from tkinter  import *
from tkinter import messagebox
from PIL import ImageTk, Image
root= Tk()
root .geometry("600x600")
#root.resizable(False,False)
root.title("SPEECH TO TEXT")
root.configure(background="white")
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
input_duration=Entry(root,width=17,font="arial 30 bold ",bg="blue",fg="white", textvariable=duration)
input_duration.place(x=160,y=340)
label_3=Label(text =" Please Enter time in seeconds",font="arial 15  ",bg="white",fg="gold" )
label_3.place(x=145,y=340)
#button record compound=LEFT,width=180,activebackground='Gold',bd=10,
button_icon1=PhotoImage(file="C:/Users/lenovo/Downloads/Tp1/python_test1/python_test2/i5.png")
root.iconphoto(False,button_icon1)

record= Button(root,font="arial 15",width=10,text="Record ", bg="#111111",fg="white",image=button_icon1, bd=5,activebackground="gold")
record.place(x=480,y=340)


root.mainloop()