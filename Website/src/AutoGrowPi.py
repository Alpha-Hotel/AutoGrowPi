import RPi.GPIO as io
import time
import time as t
import json

day_hours = 10

def startup(pin:int):
    i = 5
    while i > 0:
        print('on')
        io.output(pin,0)#turns light on
        time.sleep(5)
        io.output(pin,1) #turns light off
        print('off')
        time.sleep(5)
        i-=1


def relay(pin:int, day_hours:int)->None:
    #Growlight controller. 
    while True:
        print('on')
        relay.off() #turns light on
        time.sleep((day_hours/24)*86_400) #86_400 seconds in a day
        relay.on() #turns light off
        print('off')
        time.sleep(((24-day_hours)/24)*86_400)#86_400


if __name__ == "__main__":
    io.setup(0, io.OUT) #Grow lamp pin
    startup(0)
    relay(0,day_hours)