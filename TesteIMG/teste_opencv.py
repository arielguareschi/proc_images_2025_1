import cv2

# Carregar uma imagem
imagem = cv2.imread("exemplo.jpg")

# Exibir a imagem
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
