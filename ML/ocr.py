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

    test = Image.open(p_name)
    text=image_to_string(test)
    print(text)
    
    print(text)
    return text


