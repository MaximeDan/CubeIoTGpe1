import machine
from machine import I2C, Pin
from lcdi2c import LCDI2C
from time import sleep

# Pyboard - SDA=Y10, SCL=Y9
#i2c = I2C(2)
# ESP8266 sous MicroPython
i2c = I2C(scl=Pin(0), sda=Pin(2))

# Initialise l'ecran LCD
lcd = LCDI2C( i2c, cols=16, rows=2 )
lcd.backlight()

lcd.set_cursor( (0, 0) ) # Tuple with Col=4, Row=1, zero based indexes

# display a message (no automatic linefeed)
lcd.print("Hello, from MicroPython !")
sleep(1)
# horizontal scrolling
for i in range( 10 ):
	lcd.scroll_display()
	sleep( 0.500 )
	
lcd.clear()



# # backlight control
# for i in range( 3 ):
# 	lcd.backlight(False)
# 	sleep( 0.400 )
# 	lcd.backlight()
# 	sleep( 0.400 )
# 
# # Clear screen
# lcd.clear()
# 
# # Move the cursor + print
# lcd.set_cursor( (4, 1) ) # Tuple with Col=4, Row=1, zero based indexes
# lcd.print( '@' )
# # or do positionning+print with a single print() call
# lcd.print( '^', pos=(10,0) )
# lcd.print( '!', pos=(10,1) )
# sleep( 2 )
# 
# # Clear screen
# lcd.clear()
# lcd.home()  # Cursor at home position
# lcd.cursor()
# lcd.blink() # Blinking cursor
# lcd.print( "Cursor:" )
# 
# # Afficher le caractère 0 à la position (0,0)
# lcd.home()
# lcd.write( 0 )
# lcd.print( 'MC Hobby', (4,0) )
# lcd.set_cursor( (15,0) )
# lcd.write( 0 )
# lcd.clear()