# OCR with Python, Tesseract, and OpenCV

This project demonstrates Optical Character Recognition (OCR) on images using Python, Tesseract, and OpenCV.

## Requirements
- Python
- OpenCV
- Tesseract

## Setup
1. Install the required packages:
    - Download and install Tesseract from [here](https://github.com/tesseract-ocr/tesseract).
2. Update the `tesseract_cmd` variable in `run.py` with the path to the Tesseract executable on your system.

## Usage
1. Place the image you want to perform OCR on in the `img` directory.
2. Update the `cv2.imread` function in `run.py` with the path to your image.
3. Run the script:

```bash
python run.py
```

The script will load the image, convert it to grayscale (optional, depending on the image), and then apply OCR using Tesseract. The resulting text will be printed to the console.

## Note
- The current script is set to recognize the Portuguese language. If you want to use another language, change the `lang` parameter in the `pytesseract.image_to_string` function to the appropriate language code. You can find the list of supported languages [here](https://github.com/tesseract-ocr/tesseract/wiki/Data-Files#data-files-for-version-400-november-29-2016).
  
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
