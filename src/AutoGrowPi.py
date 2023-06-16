
import time
import time as t
import json
from gpiozero.pins.native import NativeFactory
from gpiozero import Device, LED

day_hours = 10

def startup(pin:int):
    i = 5
    while i > 0:
        print('on')
        io.output(pin, io.HIGH)#turns light on
        time.sleep(5)
        io.output(pin, io.LOW) #turns light off
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

def test(grow_light):
    while True:
        grow_light.on()
        time.sleep(5)
        grow_light.off()
        time.sleep(5)


if __name__ == "__main__":
    Device.pin_factory = NativeFactory()
    growlight = LED("GPIO04")
    test(growlight)
    '''io.setup(2, io.OUT) #Grow lamp pin
    startup(0)
    relay(0,day_hours)'''