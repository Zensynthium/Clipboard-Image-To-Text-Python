# Clipboard-Image-To-Text-Python
A small Python application that converts images in your clipboard to text all with the use of one key combination! This is especially useful when used in conjunction with snipping tools ( **[ Win + Shift + S ]** on Windows ). It Can be ran using the ClipToTextHokey file as a .py for print feedback or a .pyw so it runs in the background out of sight. Leverages Tesseract OCR (Optical Character Recognition) developed by Google as an open source repository.

Since it uses Tesseract OCR, it's going to need to be downloaded on your system for this application to function properly. 

Default shortcut to convert clipboard images to text is **[ Shift + ` ]** / **[ Shift + ~ ]**, but can be changed in the ClipImageToText.py file.

**Tesseract Repository (Linux Binaries):**
https://github.com/tesseract-ocr/tesseract/releases

**Windows Installer:**
https://github.com/UB-Mannheim/tesseract/wiki

**Mac Instructions:**
https://formulae.brew.sh/formula/tesseract

You will likely have to either use a package manager or build from source. Cygwin is mentioned as a possible package manager, but I also found this link online which utilizes the package manager brew.

**Tesseract OCR Docs:**
https://github.com/tesseract-ocr/tessdoc

# License
MIT
Copyright (c) Zensynthium