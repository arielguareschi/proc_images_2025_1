import cv2
import numpy as np

# Carregar uma imagem
imagem = cv2.imread("cachorro.jpg")

# Verifica se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem!")
    exit()

# Exibir a imagem original
cv2.imshow("Imagem Original", imagem)
cv2.waitKey(0)

# Converter para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Exibir a imagem em escala de cinza
cv2.imshow("Imagem em Escala de Cinza", imagem_cinza)
cv2.waitKey(0)

# Redimensionar a imagem para 50% do tamanho original
largura = int(imagem.shape[1] * 0.5)
altura = int(imagem.shape[0] * 0.5)
dimensoes = (largura, altura)

imagem_redimensionada = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)

# Exibir a imagem redimensionada
cv2.imshow("Imagem Redimensionada", imagem_redimensionada)
cv2.waitKey(0)

# Separação de canais de cor (B, G, R)
b, g, r = cv2.split(imagem)

# Criando imagens onde apenas um canal está visível
imagem_azul = cv2.merge([b, np.zeros_like(g), np.zeros_like(r)])
imagem_verde = cv2.merge([np.zeros_like(b), g, np.zeros_like(r)])
imagem_vermelha = cv2.merge([np.zeros_like(b), np.zeros_like(g), r])

# Exibir os canais de cor individualmente
cv2.imshow("Canal Azul", imagem_azul)
cv2.imshow("Canal Verde", imagem_verde)
cv2.imshow("Canal Vermelho", imagem_vermelha)
cv2.waitKey(0)

# Salvando as imagens modificadas
cv2.imwrite("imagem_cinza.jpg", imagem_cinza)
cv2.imwrite("imagem_redimensionada.jpg", imagem_redimensionada)
cv2.imwrite("imagem_azul.jpg", imagem_azul)
cv2.imwrite("imagem_verde.jpg", imagem_verde)
cv2.imwrite("imagem_vermelha.jpg", imagem_vermelha)

print("Imagens processadas e salvas com sucesso!")

# Fechar todas as janelas abertas
cv2.destroyAllWindows()
