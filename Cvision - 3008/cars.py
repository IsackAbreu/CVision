# Importando as bibliotecas
from re import I
import cv2
import time
import numpy as np

#criar classificador de carro
classify_car = cv2.CascadeClassifier('./hscd/cars.xml')

#pega um video cm carro 
vid_capture = cv2.VideoCapture('./ideo/cars_moving.mp4')

#loop do codigo
while vid_capture.isOpened():

    #ler fames
    ret, frame = vid_capture.read()

    #preto e brnco
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars_detected = classify_car.detectMultiScale(grayscale_img, 1.4, 2)
    cv2.imshow('carros', frame)

    cv2.imshow('carros', frame)
    # desenhando retangulos
    for (x,y,w,h) in cars_detected:
        cv2.rectangle(frame, (x,y), (x+w, y+w), (0, 255, 0), 2)
        cv2.imshow('carros', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid_capture.release()
cv2.destroyAllWindows()