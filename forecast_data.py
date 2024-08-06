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
from math import *
import numpy as np
def obtenir_temperature_matin(donnees_meteo):
    forecast_hours = donnees_meteo['forecast']['forecastday'][0]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        temp = hour_forecast['temp_c']
        day_or_not = hour_forecast['is_day']
        if day_or_not == 1 :
            liste.append(temp)
    return np.mean(liste)

def obtenir_temperature_matin_jour_suivant(donnees_meteo):
    forecast_hours = donnees_meteo['forecast']['forecastday'][1]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        temp = hour_forecast['temp_c']
        day_or_not = hour_forecast['is_day']
        if day_or_not == 1 :
            liste.append(temp)
    return np.mean(liste)
def obtenir_temperature_matin_jour_2(donnees_meteo):
    forecast_hours = donnees_meteo['forecast']['forecastday'][2]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        temp = hour_forecast['temp_c']
        day_or_not = hour_forecast['is_day']
        if day_or_not == 1 :
            liste.append(temp)
    return np.mean(liste)

def obtenir_temperature_matin_jour_3(donnees_meteo):
    forecast_hours = donnees_meteo['forecast']['forecastday'][3]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        temp = hour_forecast['temp_c']
        day_or_not = hour_forecast['is_day']
        if day_or_not == 1 :
            liste.append(temp)
    return np.mean(liste)

def obtenir_temperature_matin_jour_4(donnees_meteo):
    forecast_hours = donnees_meteo['forecast']['forecastday'][4]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        temp = hour_forecast['temp_c']
        day_or_not = hour_forecast['is_day']
        if day_or_not == 1 :
            liste.append(temp)
    return np.mean(liste)

def obtenir_temperature_nuit(donnees_meteo):
    forecast_hours = donnees_meteo['forecast']['forecastday'][0]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        temp = hour_forecast['temp_c']
        day_or_not = hour_forecast['is_day']
        if day_or_not == 0 :
            liste.append(temp)
    return np.mean(liste)

def obtenir_temperature_nuit_jour_suivant(donnees_meteo):
    forecast_hours = donnees_meteo['forecast']['forecastday'][1]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        temp = hour_forecast['temp_c']
        day_or_not = hour_forecast['is_day']
        if day_or_not == 0 :
            liste.append(temp)
    return np.mean(liste)
def obtenir_temperature_nuit_jour_2(donnees_meteo):
    forecast_hours = donnees_meteo['forecast']['forecastday'][2]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        temp = hour_forecast['temp_c']
        day_or_not = hour_forecast['is_day']
        if day_or_not == 0 :
            liste.append(temp)
    return np.mean(liste)

def obtenir_temperature_nuit_jour_3(donnees_meteo):
    forecast_hours = donnees_meteo['forecast']['forecastday'][3]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        temp = hour_forecast['temp_c']
        day_or_not = hour_forecast['is_day']
        if day_or_not == 0 :
            liste.append(temp)
    return np.mean(liste)


def obtenir_temperature_nuit_jour_4(donnees_meteo):
    forecast_hours = donnees_meteo['forecast']['forecastday'][4]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        temp = hour_forecast['temp_c']
        day_or_not = hour_forecast['is_day']
        if day_or_not == 0 :
            liste.append(temp)
    return np.mean(liste)

def obtenir_wind_speed_maintenat(donnee_meteo) :
    forecast_hours = donnee_meteo['forecast']['forecastday'][0]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        wind = hour_forecast['wind_kph']
        liste.append(wind)
    return np.mean(liste)

def obtenir_wind_speed_suivant(donnee_meteo) :
    forecast_hours = donnee_meteo['forecast']['forecastday'][1]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        wind = hour_forecast['wind_kph']
        liste.append(wind)
    return np.mean(liste)

def obtenir_wind_speed_2(donnee_meteo) :
    forecast_hours = donnee_meteo['forecast']['forecastday'][2]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        wind = hour_forecast['wind_kph']
        liste.append(wind)
    return np.mean(liste)

def obtenir_wind_speed_3(donnee_meteo) :
    forecast_hours = donnee_meteo['forecast']['forecastday'][3]['hour']
    liste=[]
    for hour_forecast in forecast_hours:
        wind = hour_forecast['wind_kph']
        liste.append(wind)
    return np.mean(liste)

def obtenir_wind_speed_4(donnee_meteo) :
    forecast_hours = donnee_meteo['forecast']['forecastday'][4]['hour']
    
    liste=[]
    for hour_forecast in forecast_hours:
        wind = hour_forecast['wind_kph']
        liste.append(wind)
    return np.mean(liste)

def obtenir_avg_humidity(donnee_meteo) :
    liste=[]
    for i in range(5):
        humidity = donnee_meteo['forecast']['forecastday'][i]['day']['avghumidity']
        liste.append(humidity)
    return liste

def obtenir_pressure_mb(donnee_meteo):
    liste=[]
    avg_pressure = []
    for i in range(5):
        forecast_hours = donnee_meteo['forecast']['forecastday'][i]['hour'] 
        for hour_forecast in forecast_hours:
            pressures = hour_forecast['pressure_mb']
            liste.append(pressures)
        avg_pressure.append(np.mean(liste))
    return avg_pressure





