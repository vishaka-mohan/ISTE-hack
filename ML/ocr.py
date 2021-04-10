import cv2
import pytesseract
from pytesseract import image_to_string
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
import os
import pathlib

def readText():


    directory = pathlib.Path.cwd()
    p_name = (os.path.join(directory, "images/test.png"))


    text=image_to_string(Image.open(p_name))

    print(text)
    return text


