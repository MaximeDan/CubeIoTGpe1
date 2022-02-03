from time import sleep
import urequests as requests
import json
import machine
from machine import I2C, Pin
import time
import network
import esp
import si7021

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

print('Connection successful')
print(station.ifconfig())

'Quick example for the i2c driver.'

def run_sensor1():
    i2c = machine.I2C(machine.Pin(0), machine.Pin(2))

    temp_sensor = si7021.Si7021(i2c)
    print('Serial:              {value}'.format(value=temp_sensor.serial))
    print('Identifier:          {value}'.format(value=temp_sensor.identifier))
    print('Temperature:         {value}'.format(value=temp_sensor.temperature))
    print('Relative Humidity:   {value}'.format(value=temp_sensor.relative_humidity))
    print('Fahrenheit:          {value}'.format(value=si7021.convert_celcius_to_fahrenheit(temp_sensor.temperature)))


 def get_measures(mode="all", measures=10, interval=1):

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


while True:
    data = get_measures(mode="all", measures=10, interval=1)
    i2c = I2C(scl=Pin(0), sda=Pin(2))
    s = si7021.Si7021(i2c)
    #data = {"temperature":temperature, "humidite":humidity, "farenheit":fahrenheit, "capture":sensor}
    print(data)
    json_data = json.dumps(data).encode('utf-8')
    headers = {'Content-Type':'application/json'}
    print(data)
    print(station.isconnected())
    r = requests.post("http://192.168.43.60:5000/api/v1/ajouter/", data=json_data, headers=headers)
    json_body= json.loads(r.text)
    print(json_body)
    print('Temperature: %3.1f' %s.temperature)
    print('Humidity: %3.1f' %s.humidity)
    del  data, json_data
    sleep(10)
    except OSError as e:
       print('Failed')
       print(repr(e))
