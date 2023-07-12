# import ImageEnhancer from main.py
import unittest
import cv2
import numpy as np
from main import ImageEditor
ImgObject=ImageEditor()
# Write test case to  test the functionality of the ImageEnhancer class
class TestResize(unittest.TestCase):
    def test_resize_image(self):
        img = cv2.imread('1.png')
        height = 100
        width = 100

        result = ImgObject.resize(img, width, height)
        self.assertIsNotNone(result[0])
        self.assertEqual(result[0].shape[0], height)
        self.assertEqual(result[0].shape[1], width)

    def test_crop(self):
        img = cv2.imread('1.png')
        np_array = np.frombuffer(img, np.uint8)
        download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        downloaded_img = ImgObject.crop(img)
        self.assertIsNotNone(img)

    def test_brightness(self):
        img = cv2.imread('1.png')
        np_array = np.frombuffer(img, np.uint8)
        download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        perc = 10
        downloaded_img = ImgObject.Brightness(img, perc)
        self.assertIsNotNone(img)

    def test_contrast(self):
        img = cv2.imread('1.png')
        np_array = np.frombuffer(img, np.uint8)
        download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        percentage = 10
        downloaded_img = ImgObject.contrast(img, percentage)
        self.assertIsNotNone(img)
