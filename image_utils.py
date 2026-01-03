from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    img = Image.open(file_path)
    return np.array(img)
    
def edge_detection(image):
   gray_image = np.mean(image_array, axis=2)
    
    filter_v = np.array([[1, 1, 1],
                         [0, 0, 0],
                         [-1, -1, -1]])

    filter_h = np.array([[1, 0, -1],
                         [1, 0, -1],
                         [1, 0, -1]])
    
    edgeX = convolve2d(gray_image, filter_h, mode='same')
    edgeY = convolve2d(gray_image, filter_v, mode='same')
    
    # $$edgeMAG = \sqrt{edgeX^2 + edgeY^2}$$
    edgeMAG = np.sqrt(np.square(edgeX) + np.square(edgeY))
    
    return edgeMAG

