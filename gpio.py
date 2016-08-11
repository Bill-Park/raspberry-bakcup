import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(19, gpio.OUT)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)
gpio.setup(26, gpio.OUT)

gpio.output(19, gpio.HIGH)
gpio.output(26, gpio.LOW)

gpio.output(20, gpio.HIGH)
gpio.output(21, gpio.LOW)
print("test")
time.sleep(1)

gpio.output(19, gpio.LOW)
gpio.output(26, gpio.HIGH)

gpio.output(20, gpio.LOW)
gpio.output(21, gpio.HIGH)

time.sleep(1)

gpio.output(26, gpio.LOW)
gpio.output(21, gpio.LOW)
print("end")
gpio.cleanup()
