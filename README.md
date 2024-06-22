# IMAGE-TO-TEXT
Image Text Extraction with Tesseract OCR in Google Colab
This project demonstrates how to use Tesseract OCR in Google Colab to extract text from images. The project utilizes Python libraries such as pytesseract and opencv-python.

Setup
To run this project, you need to install the required dependencies and upload an image file to extract text from it.

Dependencies
Tesseract OCR
pytesseract
OpenCV
Install the dependencies  in Google Colab:

Usage
Import the required libraries:
Upload an image:
Use the files.upload() function to upload an image file from your local machine.
Read and display the image:

After uploading the image, read and display it using OpenCV.
Convert the image to grayscale:

Convert the uploaded image to grayscale to prepare it for text extraction.
Extract text from the image:

Use Tesseract OCR to extract text from the grayscale image.

python
