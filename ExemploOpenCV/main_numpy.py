#main_numpy
#pip install numpy
import numpy as np
import cv2

print(np.__version__)

# Criar uma imagem de 256x256 pixels com cores aleatórias
imagem = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
print(imagem)
# Exibir a imagem
cv2.imshow("Imagem Aleatória", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
