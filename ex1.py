import folium
import tkinter
import requests
import os




    
url="https://api.openweathermap.org/data/2.5/weather?lat=39.6383092&lon=22.4160706&appid=06c921750b9a82d8f5d1294e1586276f"
json_data = requests.get(url).json()
condition = json_data['weather'][0]['main']
temp = int(json_data['main']['temp']-273.15)
tx1=str(temp)+'°C'
m1=folium.Map(location=[39.6383092,22.4160706],zoom_start=7,Layer='Circle')
folium.Marker(location=[39.6383092,22.4160706],
              tooltip='press me',
              icon=folium.Icon(color='blue',icon='cloud'),
              popup=tx1).add_to(m1)

url="https://api.openweathermap.org/data/2.5/weather?lat=39.1615550&lon=20.9858503&appid=06c921750b9a82d8f5d1294e1586276f"
json_data = requests.get(url).json()
condition = json_data['weather'][0]['main']
temp = int(json_data['main']['temp']-273.15)
tx1=str(temp)+'°C'

folium.Marker(location=[39.1615550,20.9858503],
              tooltip='press me',
              icon=folium.Icon(color='blue',icon='cloud'),
              popup=tx1).add_to(m1)

url="https://api.openweathermap.org/data/2.5/weather?lat=40.3007259&lon=21,7883119&appid=06c921750b9a82d8f5d1294e1586276f"
json_data = requests.get(url).json()
condition = json_data['weather'][0]['main']
temp = int(json_data['main']['temp']-273.15)
tx1=str(temp)+'°C'

folium.Marker(location=[40.3007259,21.7883119],
              tooltip='press me',
              icon=folium.Icon(color='blue',icon='cloud'),
              popup=tx1).add_to(m1)
                             
url="https://api.openweathermap.org/data/2.5/weather?lat=40.3007259&lon=22.4160706&appid=06c921750b9a82d8f5d1294e1586276f"
json_data = requests.get(url).json()
condition = json_data['weather'][0]['main']
temp = int(json_data['main']['temp']-273.15)
tx1=str(temp)+'°C'

folium.Marker(location=[40.3007259,22.4160706],
              tooltip='press me',
              icon=folium.Icon(color='blue',icon='cloud'),
              popup=tx1).add_to(m1)
m1.save('p2.html')
