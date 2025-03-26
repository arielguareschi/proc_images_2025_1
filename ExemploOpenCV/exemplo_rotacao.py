#exemplo_rotacao
import cv2
import numpy as np
import matplotlib.pyplot as plt

imagem = cv2.imread("cachorro.jpg")
# Obtém dimensões da imagem
altura, largura = imagem.shape[:2]
# Define o centro da imagem para rotação
centro = (largura // 2, altura // 2)
# Gera a matriz de rotação (ângulo de 45°)
matriz_rotacao = cv2.getRotationMatrix2D(centro, 72, 1.0)
# Aplica a rotação
imagem_rotacionada = cv2.warpAffine(imagem, matriz_rotacao,
                                    (largura, altura))
# Converte para RGB e exibe a imagem rotacionada
plt.imshow(cv2.cvtColor(imagem_rotacionada, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
