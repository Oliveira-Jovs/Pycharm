import cv2

# Carregar a imagem
image = cv2.imread('IMG_20220713_201304.jpg')

if image is None:
    print('Não foi possível carregar a imagem.')
else:
    # Exibir a imagem em uma janela
    cv2.imshow('Imagem', image)

    # Aguardar até que uma tecla seja pressionada
    cv2.waitKey(0)

    # Fechar a janela
    cv2.destroyAllWindows()
