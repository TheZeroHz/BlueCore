import time
import board
import digitalio
import neopixel

# ------------------------
# TTP223 Touch Module Setup (Digital Input)
# ------------------------
touch_pin = digitalio.DigitalInOut(board.GPIO1)  # Connect TTP223 OUT to GPIO1
touch_pin.direction = digitalio.Direction.INPUT
touch_pin.pull = digitalio.Pull.DOWN  # Use pull-down if TTP223 doesn't have one

# ------------------------
# NeoPixel Setup
# ------------------------
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3, auto_write=False)

# ------------------------
# Colors
# ------------------------
TOUCH_COLOR = (0, 255, 0)  # Green when touched
IDLE_COLOR = (0, 0, 0)    # Off when not touched

print("TTP223 Touch Sensor + NeoPixel Ready!")

while True:
    if touch_pin.value:  # HIGH when touched
        print(0)
        pixels.fill(TOUCH_COLOR)
    else:
        print(1)
        pixels.fill(IDLE_COLOR)
    
    pixels.show()
    time.sleep(0.1)
