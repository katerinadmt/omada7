import folium
import requests
import time 
from folium import IFrame
e={38.4624412:23.5947651,
37.9839412:23.7283052,
39.6639818:20.8522784,
41.0910711:23.5498031,
40.9369224:24.4122766,
40.8456920:25.8753275,
40.6403167:22.9352716,
40.3007259:21.7883119,
39.6242819:19.9215140,
39.6383092:22.4160706,
38.6248275:21.4094206,
38.265:21.746,
37.4995:22.3805,
37.6684:21.4391,
37.0377582:22.1109392,
41.1178330:25.4041307,
41.1380289:24.8862688,
41.1499443:24.1468286,
40.7929908:22.4140645,
40.5067:22.2064,
40.7794738:21.4076115,
40.5171556:21.2688435,
40.2692:22.5117,
39.5509:21.7667,
39.1615550:20.9858503,
38.9589226:20.7496811,
39.3634:21.9185,
38.9004584:22.4341691,
38.3686353:21.4283544,
37.9386936:22.9280447,
39.361:22.9395,
39.1061204:26.5538342,
35.5120831:24.0191544,
35.3400127:25.1343475,
38.3806:26.0574,
37.6349825:22.7285119,
37.0817:22.4246,
36.2225:28.0215,
38.2507139:22.0858224,
38.5273:23.8348,
38.8744:24.5509,   
35.3594:24.4774,
35.1951:25.6943,
39.8773:25.0629,
37.7805:20.8957,
38.2382:20.6323,
36.8923:27.2845,
37.743:26.9797,
35.5041:27.2112,
38.438:22.879,
37.7479:23.4352, 
37.6099:26.2642,
39.117:23.7171,
39.1737:23.486,   
 37.8011:24.9527,
 37.0135:25.4608,
 37.0223:25.1971,
 37.599:24.3237,
 37.587:25.1038, 
 36.4055:25.4491,
 36.7213:25.3496,
 36.7207:24.4999,
 36.209:22.994,
 37.404:24.9142,
 36.5295:26.3287,
 37.1373:24.494,
 37.3123:23.4366,
 36.6618:25.1257,
  }  

m1=folium.Map(location=[39.6383092,22.4160706],zoom_start=7)


for lan in e:
       url="https://api.openweathermap.org/data/2.5/weather?lat="+str(lan)+"&lon="+str(e[lan])+"&appid=06c921750b9a82d8f5d1294e1586276f"
       json_data = requests.get(url).json()
       condition = json_data['weather'][0]['main']
       temp = int(json_data['main']['temp']-273.15)
       min_temp = int(json_data['main']['temp_min'] - 273.15)
       max_temp = int(json_data['main']['temp_max'] - 273.15)
       pressure = json_data['main']['pressure']
       humidity = json_data['main']['humidity']
       wind = json_data['wind']['speed']
       sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] + 7200))
       sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] + 7200))
       f = open('weather.html','w')

       message = """<html>
       <head></head>
       <body><p>""""condition:"+condition  +  """</p></body>
       <body><p>""""temperature:"+ str(temp) + "°C" """</p></body>
       <body><p>""""Min Temp: " + str(min_temp) + "°C" """</p></body>
       <body><p>"""" Max Temp:" + str(max_temp) + "°C" """</p></body>
       <body><p>""""Pressure: " + str(pressure) +"Pa" """</p></body>
       <body><p>""""Humidity: " + str(humidity)+"g/kg" """</p></body>
       <body><p>""""Wind Speed: " + str(wind) +"m/s" """</p></body>
       <body><p>""""Sunrise: " + sunrise + "am" """</p></body>
       <body><p>""""Sunset: " + sunset+"pm" """</p></body>
         </html>"""

       f.write(message)
       f.close()
       l=open('weather.html','r')
       b=l.read()
       l.close()
       iframe=IFrame(b, width=200, height=320)
       if condition == 'Clear':
              c='certificate'
              folium.Marker(location=[lan,e[lan]],icon=folium.Icon(color='orange',icon=c),
                            popup=folium.Popup(iframe,max_width=450)).add_to(m1)
       elif condition == 'Clouds':
              c='cloud'
              folium.Marker(location=[lan,e[lan]],icon=folium.Icon(color='lightgray',icon=c),
                            popup=folium.Popup(iframe,max_width=450)).add_to(m1)
       elif condition == 'Rain':
              
              c='tint'
              
       
              folium.Marker(location=[lan,e[lan]],icon=folium.Icon(color='blue',icon=c),
                            popup=folium.Popup(iframe,max_width=450)).add_to(m1)
m1.save('myweather app.html')
       
        
    
    
   
    

     
    
