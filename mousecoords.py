import time
from pynput import mouse

# Create a MouseController object to control the mouse
mouse_controller = mouse.Controller()

while True:
    # Get the current mouse position
    x, y = mouse_controller.position

    # Print the current mouse position
    print(f"Mouse position: ({x}, {y})")

    # Sleep for 1 second
    time.sleep(1)
