# https://www.youtube.com/watch?v=B9eaMVppW4U
import spidev
from time import sleep
spibus = spidev.SpiDev()
spibus.open(0, 1)
spibus.mode = 0b01
spibus.max_speed_hz = 5000

# toggle led2 (not sure why this works)
spibus.xfer([0x40, 0x0, 0xf0])
sleep(1)
spibus.xfer([0x40, 0x0, 0xf])

# read from all
for i in range(18):
    print(spibus.xfer([0x41, i, 0x0]))

