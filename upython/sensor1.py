'Quick example for the i2c driver.'

def run_sensor1():
    '''Runs all of the methods from the i2c driver. Imports are included in the
    method for re-importing any updates when testing.

    '''
    import si7021
    import machine
    from time import sleep_ms
    i2c = machine.I2C(machine.Pin(0), machine.Pin(2))

    temp_sensor = si7021.Si7021(i2c)
    print('Serial:              {value}'.format(value=temp_sensor.serial))
    print('Identifier:          {value}'.format(value=temp_sensor.identifier))
    print('Temperature:         {value}'.format(value=temp_sensor.temperature))
    print('Relative Humidity:   {value}'.format(value=temp_sensor.relative_humidity))
    print('Fahrenheit:          {value}'.format(value=si7021.convert_celcius_to_fahrenheit(temp_sensor.temperature)))
    
    #sleep_ms(5000)
    #print('Temperature:         {value}'.format(value=temp_sensor.temperature))