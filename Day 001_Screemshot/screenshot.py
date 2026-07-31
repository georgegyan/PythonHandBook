import pyautogui
from PIL import Image

screenshot = pyautogui.screenshot()

filename = "screenshot.png"
screenshot.save(filename)

image = Image.open(filename)
image.show()

print(f"Screenshot saved as {filename}")