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
