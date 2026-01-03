from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    import matplotlib.pyplot as plt

    penguin1 = Image.open('penguin1.jpg')
    penguin1 = np.array(penguin1)

    plt.figure(figsize = (6,4))
    plt.imshow(penguin1)

    gray_penguin1 = np.mean(penguin1, axis = 2)
    plt.figure(figsize = (6,4))
    plt.imshow(gray_penguin1, cmap = 'gray')
    
def edge_detection(image):
    kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

    filtered_image = convolve2d(gray_penguin1, kernel, mode='same')
    edge_detected = np.absolute(filtered_image)
    plt.figure(figsize=(8, 4))
    plt.imshow(edge_detected, cmap='gray')
    plt.show()
