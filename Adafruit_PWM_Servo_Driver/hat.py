#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
from Adafruit_I2C import Adafruit_I2C

import time

pwm = PWM(0x7F)

adc = Adafruit_I2C(0x48)

pwm.setPWMFreq(1000)
lightSensorChannel = 5
tempChannel = 4

 
while(1):
	pwm.setPWM(0, 0, 4095)
	pwm.setPWM(4, 0, 4095)
	time.sleep(1)
	pwm.setPWM(0, 4095, 4095)
	pwm.setPWM(4, 4095, 4095)
	time.sleep(1)

	if (lightSensorChannel % 2 == 0):
		c = lightSensorChannel / 2
	else:
		c = (lightSensorChannel -1) / 2 + 4

	if (tempChannel % 2 == 0):
		c_temp = tempChannel / 2
	else:
		c_temp = (tempChannel - 1) / 2 + 4

	reg= 0x84 | (c << 4)
	reg_temp = 0x84 | (c_temp << 4)


	adc.writeRaw8(reg)
	lightLevel = adc.readU8(reg)

	adc.writeRaw8(reg_temp)
	tempLevel = adc.readU8(reg_temp)
	real_temp = ((adc.readU8(reg_temp) * 3.3) /256 - 0.4) / 0.0195

	print( "Light level at %02X is %x(hex) %d(decimal) " %(reg, lightLevel,lightLevel))

	print( "Temp level at %02X is %x(hex) %d(decimal) " %(reg_temp,tempLevel, tempLevel ))
	print( "real temp is %4d" %(real_temp))

