from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import json
from datetime import *
from details_page import *
root=Tk()
root.title("Weather App")

# Create a Canvas widget with the same size as the window
canvas = tk.Canvas(root, width=800, height=800)
root.geometry("900x537")
root.resizable(False, False) 

def getWeather():
    city = textfield.get()
    try :
        api_key = 'bab8b363631cb73a8e0cbaaec7044a5d'
        url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        data = response.json()
        # Appel à l'API OpenWeatherMap pour obtenir les données météorologiques
        geolocator = Nominatim(user_agent="MyGeocoderApp")
        location = geolocator.geocode(city)
        url1 = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        requests1 = requests.get(url1)
        main =requests1.json()
        api_key2 = '8e5ef3dffdc44cc2a6b170725242104'
        url2 = f'https://api.weatherapi.com/v1/forecast.json?key={api_key2}&q={city}&days=5'
        response2 = requests.get(url2)
        data2 = response2.json()
        
        if data['cod'] == '200' and main['cod'] == 200:
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
            timezone.config(text=result)
            long_lat.config(text=f"{round(location.latitude,4)}°N, {round(location.longitude,4)}E")
            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time = local_time.strftime("%H:%M")
            clock.config(text=current_time)
            hourly_data = data['list']
            current_temp = main['main']['temp']
            current_wind=main['wind']['speed']
            current_pressure=main['main']['pressure']
            current_humidity=main['main']['humidity']
            temp_max=main['main']['temp_max']
            temp_min=main['main']['temp_min']
            current_feels=main['main']['feels_like']
            current_weather_main=main['weather'][0]['main']
            current_weather_description=main['weather'][0]['description']
            current_weather_icon=main['weather'][0]['icon']
            sunset=main['sys']['sunset']
            sunrise=main['sys']['sunrise']
            category_weather=(Image.open(f"category/{current_weather_icon}2x.png"))
            resized_category= category_weather.resize((254,242))
            image_category=ImageTk.PhotoImage(resized_category) 
            main_label.config(image=image_category)  
            main_label.image=image_category 
            if int(current_temp) < 27 :
                t.config(fg="blue")
                t.config(text=f"{int(current_temp)}°C")
            elif 22 <= int(current_temp) < 34 :
                t.config(fg="#FF5733")
                t.config(text=f"{int(current_temp)}°C")
            else :
                t.config(fg="red")
                t.config(text=f"{int(current_temp)}°C")
                
            c.config(text=f"{current_weather_main}({current_weather_description})\n\nfeels like {int(current_feels)}°C")
            details.config(text="More details >")
            def details_click(event):
                choice_page(main,data2,root,current_time) 
            def details_enter(event):
                details.config(fg="red")  

            def detail_leave(event):
                details.config(fg="black")  
                
            details.bind("<Enter>", details_enter)
            details.bind("<Leave>", detail_leave)
            details.bind("<Button-1>", details_click)
            sunrise_label.place(x=560,y=200)
            sunset_label.place(x=830,y=200)
            bow_label.place(x=525,y=100)
            
            sunrise_time_label.config(text=f"{datetime.fromtimestamp(sunrise).strftime('%H:%M')}")
            sunset_time_label.config(text=f"{datetime.fromtimestamp(sunset).strftime('%H:%M')}")
            for i in range(0,10):
                hour_data = hourly_data[i]
                time = hour_data['dt_txt']
                date_object = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                # Format the datetime object to display only hours and minutes
                temperature = hour_data['main']['temp']
                icon = hour_data['weather'][0]['icon']
                wind=float(hour_data['wind']['speed'])*3600/1000
                temperature_labels[i].config(text=f"{date_object.strftime('%H:%M')} \n{temperature}°C")
                image_weather=(Image.open(f"icon/{icon}@2x.png"))
                resized_image= image_weather.resize((50,50))
                photo=ImageTk.PhotoImage(resized_image) 
                image_labeles[i].config(image=photo)  
                image_labeles[i].image=photo    
                wind_labels[i].config(text=f"{wind:.2f}km/h")
        else:
            messagebox.showerror("Error", f"City '{city}' not found")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")            
        
def getWeather1(event) :
    getWeather()
    
    
##icon
image_icon=PhotoImage(file="Images/logo.png")
root.iconphoto(False,image_icon)


##search box
Search_image=PhotoImage(file="Images\\Copy of search.png")
myimage= Label(image=Search_image, bg=root.cget('bg'))
myimage.place(x=20,y=20)
textfield= tk.Entry(root, justify= "center" ,width=17, font=("poppins",25, "bold"),bg="#484848", border=0, fg="white")
textfield.place(x=110,y=40)
textfield.focus()

weat_image=PhotoImage(file="Images/Layer 7.png")
weatherimage=Label(root, image=weat_image, bg="#404040")
weatherimage.place(x=50,y=34)



#main bloc
main_label = Label(root,bg=root.cget('bg'))
main_label.place (x=20,y=100)
t=Label(root,font=("arial",30,'bold'),fg="blue")
t.place(x=300,y=130)
c=Label(root,font=("arial",15, 'bold'))
c.place(x=300,y=230)

#additionnal bloc
sunrise_image=(Image.open(f"icon/sunrise.png"))
resized_sunrise_image= sunrise_image.resize((60,60))
photo1=ImageTk.PhotoImage(resized_sunrise_image) 
sunrise_label=tk.Label(root,image=photo1,bg=root.cget('bg'))
sunrise_time_label = tk.Label(root,bg=root.cget('bg'))
sunrise_time_label.place(x=575,y=250)

sunset_image=(Image.open(f"icon/sunset.png"))
resized_sunset_image= sunset_image.resize((60,60))
photo2=ImageTk.PhotoImage(resized_sunset_image) 
sunset_label=tk.Label(root,bg=root.cget('bg'),image=photo2)
sunset_time_label = tk.Label(root,bg=root.cget('bg'))
sunset_time_label.place(x=845,y=250)

bow_image=(Image.open(f"icon/bow.png"))
resized_bow_image= bow_image.resize((400,100))
photo3=ImageTk.PhotoImage(resized_bow_image) 
bow_label=tk.Label(root,bg=root.cget('bg'),image=photo3)


details = tk.Label(root, fg="black", font=("Helvetica", 15, "underline"),bg=root.cget('bg'))
details.place(x=650,y=300)

#search box
Search_icon=PhotoImage(file="Images\\Copy of search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2" ,bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)
textfield.bind("<Return>",getWeather1)



##Bottom box
frame=Frame (root, width=90,height=180,bg="#212120")
frame. pack(side=BOTTOM,fill=X)
#bottom boxes
secondbox=PhotoImage(file="Images/Rounded Rectangle 2 copy.png")
l1=Label(frame, image=secondbox, bg= "#212120") .place(x=0,y=30)
l2=Label(frame, image=secondbox, bg="#212120") .place(x=90,y=30)
l3=Label (frame, image=secondbox, bg= "#212120") .place (x=180,y=30)
l4=Label (frame, image=secondbox, bg="#212120") .place(x=270,y=30)
l5=Label (frame, image=secondbox, bg= "#212120") .place(x=360,y=30)
l6=Label (frame, image=secondbox, bg="#212120") .place (x=450,y=30)
l7=Label(frame, image=secondbox, bg= "#212120") .place (x=540,y=30)
l8=Label(frame, image=secondbox, bg= "#212120") .place (x=630,y=30)
l9=Label(frame, image=secondbox, bg= "#212120") .place (x=720,y=30)
l10=Label(frame, image=secondbox, bg= "#212120") .place (x=810,y=30)


#clock (here we will place time)
clock=Label(root, font=("Helvetica",30, 'bold'),fg="black")
clock.place(x=650,y=20)
#timezone
timezone=Label(root, font=("Helvetica",20, 'bold'),fg="black",bg=root.cget('bg'))
timezone.place(x=650,y=100)
long_lat=Label(root, font=("Helvetica",15, 'bold'),fg="black")
long_lat.place(x=650,y=70)




temperature_labels=[]
image_labeles=[]
wind_labels=[]
#first cell
firstframe=Frame(root, width=75, height=118,bg="#212120")
firstframe.place(x=3,y=390)

hour1=Label(firstframe,bg="#212120",fg="#fff",width=10)
hour1.place(x=0,y=0)
temperature_labels.append(hour1)

firstimage=Label(firstframe,bg="#212120",width=70)
firstimage.place(x=0,y=35)
image_labeles.append(firstimage)

wind1=Label(firstframe,bg="#212120",width=10,fg="#fff")
wind1.place(x=0,y=95)
wind_labels.append(wind1)
#second cell
secondframe=Frame(root, width=75, height=118,bg="#212120")
secondframe.place(x=93,y=390)
hour2=Label(secondframe,bg="#212120",width=10,fg="#fff")
hour2.place(x=0,y=0)
temperature_labels.append(hour2)
secondimage=Label(secondframe,bg="#212120",width=70)
secondimage.place(x=0,y=35)
image_labeles.append(secondimage)
wind2=Label(secondframe,bg="#212120",width=10,fg="#fff")
wind2.place(x=0,y=95)
wind_labels.append(wind2)
#third cell
thirdframe=Frame(root, width=75, height=118,bg="#212120")
thirdframe.place(x=183,y=390)
hour3=Label(thirdframe,width=10,bg="#212120",fg="#fff")
hour3.place(x=0,y=0)
temperature_labels.append(hour3)
thirdimage=Label(thirdframe,bg="#212120",width=70)
thirdimage.place(x=0,y=35)
image_labeles.append(thirdimage)
wind3=Label(thirdframe,bg="#212120",width=10,fg="#fff")
wind3.place(x=0,y=95)
wind_labels.append(wind3)
#fouth cell
fourthframe=Frame(root, width=75, height=118,bg="#212120")
fourthframe.place(x=273,y=390)
hour4=Label(fourthframe, width= 10,bg="#212120",fg="#fff")
hour4.place(x=0,y=0)
temperature_labels.append(hour4)
fourthimage=Label(fourthframe,bg="#212120",width=70)
fourthimage.place(x=0,y=35)
image_labeles.append(fourthimage)
wind4=Label(fourthframe,bg="#212120",width=10,fg="#fff")
wind4.place(x=0,y=95)
wind_labels.append(wind4)
#fifth frame
fifthframe=Frame(root, width=75, height=118,bg="#212120")
fifthframe.place(x=363,y=390)
hour5=Label(fifthframe,  width=10,bg="#212120",fg="#fff")
hour5.place(x=0,y=0)
temperature_labels.append(hour5)
fifthimage=Label(fifthframe,bg="#212120",width=70)
fifthimage.place(x=0,y=35)
image_labeles.append(fifthimage)
wind5=Label(fifthframe,bg="#212120",width=10,fg="#fff")
wind5.place(x=0,y=95)
wind_labels.append(wind5)
#sixth frame
sixthframe=Frame(root, width=75, height=118,bg="#212120")
sixthframe.place(x=453,y=390)
hour6=Label(sixthframe, width=10,bg="#212120",fg="#fff")
hour6.place(x=0,y=0)
temperature_labels.append(hour6)
sixthimage=Label(sixthframe,bg="#212120",width=70)
sixthimage.place(x=0,y=35)
image_labeles.append(sixthimage)
wind6=Label(sixthframe,bg="#212120",width=10,fg="#fff")
wind6.place(x=0,y=95)
wind_labels.append(wind6)
#seventh frame
seventhframe=Frame(root, width=75, height=118,bg="#212120")
seventhframe.place(x=543,y=390)
hour7=Label(seventhframe, width=10,bg="#212120",fg="#fff")
hour7.place(x=0,y=0)
temperature_labels.append(hour7)
seventhimage=Label(seventhframe,bg="#212120",width=70)
seventhimage.place(x=0,y=35)
image_labeles.append(seventhimage)
wind7=Label(seventhframe,bg="#212120",width=10,fg="#fff")
wind7.place(x=0,y=95)
wind_labels.append(wind7)
#eightth frame
eightthframe=Frame(root, width=75, height=118,bg="#212120")
eightthframe.place(x=633,y=390)
hour8=Label(eightthframe, width=10,bg="#212120",fg="#fff")
hour8.place(x=0,y=0)
temperature_labels.append(hour8)
eightthimage=Label(eightthframe,bg="#212120",width=70)
eightthimage.place(x=0,y=35)
image_labeles.append(eightthimage)
wind8=Label(eightthframe,bg="#212120",width=10,fg="#fff")
wind8.place(x=0,y=95)
wind_labels.append(wind8)
#nineth frame
ninethframe=Frame(root, width=75, height=118,bg="#212120")
ninethframe.place(x=723,y=390)
hour9=Label(ninethframe, width=10,bg="#212120",fg="#fff")
hour9.place(x=0,y=0)
temperature_labels.append(hour9)
ninethimage=Label(ninethframe,bg="#212120",width=70)
ninethimage.place(x=0,y=35)
image_labeles.append(ninethimage)
wind9=Label(ninethframe,bg="#212120",width=10,fg="#fff")
wind9.place(x=0,y=95)
wind_labels.append(wind9)
#tenth frame
tenthframe=Frame(root, width=75, height=118,bg="#212120")
tenthframe.place(x=813,y=390)
hour10=Label(tenthframe, width=10,bg="#212120",fg="#fff")
hour10.place(x=0,y=0)
temperature_labels.append(hour10)
tenthimage=Label(tenthframe,bg="#212120",width=70)
tenthimage.place(x=0,y=35)
image_labeles.append(tenthimage)
wind10=Label(tenthframe,bg="#212120",width=10,fg="#fff")
wind10.place(x=0,y=95)
wind_labels.append(wind10)


root.mainloop()