#main_pillow
from PIL import Image

print(Image.__version__)

#Abrir a imagem
imagem = Image.open("cachorro.jpg")

#Mostrar a imagem
imagem.show()

#Salvar a imagem convertida
imagem.save("cachorro.png")
