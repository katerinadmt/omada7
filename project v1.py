import folium
import requests
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
36.8682:27.2557,
36.2225:28.0215,
38.2507139:22.0858224,
38.5273:23.8348,38.8744:24.5509}  

m1=folium.Map(location=[39.6383092,22.4160706],zoom_start=7)


for lan in e:
       url="https://api.openweathermap.org/data/2.5/weather?lat="+str(lan)+"&lon="+str(e[lan])+"&appid=06c921750b9a82d8f5d1294e1586276f"
       json_data = requests.get(url).json()
       condition = json_data['weather'][0]['main']
       
       temp = int(json_data['main']['temp']-273.15)
       if condition == 'Clear':
              c='certificate'
              folium.Marker(location=[lan,e[lan]],icon=folium.Icon(color='blue',icon=c),popup=str(temp)+'°C').add_to(m1)
       elif condition == 'Clouds':
              c='cloud'
              folium.Marker(location=[lan,e[lan]],icon=folium.Icon(color='blue',icon=c),popup=str(temp)+'°C').add_to(m1)
       elif condition == 'Rain':
              
              c='tint'
              
       
              folium.Marker(location=[lan,e[lan]],icon=folium.Icon(color='blue',icon=c),popup=str(temp)+'°C').add_to(m1)
m1.save('test.html')
       
        
    
    
   
    

     
    
