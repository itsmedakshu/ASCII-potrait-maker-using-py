# src/main.py
from image_utils import load_and_resize, to_grayscale, sobel_edges
from ascii_utils import grayscale_to_ascii, print_colored_ascii
from color_utils import rgb_to_hsv

def main():
    path = "ASCII_potrait/ascii_art_generator/test_images/example.png"
    img = load_and_resize(path, new_width=120)
    gray = to_grayscale(img)
    edges = sobel_edges(gray)
    hsv = rgb_to_hsv(img)
    ascii_img = grayscale_to_ascii(edges)
    print_colored_ascii(ascii_img, hsv)

if __name__ == "__main__":
    main()
