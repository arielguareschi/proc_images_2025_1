from ultralytics import YOLO
import cv2
import urllib.request
import numpy as np

# Baixa uma imagem
url = 'https://ultralytics.com/images/bus.jpg'
resp = urllib.request.urlopen(url)
image_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)
imagem = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

# Converte para RGB (YOLO trabalha com RGB)
imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# Carrega o modelo pré-treinado (nano = mais leve e rápido)
model = YOLO('yolov8x.pt')

# Detecta objetos
results = model(imagem_rgb)
result = results[0]

# Exibe os objetos detectados
for box in result.boxes:
    classe = int(box.cls[0])
    label = result.names[classe]
    conf = float(box.conf[0])
    print(f'{label} (confiança: {conf:.2%})')

# Gera a imagem com as anotações
img_result = result.plot()

# Salva e exibe
cv2.imwrite('resultado.jpg', cv2.cvtColor(img_result, cv2.COLOR_RGB2BGR))
cv2.imshow('Resultado da Detecção', img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
