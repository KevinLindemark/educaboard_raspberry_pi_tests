from threading import Event
from gpiozero import RotaryEncoder, RGBLED, Button

rotor = RotaryEncoder(7, 8, wrap=True, max_steps=180)
rotor.steps = -180
# JP1 SCK must be connected with dupont to JP6 GP4 (to test without SPI port expander)
btn = Button(11, pull_up=True)
done = Event()

def rotor_steps():
    print(rotor.steps) 

def rotary_encoder_pushbutton():
    print('Rotary encoder button pressed!')

def stop_script():
    print('Exiting')
    done.set()

print("rotate knob to change values")
rotor.when_rotated = rotor_steps
print('Push the button to check that it is connected')
btn.when_released = rotary_encoder_pushbutton
print('Hold the button to exit')
btn.when_held = stop_script
done.wait()
