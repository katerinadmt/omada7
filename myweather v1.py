import requests
import tkinter

def getweather():
  
        city = entr1.get()
        url="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
        json_data = requests.get(url).json()
       
            
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp']-273.15)
        tx1=str(temp)+'°C'
        label1.config(text = tx1)
        label2.config(text = condition)
   














window=tkinter.Tk()
window.title('my weather')
window.geometry('600x600')
box_value=tkinter.StringVar()
entr1=tkinter.Entry(window,textvariable=box_value, font='bold')
entr1.pack()
buttom=tkinter.Button(window,text='',command = getweather,width = 40)
buttom.pack()
label1=tkinter.Label(window,justify='center',font='bold')
label1.pack()
label2=tkinter.Label(window,justify='center',font='bold')
label2.pack()
window.mainloop()
