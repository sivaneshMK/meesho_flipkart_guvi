import os
import time


class ScreenshotHelper:

    @staticmethod
    def take_screenshot(driver, name):
        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, f"{name}_{int(time.time())}.png")
        driver.save_screenshot(file_path)
        return file_path
