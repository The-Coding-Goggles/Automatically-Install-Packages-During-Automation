import os

try:
    import cv2
except ImportError:
    os.system('pip install opencv-python')

import cv2