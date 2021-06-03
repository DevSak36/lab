import time
import usb.core
import usb.util

# https://www.usb.org/
# HID\VID_1BCF&PID_0007&COL01\6&1C664702&1&0000
'''
VID = 0x1BCF
PID = 0x0007

device_usb = usb.core.find(idVendor=VID, idProduct=PID)

if not device_usb:
    print("Could not find the device  :( ")
    exit(1)
print("Yeeha!, Found the device  :) ")
print(device_usb)
exit(0)
'''
#all usb list
device_usbs = usb.core.find()
print(device_usbs)
