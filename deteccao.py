import cv2
import numpy as np
import os
import serial

porta = "COM3"
velocidade = 9600

conexao = serial.Serial(porta, velocidade)
cap = cv2.VideoCapture(0)
kernel = np.ones((5 ,5), np.uint8)
v='0'
while True:
    v = '0'
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([110, 50, 50])
    upper_red = np.array([130, 255, 255])
    lower_yellow = np.array([25,65,65])
    upper_yellow = np.array([32,255,255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    opening = cv2.morphologyEx(mask_red, cv2.MORPH_OPEN, kernel)
    opening2 = cv2.morphologyEx(mask_yellow, cv2.MORPH_OPEN, kernel)
    a, b, c, d = cv2.boundingRect(opening2)
    x, y, w, h = cv2.boundingRect(opening)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (240, 100, 100), 3)
    cv2.rectangle(frame, (a, b), (a + c, b + d), (30, 255, 255), 3)
    cv2.imshow('frame', frame)
    if a!=0 :
        v='1'
    if x!=0:
        v='2'
    if a!=0 and x!=0:
        v='3'
!!
    conexao.write((v).encode())
    print(v)


    #cv2.imshow('vermelho', mask_red)
    #cv2.imshow('amarelo', mask_yellow)
    key = cv2.waitKey(1)
    if key == 27:
        break

k = cv2.waitKey(5) & 0xFF
cv2.destroyAllWindows()
cap.release()
conexao.close()
