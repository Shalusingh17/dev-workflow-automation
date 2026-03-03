import pyautogui
import time

def take_screenshot():

    time.sleep(2)

    image_path = "project_update.png"

    screenshot = pyautogui.screenshot()

    screenshot.save(image_path)

    print("Screenshot saved")

    return image_path