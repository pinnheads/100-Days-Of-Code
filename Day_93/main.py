from numpy import *
from time import sleep

from PIL import ImageGrab, ImageOps
import pyautogui as py


def pressSpace():
    py.keyDown("space")
    py.keyUp("space")


def IMG(x, y, w, h):
    Box = (x, y, w, h)  # Use your own Coordinates here
    image = ImageGrab.grab(Box)
    image = ImageOps.grayscale(image)
    arr = array(image.getcolors())
    print(arr.sum())
    return arr.sum()


def start(a, b, c, d):
    print("Starting Game.....")
    x = 0

    while x <= 65:
        if IMG(a, b, c, d) != 6558 and IMG(a, b, c, d) != 6780:
            pressSpace()
            x += 1
            print("     Jumping " + str(x) + " times")

    while x <= 85:
        if IMG(a, b, c + 100, d) != 11058 and IMG(a, b, c + 100, d) != 11280:
            pressSpace()
            x += 10
            print("     Jumping " + str(x) + " times")

    while x <= 485:
        if IMG(a, b, c + 150, d) != 13308 and IMG(a, b, c + 150, d) != 13530:
            pressSpace()
            x += 1
            print("     Jumping " + str(x) + " times")


if __name__ == "__main__":
    start(80, 405, 225, 450)
