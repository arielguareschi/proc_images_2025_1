#exemploplt.py

import cv2
import matplotlib.pyplot as plt
# Carrega a imagem do disco
imagem = cv2.imread("cachorro.jpg")
# Converte de BGR para RGB
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
# Exibe a imagem
plt.imshow(imagem_rgb)
plt.axis("off")  # Remove os eixos da imagem
plt.show()


