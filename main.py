"""

Author : Shabari K S
Created as Mini Project
Download Link available in the README.md file
if you need any help email to this mail address --> "2k21cse137@kiot.ac.in"


"""


from tkinter import *
from tkinter import ttk,messagebox
import customtkinter
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import os
import sys
import platform
from PySide2 import QtCore, QtGui,QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_splash_screen import Ui_splachscreen

counter = 0



PATH = os.path.dirname(os.path.realpath(__file__))

def MainWindow():
    def load_image(path, image_size):
        return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))

    def get_weather():
        try:
            city = entry.get()

            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.geocode(city)
            obj = TimezoneFinder()

            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

            tz.configure(text=result)

            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")

            clock.configure(text=current_time)


            base_url = "http://api.openweathermap.org/data/2.5/onecall?lat="
            complete_url = base_url + str(location.latitude) + "&lon=" + str(location.longitude) + "&exclude=hourly&unit=metric&appid=" + '9e2a7ecedfd1f757ed0dfd409f8d1c5a'
            response = requests.get(complete_url)
            x = response.json()
            temp = x['current']['temp']
            humidity = x['current']['humidity']
            pressure = x['current']['pressure']
            wind = x['current']['wind_speed']
            description = x['current']['weather'][0]['description']
            temp -= 273.15
            print(x,"\n\n\n")
            print(temp, humidity, pressure, wind, description, sep="\n")
            temp = str(temp)


            t.config(text=(temp[0:4], "℃"))
            h.config(text=(humidity, "%"))
            p.config(text=(pressure, "hPa"))
            w.config(text=(wind, "m/s"))
            de.config(text=description)

            first = datetime.now()
            day_1.configure(text=first.strftime("%A"))

            second = first+timedelta(days=1)
            day_2.configure(text=second.strftime("%A"))

            third = first + timedelta(days=2)
            day_3.configure(text=third.strftime("%A"))

            fourth = first + timedelta(days=3)
            day_4.configure(text=fourth.strftime("%A"))

            fifth = first + timedelta(days=4)
            day_5.configure(text=fifth.strftime("%A"))

            sixth = first + timedelta(days=5)
            day_6.configure(text=sixth.strftime("%A"))


            firstdayimage = x['daily'][0]['weather'][0]['icon']

            photo1 = ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
            firstimage.configure(image=photo1)
            firstimage.image=photo1

            tempday1 = x['daily'][0]['temp']['day']
            tempnight1=x['daily'][0]['temp']['night']

            tempday1-=273.15
            tempnight1-=273.15
            tempday1 = str(tempday1)
            tempnight1=str(tempnight1)

            day1temp.configure(text=f"Day : {tempday1[0:4]}℃\nNight : {tempnight1[0:4]}℃")


            seconddayimage = x['daily'][1]['weather'][0]['icon']

            img_1 = (Image.open(f"icon/{seconddayimage}@2x.png"))
            resize_1 = img_1.resize((50,50))
            photo2 = ImageTk.PhotoImage(resize_1)
            secondimage.configure(image=photo2)
            secondimage.image=photo2

            tempday2 = x['daily'][1]['temp']['day']
            tempnight2=x['daily'][1]['temp']['night']

            tempday2-=273.15
            tempnight2-=273.15
            tempday2 = str(tempday2)
            tempnight2=str(tempnight2)

            day2temp.configure(text=f"Day : {tempday2[0:4]}℃\nNight : {tempnight2[0:4]}℃")

            thirddayimage = x['daily'][2]['weather'][0]['icon']

            img_2 = (Image.open(f"icon/{thirddayimage}@2x.png"))
            resize_2 = img_2.resize((50,50))
            photo3 = ImageTk.PhotoImage(resize_2)
            thirdimage.configure(image=photo3)
            thirdimage.image=photo3

            tempday3 = x['daily'][2]['temp']['day']
            tempnight3=x['daily'][2]['temp']['night']

            tempday3-=273.15
            tempnight3-=273.15
            tempday3 = str(tempday3)
            tempnight3=str(tempnight3)

            day3temp.configure(text=f"Day : {tempday3[0:4]}℃\nNight : {tempnight3[0:4]}℃")


            fourthdayimage = x['daily'][3]['weather'][0]['icon']

            img_3 = (Image.open(f"icon/{fourthdayimage}@2x.png"))
            resize_3 = img_1.resize((50,50))
            photo4 = ImageTk.PhotoImage(resize_3)
            fourthimage.configure(image=photo4)
            fourthimage.image=photo4

            tempday4 = x['daily'][3]['temp']['day']
            tempnight4=x['daily'][3]['temp']['night']

            tempday4-=273.15
            tempnight4-=273.15
            tempday4 = str(tempday4)
            tempnight4=str(tempnight4)

            day4temp.configure(text=f"Day : {tempday4[0:4]}℃\nNight : {tempnight4[0:4]}℃")

            fifthdayimage = x['daily'][4]['weather'][0]['icon']

            img_4 = (Image.open(f"icon/{fifthdayimage}@2x.png"))
            resize_4 = img_1.resize((50,50))
            photo5 = ImageTk.PhotoImage(resize_4)
            fifthimage.configure(image=photo5)
            fifthimage.image=photo5

            tempday5 = x['daily'][4]['temp']['day']
            tempnight5=x['daily'][4]['temp']['night']

            tempday5-=273.15
            tempnight5-=273.15
            tempday5 = str(tempday5)
            tempnight5=str(tempnight5)

            day5temp.configure(text=f"Day : {tempday5[0:4]}℃\nNight : {tempnight5[0:4]}℃")

            sixthdayimage = x['daily'][5]['weather'][0]['icon']

            img_5 = (Image.open(f"icon/{sixthdayimage}@2x.png"))
            resize_5 = img_1.resize((50,50))
            photo6 = ImageTk.PhotoImage(resize_5)
            sixthimage.configure(image=photo6)
            sixthimage.image=photo6

            tempday6 = x['daily'][5]['temp']['day']
            tempnight6=x['daily'][5]['temp']['night']

            tempday6-=273.15
            tempnight6-=273.15
            tempday6 = str(tempday6)
            tempnight6=str(tempnight6)

            day6temp.configure(text=f"Day : {tempday6[0:4]}℃\nNight : {tempnight6[0:4]}℃")
        except:
            messagebox.showerror('Error', 'An error occured.')

    def enter(e):
        if entry.get() != "":
            get_weather()
        else:
            messagebox.showerror('Error',"Please Enter a City")


    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    app.geometry("890x500")
    app.resizable(False,False)
    app.title("Weather Forecasting Application")

    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=40, fill="both", expand=True)

    headding = customtkinter.CTkLabel(master=frame_1, text="Weather Forecast", text_color="#57adff", text_font=("Times New Romans", 18), justify=LEFT)
    headding.pack(pady=12, padx=10)

    frame_2 = customtkinter.CTkFrame(master=frame_1, border_width=1, fg_color="gray10", border_color="white", width=200, height=220)
    frame_2.place(x=30, y=40)

    label_1 = customtkinter.CTkLabel(master=frame_2, text="   Temperature : ",text_color="white", text_font=("Helvitica",10), anchor='w')
    label_1.place(x=8, y=15)

    label_2 = customtkinter.CTkLabel(master=frame_2, text="   Humidity : ", text_color="white", text_font=("Helvitica",10), anchor='w')
    label_2.place(x=8, y=55)

    label_3 = customtkinter.CTkLabel(master=frame_2, text="   Pressure : ", text_color="white",  text_font=("Helvitica",10), anchor='w')
    label_3.place(x=8, y=95)

    label_4 = customtkinter.CTkLabel(master=frame_2, text="   Wind Speed : ", text_color="white", text_font=("Helvitica",10), anchor='w')
    label_4.place(x=8, y=135)

    label_5 = customtkinter.CTkLabel(master=frame_2, text="   Description : ", text_color="white", text_font=("Helvitica",10), anchor='w')
    label_5.place(x=8, y=175)


    search = load_image("\\layer 6.png", 20)

    entry = customtkinter.CTkEntry(master=frame_1, justify='center', border_width=0, border_color=None, height=35, width=500, placeholder_text="Enter Your City Name")
    entry.place(x=270, y=100)

    search_btn = customtkinter.CTkButton(master=frame_1, text="", fg_color="gray22", width=10, border_width=0, hover_color="gray84", image=search, command=get_weather)
    search_btn.place(x=720, y=103)

    app.bind('<Return>',enter)

    frame_3 = customtkinter.CTkFrame(master=frame_1, height=160, width=750)
    frame_3.pack(pady=10, side=BOTTOM)

    #==== bottom box ======

    firstbox = PhotoImage(file="1.png")
    secondbox = PhotoImage(file="2.png")

    Label(frame_3, image=firstbox,bg="gray24").place(x=10,y=10)
    Label(frame_3, image=secondbox, bg="gray24").place(x=260, y=18)
    Label(frame_3, image=secondbox, bg="gray24").place(x=358, y=18)
    Label(frame_3, image=secondbox, bg="gray24").place(x=456, y=18)
    Label(frame_3, image=secondbox, bg="gray24").place(x=554, y=18)
    Label(frame_3, image=secondbox, bg="gray24").place(x=653, y=18)


    clock = customtkinter.CTkLabel(master=frame_1, text="", text_color="white", text_font=("Helvatica",30,"bold"))
    clock.place(x=625, y=20)

    tz = customtkinter.CTkLabel(master=frame_1, text="", text_color="white", text_font=("Helvatica", 10))
    tz.place(x=645, y=60)

    t = Label(frame_2, font=("Helvetica", 10),fg="white", bg="gray10")
    t.place(x=102, y=19)
    h = Label(frame_2, font=("Helvetica", 10),fg="white", bg="gray10")
    h.place(x=102, y=59)
    p = Label(frame_2, font=("Helvetica", 10),fg="white", bg="gray10")
    p.place(x=102, y=97)
    w = Label(frame_2, font=("Helvetica", 10),fg="white", bg="gray10")
    w.place(x=102, y=137)
    de = Label(frame_2, font=("Helvetica", 10),fg="white", bg="gray10")
    de.place(x=102, y=179)


    firstframe = Frame(frame_3,width=232,height=132,bg="gray10")
    firstframe.place(x=14,y=14)

    day_1 = Label(firstframe,font=('Helvetica', 20),bg="gray10",fg="white")
    day_1.place(x=100,y=5)

    firstimage = Label(firstframe,bg='gray10')
    firstimage.place(x=1,y=15)

    day1temp = Label(firstframe,bg="gray10",fg="white",font=("Helvetica", 12))
    day1temp.place(x=100,y=50)

    secondframe = Frame(frame_3,width=73,height=118,bg="gray10")
    secondframe.place(x=264, y=22)

    day_2= Label(secondframe,font=('Helvetica', 8),bg="gray10",fg="white")
    day_2.place(x=10,y=5)

    secondimage = Label(secondframe,bg="gray10")
    secondimage.place(x=3,y=20)

    day2temp = Label(secondframe,bg="gray10",fg="white",font=("Helvetica", 8))
    day2temp.place(x=10, y=70)

    thirdframe = Frame(frame_3,width=73,height=118,bg="gray10")
    thirdframe.place(x=362, y=22)

    day_3 = Label(thirdframe,font=('Helvetica', 8),bg="gray10",fg="white")
    day_3.place(x=10,y=5)

    thirdimage = Label(thirdframe,bg="gray10")
    thirdimage.place(x=3,y=20)

    day3temp = Label(thirdframe,bg="gray10",fg="white",font=("Helvetica", 8))
    day3temp.place(x=10, y=70)

    fourthframe = Frame(frame_3,width=73,height=118,bg="gray10")
    fourthframe.place(x=460, y=22)

    day_4 = Label(fourthframe,font=('Helvetica', 8),bg="gray10",fg="white")
    day_4.place(x=10,y=5)

    fourthimage = Label(fourthframe,bg="gray10")
    fourthimage.place(x=3,y=20)

    day4temp = Label(fourthframe,bg="gray10",fg="white",font=("Helvetica", 8))
    day4temp.place(x=10, y=70)

    fifthframe = Frame(frame_3,width=73,height=118,bg="gray10")
    fifthframe.place(x=558, y=22)


    day_5 = Label(fifthframe,font=('Helvetica', 8),bg="gray10",fg="white")
    day_5.place(x=10,y=5)

    fifthimage = Label(fifthframe,bg="gray10")
    fifthimage.place(x=3,y=20)

    day5temp = Label(fifthframe,bg="gray10",fg="white",font=("Helvetica", 8))
    day5temp.place(x=10, y=70)


    sixthframe = Frame(frame_3,width=73,height=118,bg="gray10")
    sixthframe.place(x=657, y=22)

    day_6 = Label(sixthframe,font=('Helvetica', 8),bg="gray10",fg="white")
    day_6.place(x=10,y=5)

    sixthimage = Label(sixthframe,bg="gray10")
    sixthimage.place(x=3,y=20)

    day6temp = Label(sixthframe,bg="gray10",fg="white",font=("Helvetica", 8))
    day6temp.place(x=10, y=70)

    app.mainloop()

class splachscreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_splachscreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        self.timer.start(35)


        self.show()

    def progress(self):
        global  counter

        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            self.close()
            MainWindow()


        counter+=1


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = splachscreen()
    sys.exit(app.exec_())
