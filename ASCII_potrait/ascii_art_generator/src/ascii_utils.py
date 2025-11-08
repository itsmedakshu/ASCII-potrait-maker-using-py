# src/ascii_utils.py
import numpy as np
import cv2
ASCII_CHARS = "@%#*+=-:. "

def grayscale_to_ascii(gray_img):
    """Map grayscale image pixels to ASCII characters."""
    ascii_img = []
    scale = len(ASCII_CHARS) - 1
    for row in gray_img:
        line = "".join(ASCII_CHARS[pixel * scale // 255] for pixel in row)
        ascii_img.append(line)
    return ascii_img

# src/ascii_utils.py (append)
def print_colored_ascii(ascii_img, hsv_img):
    h, s, v = cv2.split(hsv_img)
    for y, line in enumerate(ascii_img):
        row = ""
        for x, ch in enumerate(line):
            hue = int(h[y, x] * 2)  # 0–360
            sat = s[y, x] / 255
            val = v[y, x] / 255
            r, g, b = hsv_to_rgb(hue, sat, val)
            row += f"\033[38;2;{r};{g};{b}m{ch}\033[0m"
        print(row)

def hsv_to_rgb(h, s, v):
    import colorsys
    r, g, b = colorsys.hsv_to_rgb(h / 360, s, v)
    return int(r * 255), int(g * 255), int(b * 255)
