# main.py
import cv2
print(cv2.__version__)

# Carregar uma imagem
imagem = cv2.imread("cachorro.jpg")

# Exibir a imagem
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()