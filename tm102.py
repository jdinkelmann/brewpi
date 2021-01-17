import time
import smbus

i2c_chan = 1
i2c_address = 0x4a

reg_temp = 0x00
reg_config = 0x01

def two_comps(val, bits):
    if(val & (1 << (bits - 1))) != 0:
        val = val - (1 << bits)
        
    return val