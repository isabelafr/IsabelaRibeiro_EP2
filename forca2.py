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

                               #inicio do corpo

def cabeca ():                  
    import turtle              #inicio tartaruga 2
    tartaruga = turtle.Turtle()
    tartaruga.speed(5)
    tartaruga.penup()
    tartaruga.setpos(-200,110)
    tartaruga.pendown()
    tartaruga.color("orange")
    tartaruga.circle(20)

cabeca()
    
def tronco ():
    import turtle
    tartaruga = turtle.Turtle
    tartaruga.speed(5)
    tartaruga.penup()
    tartaruga.setpos(-200,70)
    tartaruga.pendown()
    tartaruga.color("orange")

angulo4 = 270
dist4 = 100

for i in range(1):
    tartaruga.left(angulo4)
    tartaruga.forward(dist4)

tronco()
     
window.exitonclick()



f= open("entrada.txt", encoding="utf-8")

