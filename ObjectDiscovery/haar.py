import cv2

# Carrega o classificador treinado (Haar Cascade para rosto)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Lê a imagem
img = cv2.imread('resultado.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converte para escala de cinza

# Detecta rostos
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Desenha retângulos ao redor dos rostos detectados
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Detecta olhos
eyes = eye_cascade.detectMultiScale(gray)

for (ex, ey, ew, eh) in eyes:
    cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)


# Exibe a imagem
cv2.imshow('Rostos detectados', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
