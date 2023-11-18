import cv2 as cv
import numpy as np

# Valor RGB da cor desejada (#0F5579)
cor_desejada_rgb = np.array([15, 85, 121], dtype=np.uint8)

# Carregue a imagem de origem
imagem_origem = cv.imread('origemslime.jpg', cv.IMREAD_UNCHANGED)

# Verifique se a imagem foi carregada corretamente
if imagem_origem is None:
    print('Erro ao carregar a imagem.')
    exit()

# Converta a imagem para o espaço de cor HSV
imagem_hsv = cv.cvtColor(imagem_origem, cv.COLOR_BGR2HSV)

# Defina os limites inferior e superior para a cor desejada no espaço HSV
limite_inferior = np.array([90, 50, 50], dtype=np.uint8)
limite_superior = np.array([110, 255, 255], dtype=np.uint8)

# Aplique a máscara para obter apenas os pixels na faixa de cores desejada
mascara = cv.inRange(imagem_hsv, limite_inferior, limite_superior)

# Encontre os contornos na máscara
contornos, _ = cv.findContours(mascara, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

# Desenhe os contornos na imagem de origem
cv.drawContours(imagem_origem, contornos, -1, (0, 255, 0), 2)

# Mostre a imagem resultante
cv.imshow('Rastreamento de Cor', imagem_origem)
cv.waitKey(0)
cv.destroyAllWindows()
