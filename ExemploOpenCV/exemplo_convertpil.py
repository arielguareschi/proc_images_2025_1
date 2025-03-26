#exemplo_convertpil
from PIL import Image
from PIL import ImageEnhance

# Carregar a imagem
imagem = Image.open("cachorro.jpg")
# Exibir a imagem

imagem.show()
imagem.save("imagem_convertida.bmp")

nova_imagem = imagem.resize((300, 400))
nova_imagem.show()

imagem_cinza = imagem.convert("L")
imagem_cinza.show()
imagem_cinza.save("imagem_cinza.bmp")

enhancer = ImageEnhance.Color(nova_imagem)
imagem_colorida = enhancer.enhance(2)
imagem_colorida.show()