from pynput import mouse
import time

# Define the coordinates for the two points on the screen
point1 = (384, 201)
point2 = (415, 248)

# Create a mouse controller
mouse_controller = mouse.Controller()

while True:
    # Move the mouse to point 1 and click
    mouse_controller.position = point1
    mouse_controller.click(mouse.Button.left, 1)

    # Wait for 4 seconds
    time.sleep(4)

    # Move the mouse to point 2 and click
    mouse_controller.position = point2
    mouse_controller.click(mouse.Button.left, 1)

    # Wait for 4 seconds
    time.sleep(4)
