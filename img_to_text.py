!sudo apt-get install tesseract-ocr
!pip install pytesseract
!pip install opencv-python

import pytesseract
from google.colab.patches import cv2_imshow
import cv2

from google.colab import files
uploaded = files.upload()

for fn in uploaded.keys():
  img_path = fn

img=cv2.imread(img_path)
cv2_imshow(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text=pytesseract.image_to_string(gray)
print("EXTRACTED TEXT:")
print(text)

