#main

from PIL import Image
import pytesseract
from pdf2image import convert_from_path

imagem = Image.open("exemplo_ocr.jpg")
texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)

imagens = convert_from_path("Mussum Ipsum.pdf")
for i, img in enumerate(imagens):
    img.save(f"paginas/pagina{i}.jpg", 'JPEG')
    print(f"Pagina {i} salva como imagem")

