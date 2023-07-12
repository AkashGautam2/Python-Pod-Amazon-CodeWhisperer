#import ImageEnhancer from main.py
import unittest
import cv2
import numpy as np
from main import ImageEnhancer
ImgObject=ImageEnhancer()
#Write test case to  test the functionality of the ImageEnhancer class
class TestResize(unittest.TestCase):
    def test_resize_image(self):
        img=cv2.imread('Flower.png')
        # np_array = np.frombuffer(img, np.uint8)
        # download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        height = 10
        width = 20

        result = ImgObject.resize_image(img, width, height)
        # print(codeheight,codewidth)
        self.assertIsNotNone(result[0])
        self.assertEqual(result[0].shape[0],height)
        self.assertEqual(result[0].shape[1],width)
        self.assertEqual(result[2], height)
        self.assertEqual(result[1], width)
    def test_crop(self):
        img = cv2.imread('Flower.png')
        np_array = np.frombuffer(img, np.uint8)
        download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        downloaded_img= ImgObject.crop(download_img)
        self.assertIsNotNone(downloaded_img)
    def test_brightness_increase(self):
        img = cv2.imread('Flower.png')
        np_array = np.frombuffer(img, np.uint8)
        download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        percentage = 10
        downloaded_img = ImgObject.brightness_increase(download_img, percentage)
        self.assertIsNotNone(downloaded_img)
    def test_brightness_decrease(self):
        img = cv2.imread('Flower.png')
        np_array = np.frombuffer(img, np.uint8)
        download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        percentage = 10
        downloaded_img = ImgObject.brightness_decrease(download_img, percentage)
        self.assertIsNotNone(downloaded_img)