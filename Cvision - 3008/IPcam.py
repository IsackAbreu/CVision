#Importando Bibliotecas
from tabnanny import check
import cv2

#Setando vídeo
video = cv2.VideoCapture()

#Pegando ip da câmera
ip = "https://192.168.1.101:8080/video"
video.open(ip)

#Classificadores XML
classify_body = cv2.CascadeClassifier('./hscd/haarcascade_fullbody.xml')
classify_car = cv2.CascadeClassifier('./hscd/wcars.xml')

#Enquanto verdadeiro, rola o código
while True:

    #lê video
    check, img = video.read()


    #Diminui tamanho do vídeo
    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

    #lê em preto e branco
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detectar carro e corpo
    bodies_detected = classify_body.detectMultiScale(grayscale_img, 1.2, 3)
    cars_detected = classify_car.detectMultiScale(grayscale_img, 1.4, 2)

    if bodies_detected != ():
        print("TEM UMA PESSOA MEUDEUS KKJJHUGDUDHBSXUYHBWYBDYWSGDHSYD")

    #ABRIR JANELA 
    cv2.imshow("img",img)

    #DESENHAR RETÂNGULOS ONDE ACHAR CARROS E PESSOAS
    for (x, y, w, h) in bodies_detected:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow("img",img)

    for (x,y,w,h) in cars_detected:
        cv2.rectangle(img, (x,y), (x+w, y+w), (0, 255, 0), 2)
        cv2.imshow("img", img)


    #APERTAR "q" PRA SAIR
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()