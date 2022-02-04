from time import sleep
import urequests as requests
import json
import machine
import time
import network
import esp
import si7021
from machine import I2C, Pin
from lcdi2c import LCDI2C


try:
  import usocket as socket
except:
  import socket

esp.osdebug(None)

import gc
gc.collect()

ssid = 'Livebox-5476'
password = 'Clemlgy76'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

# print('Connection successful')
# print(station.ifconfig())
sec = time.localtime()[5]
mi = time.localtime()[4]
h = time.localtime()[3]
d = time.localtime()[2]
m = time.localtime()[1]
y = time.localtime()[0]



print(str(d) + "/"+ str(m) +"/"+ str(y) +" - "+ str(h) +":" + str(mi) +":"+ str(sec))
'Quick example for the i2c driver.'

def run_sensor1():
    i2c = machine.I2C(machine.Pin(0), machine.Pin(2))

    temp_sensor = si7021.Si7021(i2c)
    print('Serial:              {value}'.format(value=temp_sensor.serial))
    print('Identifier:          {value}'.format(value=temp_sensor.identifier))
    print('Temperature:         {value}'.format(value=temp_sensor.temperature))
    print('Relative Humidity:   {value}'.format(value=temp_sensor.relative_humidity))
    print('Fahrenheit:          {value}'.format(value=si7021.convert_celcius_to_fahrenheit(temp_sensor.temperature)))


def get_measures(mode="all", measures=5, interval=1):

        i2c = I2C(scl=Pin(0), sda=Pin(2))
        s = si7021.Si7021(i2c)
        temp_data = []
        humi_data = []
        fahr_data = []
        #print("On va prendre "+str(measures)+" mesures a "+str(interval)+" secondes d'intervalle")
        while measures > 0:
            #print("mesure restante "+str(measures)+"\nTemperature:"+str(s.temperature())+"\nHumidite:"+str(s.humidity()))
            temp_data.append(s.temperature)
            humi_data.append(s.relative_humidity)
            fahr_data.append(si7021.convert_celcius_to_fahrenheit(s.temperature))
            measures -= 1
            time.sleep(interval)
        print({"all temp":temp_data})
        print({"all hum":humi_data})
        print({"all fahr": fahr_data})
        temperature = round(sum(temp_data)/len(temp_data),1)
        humidite = round(sum(humi_data)/len(humi_data),1)
        fahrenheit = round(sum(fahr_data)/len(fahr_data),1)
        if mode == "all":
            data = {"temperature": temperature, "humidite": humidite, "farenheit":fahrenheit, "capture":s.identifier}
        elif mode == "temperature":
            data = {"temperature": temperature}
        elif mode == "humidite":
            data = {"humidite": humidite}
        elif mode == "farenheit":
            data = {"farenheit": fahrenheit}
        else:
            data = {"temperature": temperature, "humidite": humidite, "farenheit": fahrenheit, "capture":s.identifier}
        return data

i2c = I2C(scl=Pin(0), sda=Pin(2))
lcd = LCDI2C( i2c, cols=16, rows=2 )
lcd.backlight()
lcd.set_cursor( (0, 0) ) # Tuple with Col=4, Row=1, zero based indexes
# display a message (no automatic linefeed)
lcd.print("Bienvenue sur notre station meteo !")
# horizontal scrolling
for i in range( 20 ):
    lcd.scroll_display()
    sleep( 0.25 )
lcd.clear()

res = station.ifconfig()[0]
lcd.backlight()
lcd.set_cursor( (0, 0) ) 
lcd.print("IP: ")
lcd.set_cursor( (0, 1) )
lcd.print(res)
sleep( 0.5 )

while True:
    try:
        data = get_measures(mode="all", measures=5, interval=1)
        i2c = I2C(scl=Pin(0), sda=Pin(2))
        s = si7021.Si7021(i2c)
        #data = {"temperature":temperature, "humidite":humidity, "farenheit":fahrenheit, "capture":sensor}
        print(data)
        json_data = json.dumps(data).encode('utf-8')
        headers = {'Content-Type':'application/json'}
        print(station.isconnected())
        r = requests.post("http://192.168.43.60:5000/api/v1/ajouter/", data=json_data, headers=headers)
        json_body= json.loads(r.text)
        print(json_body)
        print('Temperature: %3.1f' %s.temperature)
        print('Humidite: %3.1f' %s.relative_humidity)
        
        lcd = LCDI2C( i2c, cols=16, rows=2 )
        lcd.backlight()
        lcd.set_cursor( (0, 0) )
        lcd.print( "capteur: "+str(s.identifier))
        lcd.set_cursor( (0, 1) )
        lcd.print(str(d) + "/"+ str(m) +"/"+ str(y) +" - "+ str(h) +":" + str(mi) +":"+ str(sec))
        sleep( 1 )
        for i in range( 10 ):
            lcd.scroll_display()
            sleep( 0.5 )
        lcd.clear()
        lcd.set_cursor( (0, 0) )
        lcd.print("temperature: "+ str(s.temperature)+"°C") 
        lcd.set_cursor( (0, 1) )
        lcd.print("fahrenheit: "+ str(si7021.convert_celcius_to_fahrenheit(s.temperature))+"°F")
        for i in range( 20 ):
            lcd.scroll_display()
            sleep( 0.5 )
        lcd.clear()
        lcd.set_cursor( (0, 0) )
        lcd.print("humidite: "+ str(s.relative_humidity)+"%")
        sleep( 1 )
        lcd.clear()
        lcd.print(json_body)
        sleep(1)
        for i in range( 30 ):
            lcd.scroll_display()
            sleep( 0.5 )
        lcd.clear()    

        del  data, json_data
        sleep(10)
    except OSError as e:
       print('Failed')
       print(repr(e))






