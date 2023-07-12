import unittest
import cv2
import numpy as np
from main import ImageProcessor
ImgObject=ImageProcessor()
# Write test case to  test the functionality of the ImageEnhancer class
class TestImage(unittest.TestCase):
    #Test case for resize function
    def test_resize_image(self):
        img = cv2.imread('1.jpeg')
        height = 20
        width = 20
        result = ImgObject.Resize(img, width, height)
        self.assertIsNotNone(result[0])
        shape0 = result[0].shape[0]
        shape1 = result[0].shape[1]
        result1 = result[1]
        result2 = result[2]
        self.assertEqual(shape0, height)
        self.assertEqual(shape1, width)
        self.assertEqual(result1, width)
        self.assertEqual(result2, height)
    #Test case for crop function
    def test_crop(self):
        img = cv2.imread('1.jpeg')
        np_array = np.frombuffer(img, np.uint8)
        download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        downloaded_img = ImgObject.crop(img)
        self.assertIsNotNone(img)
    #Test case for brightness function
    def test_brightness(self):
        img = cv2.imread('1.jpeg')
        np_array = np.frombuffer(img, np.uint8)
        download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        perc = 10
        downloaded_img = ImgObject.Brightness(img, perc)
        self.assertIsNotNone(img)
    #Test case for contrast function
    def test_contrast(self):
        img = cv2.imread('1.jpeg')
        np_array = np.frombuffer(img, np.uint8)
        download_img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        percentage = 10
        downloaded_img = ImgObject.contrast(img, percentage)
        self.assertIsNotNone(img)
