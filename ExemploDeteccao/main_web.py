#main_web.py
from ultralytics import YOLO
import cv2
import urllib.request
import numpy as np

#Baixa um imagem
url = 'https://ultralytics.com/images/bus.jpg'
resp = urllib.request.urlopen(url)
imagem_array = np.asarray(bytearray(resp.read()), dtype=np.uint8)
imagem = cv2.imdecode(imagem_array, cv2.IMREAD_COLOR)

imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

model = YOLO('yolov8n.pt')

resultados = model(imagem_rgb)
resultado = resultados[0]

for box in resultado.boxes:
    classe = int(box.cls[0])
    label = resultado.names[classe]
    conf = float(box.conf[0])
    print(f'{label} - (Confiança: {conf:.2f})')

img_result = resultado.plot()

cv2.imwrite('resultados.jpg',
            cv2.cvtColor(img_result, cv2.COLOR_RGB2BGR))
cv2.imshow('Resultado', img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()