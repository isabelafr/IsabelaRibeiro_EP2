# -*- coding: utf-8 -*-

import turtle                 #inicio tartaruga 1
window = turtle.Screen()      #criar um janela para a tartaruga 
window.bgcolor("blue")
window.title("Jogo da Forca")


tartaruga = turtle.Turtle()
tartaruga.speed(5)
tartaruga.penup()
tartaruga.setpos(-300,0)     #posição inicial da tartaruga
tartaruga.pendown()
tartaruga.color("black")     #cor da tartaruga

dist = 200
angulo = 90

for i in range (1):
    tartaruga.left(angulo)
    tartaruga.forward(dist)
    
angulo2 = 270
dist2 = 100

for i in range (1):
    tartaruga.left(angulo2)
    tartaruga.forward(dist2)

angulo3 = 270
dist3 = 50

for i in range (1):
    tartaruga.left(angulo3)
    tartaruga.forward(dist3)   #fim tartaruga 1


import turtle                  #inicio tartaruga 2
tartaruga = turtle.Turtle()
tartaruga.speed(5)
tartaruga.penup()
tartaruga.setpos(-270,0)
tartaruga.pendown()
tartaruga.color("black")


dist4 = 50
angulo4 = 0 

for i in range (1):            #número de letras!!
     tartaruga.left(angulo4)
     tartaruga.forward(dist4)


window.exitonclick()



f= open("entrada.txt", encoding="utf-8")

