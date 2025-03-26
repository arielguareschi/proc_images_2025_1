#exemplo_convertcv
import cv2
# Carregar a imagem do disco
imagem = cv2.imread("cachorro.jpg")
# Verificar se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem. Verifique o caminho.")
else:
    largura, altura = 300, 200
    imagem_redimensionada = cv2.resize(imagem, (largura, altura))

    # Exibir a imagem
    # cv2.imshow("Imagem", imagem)
    cv2.imshow("Imagem redimensionada", imagem_redimensionada)
    # Aguarda o pressionamento de qualquer tecla para fechar

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("imagem_convertida.png", imagem)
    print("Imagem salva como PNG!")
    #escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Escala de Cinza", imagem_cinza)
    cv2.imwrite("imagem_cinza.jpg", imagem_cinza)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # ficar soh o vermelho
    b, g, r = cv2.split(imagem_redimensionada)
    # Criando uma imagem somente com o canal vermelho
    imagem_vermelha = cv2.merge([b * 0, g * 0, r])
    cv2.imshow("Imagem Vermelha", imagem_vermelha)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    imagem_azul = imagem_redimensionada.copy()
    imagem_azul[:, :, 1] = 0  # Remove o verde
    imagem_azul[:, :, 2] = 0  # Remove o vermelho

    cv2.imshow("Imagem Azul", imagem_azul)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
