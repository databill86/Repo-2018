import pigpio
import RPi.GPIO as GPIO

pi = pigpio.pi()

if not pi.connected:
    print("no pi")
    exit()

bus = 1
address = 0x5a
read_bytes = 9

handle = pi.i2c_open(bus,address)
count, data = pi.i2c_read_device(handle, read_bytes)

pi.i2c_close(handle)
pi.stop()

print(count)
print(data)

exit()
