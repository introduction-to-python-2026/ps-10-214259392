import numpy as np
from PIL import Image
from scipy.signal import convolve2d

def load_image(file_path):
    # טעינה והמרה למערך
    img = Image.open(file_path)
    return np.array(img)

def edge_detection(image_array):
    # 1. המרה לגווני אפור (ממוצע ערוצים)
    gray_image = np.mean(image_array, axis=2)
    
    # 2. פילטרים לפי הדרישות
    filter_v = np.array([[1, 1, 1],
                         [0, 0, 0],
                         [-1, -1, -1]])
    
    filter_h = np.array([[1, 0, -1],
                         [1, 0, -1],
                         [1, 0, -1]])
    
    # 3. קונבולוציה עם zero padding
    edgeX = convolve2d(gray_image, filter_h, mode='same')
    edgeY = convolve2d(gray_image, filter_v, mode='same')
    
    # 4. חישוב Magnitude
    edgeMAG = np.sqrt(np.square(edgeX) + np.square(edgeY))
    
    return edgeMAG
