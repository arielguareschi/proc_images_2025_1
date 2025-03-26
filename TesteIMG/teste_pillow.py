from PIL import Image

# Abrir a imagem
imagem = Image.open("exemplo.jpg")

# Mostrar a imagem
imagem.show()

# Salvar em outro formato
imagem.save("exemplo_convertido.png")
