import pytesseract as pyt
import cv2
from gtts import gTTS
import os

# Set the Tesseract executable path
pyt.pytesseract.tesseract_cmd = "C:\\Users\\HP\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

# Read the image
img = cv2.imread("image.png")

# Extract text from the image
text = pyt.image_to_string(img)

# Display the extracted text
print("Extracted Text:")
print(text)

# Convert the extracted text to speech
if text.strip():  # Check if the text is not empty
    tts = gTTS(text=text, lang='en')  # Convert text to speech
    tts.save("output.mp3")  # Save the audio file
    print("Text-to-speech conversion complete. Playing audio...")
    os.system("start output.mp3")  # Play the audio file (for Windows)
else:
    print("No text found in the image.")

