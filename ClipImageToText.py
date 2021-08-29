from PIL import ImageGrab
import pytesseract as tess
import clipboard
from pynput import keyboard

# importing tesseract OCR as pytesseract is just a python wrapper for it.

# Downloading Tesseract OCR is required to use this application as that's how
# It converts images to text. Installation instructions are in the Readme.

# Tesseract OCR Default installs to Program Files/Program Files (x86)

# You may need to modify the first line of code below to find where 
# tesseract.exe is installed on your machine.

# Change this line depending on tesseract download location and system!
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def clipboardToText():
  text = ''

  im = ImageGrab.grabclipboard()

  try:
    text = tess.image_to_string(im)
  except:
    pass

  if text == '':
    # Nothing Captured
    print('Unable to parse any text.')
    pass
  else:
    print('Successful text conversion!')
    # Capture Succesful
    clipboard.copy(text)

# Change to whatever shortcut combination you desire
COMBINATIONS = [
  {keyboard.Key.shift, keyboard.KeyCode(char='`')},
  {keyboard.Key.shift, keyboard.KeyCode(char='~')}
]