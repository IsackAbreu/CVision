# Importando as bibliotecas
from tabnanny import check
from re import I
import cv2
import time
import numpy as np

# criando um classificador de corpo
classify_body = cv2.CascadeClassifier('./hscd/haarcascade_fullbody.xml')

# usando video pra teste
vid_capture = cv2.VideoCapture('./ideo/people_walking.mp4')

# LOOP DO CÒDIGO
while vid_capture.isOpened():
    
    

    check, img = vid_capture.read()

    #
    ret, frame = vid_capture.read()

    #
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5,
                       interpolation=cv2.INTER_LINEAR)

    # PRETO E BRANCO

    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #
    bodies_detected = classify_body.detectMultiScale(grayscale_img, 1.2, 3)

    
    cv2.imshow('Aqui estao os pedestres!', frame)
    
    for (x, y, w, h) in bodies_detected:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.imshow('Aqui estao os pedestres!', frame)

    #
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid_capture.release()
cv2.destroyAllWindows()
