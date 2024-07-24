import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from PIL import Image, ImageTk

root = Tk()
root.title("Text to Speech generator")
root.geometry("900x450+200+200")
root.resizable(False, False)
root.configure(bg="#305065")

engine=pyttsx3.init()
def speaknow():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if (text):
        if (speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',50)
            setvoice()
            
def download():
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed=speed_combobox.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
    if (text):
        if (speed=="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif (speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',50)
            setvoice()


            
try:
    image = Image.open("speak.jpg")
    image = image.resize((50, 50), Image.LANCZOS)  
    image_icon = ImageTk.PhotoImage(image)
    root.iconphoto(False, image_icon)
except Exception as e:
    print(f"Error loading image: {e}")

Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)

try:
    logo_image = Image.open("speaker logo.JPG")
    logo_image = logo_image.resize((80, 80), Image.LANCZOS) 
    Logo = ImageTk.PhotoImage(logo_image)
    label = Label(Top_frame, image=Logo, bg="white")
    label.place(x=10, y=5)
    label.image = Logo  
except Exception as e:
    print(f"Error loading logo image: {e}")

Label(Top_frame,text="TEXT TO SPEECH GENRATOR",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)


text_area=Text(root,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=400,height=250)

Label(root,text="VOICE",font='arial 15 bold',bg='#305065',fg='white').place(x=460,y=160)
Label(root,text="SPEED",font='arial 15 bold',bg='#305065',fg='white').place(x=640,y=160)

gender_combobox=Combobox(root,values=['Male','Female'],font='arial 14',state='r',width=10)
gender_combobox.place(x=450,y=200)
gender_combobox.set('Female')

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font='arial 14',state='r',width=10)
speed_combobox.place(x=630,y=200)
speed_combobox.set('Normal')

try:
    image = Image.open("speak.jpg")
    image = image.resize((50, 50), Image.LANCZOS)
    imageicon = ImageTk.PhotoImage(image)
    btn1 = Button(root, text='Speak', compound=LEFT, image=imageicon, width=130, font="arial 14 bold",command=speaknow)
    btn1.place(x=450, y=280)
except Exception as e:
    print(f"Error loading speak.jpg image: {e}")


try:
    image2 = Image.open("download.png")
    image2 = image2.resize((50, 50), Image.LANCZOS)
    imageicon2 = ImageTk.PhotoImage(image2)
    btn2 = Button(root, text='Save', compound=LEFT, image=imageicon2, bg="#39c790", width=130, font="arial 14 bold", command=download)
    btn2.place(x=630, y=280)
except Exception as e:
    print(f"Error loading download.png image: {e}")

root.mainloop()

