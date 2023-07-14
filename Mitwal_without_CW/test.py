#import ImageEnhancer from main.py
import unittest
import cv2
import numpy as np
from main import ImageEnhancer
from PIL import Image

ImgObject=ImageEnhancer()
class TestResize(unittest.TestCase):
    # Write test case to  test the functionality of the resize_image function
    def test_resize_image(self):
        img=cv2.imread('Flower.png')
        # np_array = np.frombuffer(img, np.uint8)
        # download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        height = 10
        width = 20
        result = ImgObject.resize_image(img, width, height)
        self.assertIsNotNone(result[0])
        self.assertEqual(result[0].shape[0],height)
        self.assertEqual(result[0].shape[1],width)
        self.assertEqual(result[2], height)
        self.assertEqual(result[1], width)

    # Write test case to  test the functionality of crop function
    def test_crop(self):
        img = cv2.imread('Flower.png')
        np_array = np.frombuffer(img, np.uint8)
        download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        downloaded_img= ImgObject.crop(download_img)
        self.assertIsNotNone(downloaded_img)

    # Write test case to  test the functionality of the brightness_increase function
    def test_brightness_increase(self):
        img = cv2.imread('Flower.png')
        img2 = Image.open('Flower.png')
        npimg = np.array(img2)
        np_array = np.frombuffer(img, np.uint8)
        download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        percentage = 10
        downloaded_img = ImgObject.brightness_increase(download_img, percentage)
        npimg2 = np.array(downloaded_img)
        self.assertEquals(npimg.all(), npimg2.all())
        self.assertIsNotNone(img)
        self.assertIsNotNone(downloaded_img)

    # Write test case to  test the functionality of the contrast function
    def contrast(self):
        img = cv2.imread('Flower.png')
        img2 = Image.open('Flower.png')
        npimg = np.array(img2)
        np_array = np.frombuffer(img, np.uint8)
        download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        percentage = 10
        downloaded_img = ImgObject.contrast(download_img, percentage)
        npimg2 = np.array(downloaded_img)
        self.assertEquals(npimg.all(), npimg2.all())
        self.assertIsNotNone(img)
        self.assertIsNotNone(downloaded_img)