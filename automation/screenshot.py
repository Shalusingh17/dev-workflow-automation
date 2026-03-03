import os
import time
from datetime import datetime
from mss import mss
from PIL import Image


def take_screenshot():

    print("Waiting before screenshot...")
    time.sleep(2)  # small delay for stable capture

    screenshots_folder = "screenshots"

    if not os.path.exists(screenshots_folder):
        os.makedirs(screenshots_folder)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = os.path.join(screenshots_folder, f"update_{timestamp}.png")

    with mss() as sct:
        monitor = sct.monitors[1]  # primary screen
        screenshot = sct.grab(monitor)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
        img.save(file_path)

    print(f"Screenshot saved: {file_path}")

    return file_path