import smbus
import time

# This example is for Educaboard V1.92
# and Rapberry Pi adapter V1.3
# Ensure smbus is installed with: pip install smbus4
# sudo i2cdetect -y 1
bus = smbus.SMBus(1)# RPi revision 2 (0 for revision 1)​
i2c_address = 0x4B  # default address​

while True:
    # Reads word (2 bytes) as int - 0 is comm byte​
    rd = bus.read_word_data(i2c_address, 0)
    print(f"Raw data: {rd}")
    # Exchanges high and low bytes​
    data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
    # Ignores two least significiant bits​
    data = data >> 2
    print("Data: ", data)
    time.sleep(1)