#!/usr/bin/env python
from ina219 import INA219
from ina219 import DeviceRangeError
import time

SHUNT_OHMS = 0.13

def read():
    ina = INA219(SHUNT_OHMS, address=0x45)
    ina.configure()
    i=0
    
    while 1:
        print("Mesure ",i+1)
        print("Tension: %.3f V" % ina.voltage())
        print("Courant: %.3f mA" % ina.current())
        print("Puissance: %.3f mW" % ina.power())
        print("Tension Shunt: %.3f mV" % ina.shunt_voltage())
        i=i+1
        time.sleep(2)

if __name__ == "__main__":
    read()

