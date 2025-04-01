#exemplo_ruidos
import cv2
img = cv2.imread('cachorro_pequeno.jpg')
cv2.imshow('Oliginal', img)
#
# blur = cv2.blur(img, (5,5))  # Janela de 5x5
# cv2.imshow('Blur', blur)
#
# gauss = cv2.GaussianBlur(img, (5,5), 0)
# cv2.imshow('Gaussian Blur', gauss)
#
# mediana = cv2.medianBlur(img, 5)
# cv2.imshow('Mediana', mediana)
#
# bi = cv2.bilateralFilter(img, 9, 75, 75)
# cv2.imshow('Bilateral', bi)

#Derivada na direcao X
# sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# #Derivada na direcao Y
# sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
# cv2.imshow('Sobelx', sobelx)
# cv2.imshow('Sobely', sobely)

# edges = cv2.Canny(img, 100, 200)
# cv2.imshow('Edges', edges)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255,
                          cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,
                               cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
cv2.imshow('Contornos', img)

adaptative = cv2.adaptiveThreshold(gray, 255,
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY,
                                   11, 2)
cv2.imshow('adaptative', adaptative)
contours, _ = cv2.findContours(adaptative, cv2.RETR_TREE,
                               cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
cv2.imshow('Contours', img)

cv2.waitKey(0)
