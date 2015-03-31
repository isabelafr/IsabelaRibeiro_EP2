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

def DesenhaBoneco (parte):                  
    import turtle              #inicio tartaruga 2
    tartaruga = turtle.Turtle()
    tartaruga.speed(5)
    tartaruga.color("orange")
    tartaruga.hideturtle()
    tartaruga.penup()
    if parte == 0:                #desenha cabeça
        tartaruga.setpos(-200,110)
        tartaruga.pendown()
        tartaruga.circle(20)


    

    elif parte == 1:            #desenha o corpo
        tartaruga.setpos(-200,110)
        tartaruga.pendown()
        tartaruga.left(270)
        tartaruga.forward(70)



    elif parte == 2:           #desenha um braço
            tartaruga.setpos(-200,90)
            tartaruga.pendown()
            tartaruga.left(340)
            tartaruga.forward(40)
    

    elif parte == 3:       #desenha outro braço
        tartaruga.setpos(-200,90)
        tartaruga.pendown()
        tartaruga.left(200)
        tartaruga.forward(40)
        

    elif parte == 4:      #desenha uma perna
        tartaruga.setpos(-200,40)
        tartaruga.pendown()
        tartaruga.left(300)
        tartaruga.forward(40)
    

    elif parte == 5:     #desenha a outra perna
        tartaruga.setpos(-200,40)
        tartaruga.pendown()
        tartaruga.left(240)
        tartaruga.forward(40)


def desenharboneco():    
    if erros == 1:
        DesenhaBoneco(erros-1)
    if erros == 2:
        DesenhaBoneco(erros-1)
    if erros == 3:
        DesenhaBoneco(erros-1)
    if erros == 4:
        DesenhaBoneco(erros-1)
    if erros == 5:
        DesenhaBoneco(erros-1)
    if erros == 6:
        DesenhaBoneco(erros-1)
        tartaruga.write("Você perdeu!")



####fazendo a forca 

import turtle
tartaruga = turtle.Turtle()
tartaruga.pu()
tartaruga.hideturtle()
tartaruga.setpos(-150,0)
tartaruga.pd()
for i in range (c):
    tartaruga.speed(5)
    tartaruga.color("black")
    tartaruga.penup()
    tartaruga.pendown()
    tartaruga.forward(20)
    tartaruga.penup()
    tartaruga.forward(5)
    


import turtle                 #inicio tartaruga 1
window = turtle.Screen()      #criar um janela para a tartaruga 
window.bgcolor("lightblue")
window.title("Jogo da Forca")


tartaruga = turtle.Turtle()
tartaruga.speed(5)
tartaruga.penup()
tartaruga.hideturtle()
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




digitadas = []
erros = 0
acertos = []
onde = []


a = ["A", "Â", "Á", "À", "Ã","á", "à", "â", "ã"]
e = ["E", "Ê", "É", "È", "é", "ê", "è"]
i = ["I", "Í", "Ì", "Î", "í", "ì", "î"]
o = ["O", "Ò", "Ó", "Ô", "Õ", "õ", "ô", "ó", "ò"]
u = ["U", "Ú", "Û", "Ù", "ú", "ù","û"]
c = ["Ç","ç"]





while erros < 6:
    
    l = str(window.textinput("Chute", "Chute uma letra:"))
    for i in range(len(pcchoice)-1):
             if l  == pcchoice[i]:
                 onde.append(i)
                 import turtle
                 tartaruga = turtle.Turtle()
                 tartaruga.hideturtle()
                 tartaruga.setpos(-150 + 25*i,0)
                 tartaruga.write(l, font = ("Arial",24,"normal"))
    if l not in pcchoice:
                 print('aqui')
                 erros+=1
                 desenharboneco()






    

######################################




    



window.exitonclick()





