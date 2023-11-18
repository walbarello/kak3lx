import cv2 as cv
import numpy as np

# Imagem maior (imagem na qual você deseja procurar padrões)
imagem_origem = cv.imread('origemslime.jpg', cv.IMREAD_UNCHANGED)

# Imagem menor (modelo que você está tentando encontrar na imagem maior)
modelo_slime = cv.imread('157_7.jpg', cv.IMREAD_UNCHANGED)

# Certifique-se de que as imagens foram carregadas corretamente
if imagem_origem is None or modelo_slime is None:
    print("Erro ao carregar as imagens.")
    exit()

# Realize a correspondência de modelos usando cv.matchTemplate
resultado = cv.matchTemplate(imagem_origem, modelo_slime, cv.TM_CCOEFF_NORMED)

# Obtenha a posição do melhor match
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(resultado)
print('Melhor posição superior esquerda: %s' % str(max_loc))
print('Confiança do melhor match: %s' % max_val)

limiar = 0.8
if max_val >= limiar:
    print('Encontrado Slime.')

    # Obtenha o tamanho da imagem do slime
    h, w = modelo_slime.shape[:-1]

    # Calcule o canto inferior direito do retângulo a ser desenhado
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Desenhe um retângulo na imagem original onde o modelo foi encontrado
    cv.rectangle(imagem_origem, top_left, bottom_right,
                 color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

    # Salve a imagem resultante
    cv.imwrite('result.jpg', imagem_origem)

    # Exiba a imagem com o retângulo
    cv.imshow('Resultado', imagem_origem)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print('Slime não encontrado.')
