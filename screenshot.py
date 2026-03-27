import pyautogui
import os
from datetime import datetime

SAVE_DIR = "screenshots"

def take_screenshot():

    os.makedirs(SAVE_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{SAVE_DIR}/screenshot_{timestamp}.png"

    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

    return filename
