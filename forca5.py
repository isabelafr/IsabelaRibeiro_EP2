# -*- coding: utf-8 -*-
from random import choice

f = open("entrada (1).txt", encoding="utf-8")
lista = f.readlines()

def listafuncao(q):
    list[q].strip()
    
listalimpa = []

for n in lista:
    s = n.strip()
    listalimpa.append(s)
    
pcchoice = choice(listalimpa)
c = len(pcchoice)
print(pcchoice)




import turtle                 #inicio tartaruga 1
window = turtle.Screen()      #criar um janela para a tartaruga 
window.bgcolor("lightblue")
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
    
def corpo ():
    import turtle
    tartaruga = turtle.Turtle()
    tartaruga.speed(5)
    tartaruga.penup()
    tartaruga.setpos(-200,110)
    tartaruga.pendown()
    tartaruga.color("orange")
    tartaruga.left(270)
    tartaruga.forward(70)

corpo()

def braco1 ():
    import turtle 
    tartaruga = turtle.Turtle()
    tartaruga.speed(5)
    tartaruga.penup()
    tartaruga.setpos(-200,90)
    tartaruga.pendown()
    tartaruga.color("orange")
    tartaruga.left(340)
    tartaruga.forward(40)
    
braco1()

def braco2():
    import turtle
    tartaruga = turtle.Turtle()
    tartaruga.speed(5)
    tartaruga.penup()
    tartaruga.setpos(-200,90)
    tartaruga.pendown()
    tartaruga.color("orange")
    tartaruga.left(200)
    tartaruga.forward(40)
    
braco2()

def perna1():
    import turtle
    tartaruga = turtle.Turtle()
    tartaruga.speed(5)
    tartaruga.penup()
    tartaruga.setpos(-200,40)
    tartaruga.pendown()
    tartaruga.color("orange")
    tartaruga.left(300)
    tartaruga.forward(40)
    
perna1()

def perna2():
    import turtle
    tartaruga = turtle.Turtle()
    tartaruga.speed(5)
    tartaruga.penup()
    tartaruga.setpos(-200,40)
    tartaruga.pendown()
    tartaruga.color("orange")
    tartaruga.left(240)
    tartaruga.forward(40)
    
perna2()

def morte():
    import turtle 
    tartaruga = turtle.Turtle()
    tartaruga.speed(5)
    tartaruga.penup()
    tartaruga.setpos(-250,110)
    tartaruga.pendown()
    tartaruga.color("red")
    tartaruga.left(0)
    tartaruga.forward(100)
    
morte()
    
    
    
    
window.exitonclick()




