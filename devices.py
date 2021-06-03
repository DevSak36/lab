import usb.core

devices = usb.core.find(find_all=True)

dev = next(devices)

print("device bus:", dev.bus)
print("device address:", dev.address)
print("device port:", dev.port_number)
print("device speed:", dev.speed)
