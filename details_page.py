import matplotlib.pyplot as plt
import numpy as np
from datetime import *
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
import matplotlib.pyplot as plt
from forecast_data import *
from folium import Map, Marker
from folium.plugins import MiniMap
import webbrowser
import os

def display_map(main):
    latitude = main['coord']['lat']
    longitude = main['coord']['lon']

    mymap = Map(location=[latitude, longitude], zoom_start=10)

    Marker(location=[latitude, longitude], popup="Your location").add_to(mymap)

    minimap = MiniMap()
    mymap.add_child(minimap)

    temp_file = "temp_map.html"
    mymap.save(temp_file)

    webbrowser.open("file://" + os.path.realpath(temp_file))



def plot_temp(data2):
    temparatures_matin=[obtenir_temperature_matin(data2),(obtenir_temperature_matin_jour_suivant(data2)),(obtenir_temperature_matin_jour_2(data2)),(obtenir_temperature_matin_jour_3(data2)),(obtenir_temperature_matin_jour_4(data2))]
    temperatures_nuit =[obtenir_temperature_nuit(data2),obtenir_temperature_nuit_jour_suivant(data2),obtenir_temperature_nuit_jour_2(data2),obtenir_temperature_nuit_jour_3(data2),obtenir_temperature_nuit_jour_4(data2)]
    days = [(datetime.now()+timedelta(days=0)).strftime("%m/%d"),(datetime.now()+timedelta(days=1)).strftime("%m/%d"),(datetime.now()+timedelta(days=2)).strftime("%m/%d"),(datetime.now()+timedelta(days=3)).strftime("%m/%d"),(datetime.now()+timedelta(days=4)).strftime("%m/%d")]
    plt.plot(days, temparatures_matin,marker='o',color="red",label='Morning Temperature')  # Line 1
    plt.plot(days, temperatures_nuit,marker='o',color ="blue",label='Night Temperature')  # Line 1
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_wind_speed(data2):
    wind_speeds =[obtenir_wind_speed_maintenat(data2),obtenir_wind_speed_suivant(data2),obtenir_wind_speed_2(data2),obtenir_wind_speed_3(data2),obtenir_wind_speed_4(data2)]
    days = [(datetime.now()+timedelta(days=0)).strftime("%m/%d"),(datetime.now()+timedelta(days=1)).strftime("%m/%d"),(datetime.now()+timedelta(days=2)).strftime("%m/%d"),(datetime.now()+timedelta(days=3)).strftime("%m/%d"),(datetime.now()+timedelta(days=4)).strftime("%m/%d")]
    plt.figure(figsize=(8, 6))
    plt.plot(days, wind_speeds, color='blue', marker='o')
    plt.title('Wind Speed Over Time')
    plt.xlabel('Time')
    plt.ylabel('Wind Speed (K/H)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def plot_humidity(data2):
    humidity_liste = obtenir_avg_humidity(data2)
    days = [(datetime.now()+timedelta(days=0)).strftime("%m/%d"),(datetime.now()+timedelta(days=1)).strftime("%m/%d"),(datetime.now()+timedelta(days=2)).strftime("%m/%d"),(datetime.now()+timedelta(days=3)).strftime("%m/%d"),(datetime.now()+timedelta(days=4)).strftime("%m/%d")]
    plt.figure(figsize=(8, 6))
    plt.plot(days,humidity_liste, marker='o')
    plt.title('Humidity Forecast')
    plt.xlabel('Time (hours)')
    plt.ylabel('Humidity (%)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

def plot_pressure(data2):
    pressure_list= obtenir_pressure_mb(data2)
    days = [(datetime.now()+timedelta(days=0)).strftime("%m/%d"),(datetime.now()+timedelta(days=1)).strftime("%m/%d"),(datetime.now()+timedelta(days=2)).strftime("%m/%d"),(datetime.now()+timedelta(days=3)).strftime("%m/%d"),(datetime.now()+timedelta(days=4)).strftime("%m/%d")]
    plt.figure(figsize=(8, 6))
    plt.plot(days,pressure_list, marker='o')
    plt.title('Humidity Forecast')
    plt.xlabel('Time (hours)')
    plt.ylabel('Humidity (%)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()


def plot_selected_graph(data2,combo):
    selected_option = combo.get()
    if selected_option == "temperature" :
        plot_temp(data2)
    elif selected_option == "wind speed" :
        plot_wind_speed(data2)
    elif selected_option == "humidity" :
        plot_humidity(data2)
    elif selected_option == "pressure":
        plot_pressure(data2)
    else:
        messagebox.showerror("Error ","plot not found")
    
def choice_page(main,data2,root,current_time) :
    window=tk.Toplevel(root)
    image_icon=PhotoImage(file="Images/logo.png")
    window.iconphoto(False,image_icon)
    window.geometry("900x537")
    window.resizable(False, False) 
    current_weather_label = ttk.Label(window, text="Current weather", font=("Helvetica", 16, "bold"))
    current_weather_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    # temps actuel 
    time_label = ttk.Label(window, text=current_time, font=("Helvetica", 10, "bold"))
    time_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

    # Bouton pour afficher la carte
    map_button = ttk.Button(window, text="Show Map", command= lambda : display_map(main))
    map_button.grid(row=1, column=3)

    current_temperature = str(data2['current']['temp_c']) + "°C"
    current_weather = {
        "wind speed": str(data2['current']['wind_kph']) + " km/h",
        "humidity": str(data2['current']['humidity']) + "%",
        "pressure": str(data2['current']['pressure_mb']) + " hpa"
    }
    temperature_label = ttk.Label(window, text=current_temperature, foreground="#001F3F", font=("Helvetica", 27, "bold"))
    temperature_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)

    # Affichage des valeurs de température, de vitesse du vent, d'humidité et de pression
    row_index = 4
    for key, value in current_weather.items():
        label_key = ttk.Label(window, text=f"{key.capitalize()}", font=("Helvetica", 10,"bold"))
        label_key.grid(row=row_index, column=0, sticky="w", padx=10, pady=5)
        
        label_value = ttk.Label(window, text=f"{value}", font=("Helvetica", 10))
        label_value.grid(row=row_index, column=1, sticky="w", padx=10, pady=5)
        
        row_index += 1
    
    forcast_weather_label = ttk.Label(window, text="Forcast future weather", font=("Helvetica", 16, "bold"))
    forcast_weather_label.grid(row=7, column=0, sticky="w", padx=10, pady=10)    
    choose_plot_label = ttk.Label(window, text="Choose a graph to plot", font=("Helvetica", 11, "bold"))
    choose_plot_label.grid(row=8, column=0, sticky="w", padx=10, pady=10)
    #liste des graphe a tracer
    liste=["temperature","wind speed","humidity","pressure"]
    combo = ttk.Combobox(window , values=liste,width=15)
    combo.grid(row=8,column=1)
    combo.current(0)
    # Bouton pour tracer le graphique
    plot_button = tk.Button(window, text="plot graph", command= lambda: plot_selected_graph(data2,combo))
    plot_button.grid(row=9, column=1)
    