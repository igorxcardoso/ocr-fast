import cv2
import pytesseract

# Configurar o caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"  # Atualize com o caminho real no seu sistema

# Carregar a imagem usando o OpenCV
image = cv2.imread('img/imagem5.png')

# Converter a imagem para escala de cinza (opcional, dependendo da imagem)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar OCR usando pytesseract
text = pytesseract.image_to_string(gray_image, lang='por')

# Exibir o texto resultante
print(text)
