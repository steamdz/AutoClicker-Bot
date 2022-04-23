import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

KEY = KeyCode(char="x")

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.01)

def toggle(key):
    if key == KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle) as listner:
    listner.join()
