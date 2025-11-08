# src/image_utils.py
from PIL import Image
import cv2
import numpy as np

def load_and_resize(path, new_width=100):
    img = Image.open(path).convert("RGB")
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # adjust for terminal aspect
    img = img.resize((new_width, new_height))
    return img

def to_grayscale(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

# src/image_utils.py (append)
def sobel_edges(gray_img):
    grad_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = cv2.magnitude(grad_x, grad_y)
    magnitude = np.uint8(np.clip(magnitude, 0, 255))
    return magnitude
