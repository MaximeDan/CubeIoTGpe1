from machine import Pin
from time import sleep
import urequests as requests
import json
import si7021
import machine
from machine import I2C, Pin
import time
import network
import esp
import i2c

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



while True:
    try:
        i2c = machine.I2C(machine.Pin(0), machine.Pin(2))
        temp_sensor = si7021.Si7021(i2c)
        sensor = temp_sensor.identifier
        temperature = temp_sensor.temperature
        humidity = temp_sensor.relative_humidity
        fahrenheit = si7021.convert_celcius_to_fahrenheit(temp_sensor.temperature)

        data = {"temperature":temperature, "humidite":humidity, "farenheit":fahrenheit, "capture":sensor}
        print(data)
        json_data = json.dumps(data).encode('utf-8')
        headers = {'Content-Type':'application/json'}
        print(data)
        print(station.isconnected())
        r = requests.post("http://192.168.43.60:5000/api/v1/ajouter/", data=json_data, headers=headers)
        #r = requests.post("http://127.0.0.1:5000/api/v1/donnees/", json = data)
        json_body= json.loads(r.text)
        #json_body= r
        print(json_body)
        print('Temperature: %3.1f' %temperature)
        print('Humidity: %3.1f' %humidity)
        del temperature, humidity, data, json_data
        sleep(10)
     except OSError as e:
        print('Failed')
        print(repr(e))
    