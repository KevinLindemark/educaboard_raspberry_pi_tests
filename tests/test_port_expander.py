# https://www.youtube.com/watch?v=B9eaMVppW4U
import spidev
spibus = spidev.SpiDev()
spibus.open(0, 1)
spibus.mode = 0b01
spibus.max_speed_hz = 5000

for i in range(255):
    spibus.xfer([0x40, 0xf, 0xf1])
#data = spibus.xfer([0x41, 0x9, 0x0])
#print(bin(data[0]))
