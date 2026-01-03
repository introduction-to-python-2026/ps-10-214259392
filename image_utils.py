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

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from skimage.filters import median
from skimage.morphology import ball
# ייבוא הפונקציות מהקובץ שיצרנו
from image_utils import load_image, edge_detection

# 1. טעינת התמונה
original_image = load_image('penguin1.jpg') 

# 2. ניקוי רעשים באמצעות Median Filter
# הפילטר מקבל את התמונה המקורית וכדור ברדיוס 3
clean_image = median(original_image, ball(3))

# 3. הרצת זיהוי קצוות על התמונה הנקייה
edgeMAG = edge_detection(clean_image)

# 4. המרה למערך בינארי (Thresholding)
# בחרי ערך סף (Threshold) לפי ההיסטוגרמה (למשל 50)
threshold_value = 50 
edge_binary = edgeMAG > threshold_value

# 5. הצגת התוצאה ושמירה
plt.figure(figsize=(10, 5))
plt.imshow(edge_binary, cmap='gray')
plt.title("Binary Edge Detection Output")
plt.axis('off')
plt.show()

# שמירה כקובץ PNG
edge_image = Image.fromarray((edge_binary * 255).astype(np.uint8))
edge_image.save('my_edges.png')
