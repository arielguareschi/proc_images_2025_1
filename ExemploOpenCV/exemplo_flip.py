#exemplo_flip
import cv2

# imagem = cv2.imread("cachorro.jpg")
# imagem_horizontal = cv2.flip(imagem, 1)
# imagem_vertical = cv2.flip(imagem, 0)
# imagem_cabalhota = cv2.flip(imagem, -1)
#
# cv2.imshow("imagem original", imagem)
# cv2.imshow("imagem horizontal", imagem_horizontal)
# cv2.imshow("imagem vertical", imagem_vertical)
# cv2.imshow("imagem cabalhota", imagem_cabalhota)
#
# imagem_cortada = imagem[100:350, 100:350]
# cv2.imshow("imagem cortada", imagem_cortada)

imagem_pequena = cv2.imread("cachorro_pequeno.jpg")
cv2.imshow("imagem pequena", imagem_pequena)
novo_tamanho = (int(imagem_pequena.shape[1] * 4),
                int(imagem_pequena.shape[0] * 4))
imagem_linear = cv2.resize(imagem_pequena, novo_tamanho,
                           interpolation=cv2.INTER_LINEAR)
imagem_cubica = cv2.resize(imagem_pequena, novo_tamanho,
                           interpolation=cv2.INTER_CUBIC)
imagem_lanczos4 = cv2.resize(imagem_pequena, novo_tamanho,
                             interpolation=cv2.INTER_LANCZOS4)

cv2.imshow("imagem lanczos4", imagem_lanczos4)
cv2.imshow("imagem cubica", imagem_cubica)
cv2.imshow("imagem_linear", imagem_linear)


cv2.waitKey(0)
cv2.destroyAllWindows()