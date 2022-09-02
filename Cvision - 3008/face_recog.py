#Importando Bibliotecas
from tabnanny import check
import cv2
from tkinter import messagebox

#Setando WEBCAM
video = cv2.VideoCapture(0)

#Classificadores XML DE ROSTO
classify_face = cv2.CascadeClassifier('./hscd/frontal_face.xml')

#Classificadores XML de OLHO
classify_eye = cv2.CascadeClassifier('./hscd/eye.xml')

first_read = True
blink = False
eye_loc = False
txt1 = True

#Enquanto verdadeiro, rola o código
while True:

    #lê WEBCAM
    check, img = video.read()

    #Diminui tamanho do vídeo
    img = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)

    #lê em preto e branco
    grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detectar ROSTO
    faces_detected = classify_face.detectMultiScale(grayscale_img, 1.2, 3)

    #detectar OLHO
    eye_detected = classify_eye.detectMultiScale(grayscale_img, 1.2, 3)

    #ABRIR JANELA 
    cv2.imshow("img",img)

    #se detectar o rosto
    if (len(faces_detected) >= 1):
        if txt1 == True:
            cv2.putText(img,"Rosto encontrado, pisque o olho",(60,70),
            cv2.FONT_HERSHEY_PLAIN, 2,(0,255,0),2)
        else:
            cv2.putText(img,"Checando Morador...",(60,70),
            cv2.FONT_HERSHEY_PLAIN, 2,(0,255,0),2)
    else:
        cv2.putText(img,"Procurando rosto...",(80,70),
        cv2.FONT_HERSHEY_PLAIN, 3,(0,255,255),2)
        cv2.imshow("img",img)

        #se detectar o olho
    if(len(eye_detected)>=2):

        eye_loc = True

        if(first_read):
            cv2.putText(img,"Olhos detectados", (70,400),cv2.FONT_HERSHEY_PLAIN, 2,(255,255,255),2)
        else:
            cv2.putText(img,"Olhos abertos", (70,400),cv2.FONT_HERSHEY_PLAIN, 2,(255,255,255),2)

    else:

        if(first_read) and eye_loc == True:
            cv2.putText(img,"Piscou", (70,400),cv2.FONT_HERSHEY_PLAIN, 2,(0,0,255),2)
            txt1 = False
            blink = True

    #DESENHAR RETÂNGULOS onde achar ROSTOS
    for (x, y, w, h) in faces_detected:

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 139), 2)
        cv2.imshow("img",img)
        roi_face_clr = img[y:y+h,x:x+w]
        roi_face = grayscale_img[y:y+h,x:x+w]

    print (blink)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if blink == True:
        pass

video.release()
cv2.destroyAllWindows()