# src/color_utils.py
import cv2
import numpy as np

def rgb_to_hsv(image):
    """Convert PIL Image (RGB) to HSV using OpenCV"""
    np_img = np.array(image)
    hsv_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2HSV)
    return hsv_img
