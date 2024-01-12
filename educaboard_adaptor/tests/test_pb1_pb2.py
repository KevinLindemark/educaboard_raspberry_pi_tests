from gpiozero import Button

pb1 = Button(4)
pb2 = Button(17)
while True:
    if pb1.is_pressed:
        print("pb1 is pressed")
    if pb2.is_pressed:
        print("pb2 is pressed")

