import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Carrega o modelo de detecção de objetos do TensorFlow Hub (EfficientDet)
modelo = hub.load("https://tfhub.dev/tensorflow/efficientdet/lite2/detection/1")

# Lista de classes do COCO Dataset
CLASSES = [
    '???', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', '???',
    'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse',
    'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack',
    'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard',
    'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard',
    'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork',
    'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange',
    'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair',
    'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv',
    'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave',
    'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase',
    'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]

# Função auxiliar para carregar e redimensionar a imagem
def carregar_imagem(path):
    img = cv2.imread(path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (320, 320))
    img_tensor = tf.convert_to_tensor(img_resized, dtype=tf.uint8)
    return img, tf.expand_dims(img_tensor, 0)  # original + versão para o modelo

# Caminho da imagem
img_path = 'imagem_exemplo.jpg'

# Carrega e prepara a imagem
img_original, img_input = carregar_imagem(img_path)

# Executa a detecção
result = modelo(img_input)
result = {key: value.numpy() for key, value in result.items()}

# Processa os resultados
caixas = result["detection_boxes"]
pontuacoes = result["detection_scores"]
classes = result["detection_classes"]

# Desenha os objetos detectados
altura, largura, _ = img_original.shape
for i in range(len(pontuacoes)):
    if pontuacoes[i] > 0.5:  # limiar de confiança
        y1, x1, y2, x2 = caixas[i]
        x1, x2 = int(x1 * largura), int(x2 * largura)
        y1, y2 = int(y1 * altura), int(y2 * altura)

        classe_id = int(classes[i])
        label = CLASSES[classe_id] if classe_id < len(CLASSES) else "desconhecido"

        # Desenha retângulo e texto
        cv2.rectangle(img_original, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img_original, f"{label} ({pontuacoes[i]*100:.1f}%)", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Exibe a imagem final
plt.figure(figsize=(10, 8))
plt.imshow(cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Objetos Reconhecidos com TensorFlow')
plt.show()
