#Isabela Frederico Ribeiro


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

def desenhaforca():
    import turtle                #inicio dos tracinhos
    tartaruga = turtle.Turtle()
    tartaruga.hideturtle()
    tartaruga.pu()
    tartaruga.setpos(-150,0)
    tartaruga.pd()
    for i in range (c):
        tartaruga.speed(5)
        tartaruga.color("black")
        tartaruga.penup()
        tartaruga.pendown()
        tartaruga.forward(20)
        tartaruga.penup()
        tartaruga.forward(5)     #fim dos tracinhos 
        
            
    
    
    import turtle                 #inicio tartaruga 1
    window = turtle.Screen()      #criar um janela para a tartaruga 
    window.bgcolor("lightblue")
    window.title("Jogo da Forca")
    
    
    tartaruga = turtle.Turtle()
    tartaruga.hideturtle()
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
def desenhaboneco(parametro):
    ####################
        #cabeça
        import turtle              #tartaruga 2
        tartaruga = turtle.Turtle()
        tartaruga.hideturtle()
        tartaruga.speed(5)
        tartaruga.color("orange")
        tartaruga.penup()
        if parametro == 0:
            tartaruga.setpos(-200,110)
            tartaruga.pendown()
            tartaruga.circle(20)
    
    
    #####################    
        #corpo
        import turtle             #tartaruga 3 
        tartaruga = turtle.Turtle()
        tartaruga.hideturtle()
        tartaruga.speed(5)
        tartaruga.color("orange")
        tartaruga.penup()
        if parametro == 1:
            tartaruga.setpos(-200,110)
            tartaruga.pendown()
            tartaruga.left(270)
            tartaruga.forward(70)
    
    
    ######################
        #braco1
        import turtle            #tartaruga 4 
        tartaruga = turtle.Turtle()
        tartaruga.hideturtle()
        tartaruga.speed(5)
        tartaruga.color("orange")
        tartaruga.penup()
        if parametro == 2:
            tartaruga.setpos(-200,90)
            tartaruga.pendown()
            tartaruga.left(340)
            tartaruga.forward(40)
    
    
    #######################
        #braco2
        import turtle           #tartaruga 5 
        tartaruga = turtle.Turtle()
        tartaruga.hideturtle()
        tartaruga.speed(5)
        tartaruga.penup()
        tartaruga.color("orange")
        if parametro == 3:
            tartaruga.setpos(-200,90)
            tartaruga.pendown()
            tartaruga.left(200)
            tartaruga.forward(40)
        
    
    
    ########################
        #perna1
        import turtle          #tartaruga 6 
        tartaruga = turtle.Turtle()
        tartaruga.hideturtle()
        tartaruga.speed(5)
        tartaruga.penup()
        if parametro == 4:
            tartaruga.setpos(-200,40)
            tartaruga.pendown()
            tartaruga.left(300)
            tartaruga.forward(40)
        
    
    
    ########################
        #perna2
        import turtle          #tartaruga 7 
        tartaruga = turtle.Turtle()
        tartaruga.hideturtle()
        tartaruga.speed(5)
        tartaruga.penup()
        tartaruga.color("orange")
        if parametro == 5:
            tartaruga.setpos(-200,40)
            tartaruga.pendown()
            tartaruga.left(240)
            tartaruga.forward(40)
        
    
    
    ########################
        #morte
        import turtle          #tartaruga 8 
        tartaruga = turtle.Turtle()
        tartaruga.hideturtle()
        tartaruga.speed(5)
        tartaruga.penup()
        tartaruga.color("red")
        if parametro == 6:
            tartaruga.setpos(-250,110)
            tartaruga.pendown()
            tartaruga.left(0)
            tartaruga.forward(100) #fim do corpo
                  


def letraschutadas(chutes):
    import turtle 
    tartaruga = turtle.Turtle()
    tartaruga.penup()
    tartaruga.setpos(-30,200)
    tartaruga.write("Letras chutadas", align = "left", font = ("Arial", 14, "bold"))
    for i in range(len(chutes)):
        tartaruga.setpos(-30, 200)
        tartaruga.write(chutes[i], align = "left", font = ("Arial", 14, "bold"))
        
        
def letrasacertadas(certas):
    import turtle
    tartaruga = turtle.Turtle()
    tartaruga.penup()
    size_certas = len(certas)
    for i in range (size_certas):
        if pcchoice[i] != " ":
            tartaruga.setpos(-30,200)
            tartaruga.pd()
            tartaruga.forward(20)
        tartaruga.pu()
        tartaruga.setpos(-30,200)
        tartaruga.write(certas[i], align = "left" ,font = ("Arial", 14, "bold"))
        
        
window = desenhaforca()
digitadas = []
erros = 0
acertos = []


C = ["Ç"]
A = ["Ã", "Â", "À", "Á"]
E = ["È", "É", "Ê"]
O = ["Ô", "Õ", "Ó"]
I = ["Í", "Ì", "Î"]
U = ["Ù", "Ú", "Û"]

#############################################
#linhas retiradas de um exemplu do livro Python do Nilo Ney 
window = desenhaforca()
chutes = []
erros = 0
acertos =[]
import turtle 
tartaruga = turtle.Turtle()
while True:
    certas = " "
    for letra in pcchoice:
        if letra in acertos:
            certas += letra
        else:
            certas += " "
    letrasacertadas(certas)
    if certas == pcchoice:
        tartaruga.pu()
        tartaruga.setpos(-150,100)
        tartaruga.write("Parabéns, você adivinhou!!", align = "left", font = ("Arial", 14, "bold"))
        break
    chance = turtle.textinput("Jogo da forca", "Chute uma letra:")
    if chance in chutes:
        continue
    else:
        chutes += chance
        letraschutadas(chutes)
        if chance in pcchoice:
            acertos += chance
        else:
            erros += 1
        if chance == "A":
            for i in range (0,len(A)-1):
                if A[i] in pcchoice:
                    acertos += A[i]
        if chance == "E":
            for i in range(0,len(E)-1):
                if E[i] in pcchoice:
                    acertos +=E[i]
                    
        if chance == "I":
            for i in range(0,len(I)-1):
                if I[i] in pcchoice:
                    acertos += I[i]
        if chance == "O":
            for i in range(0,len(O)-1):
                if O[i] in pcchoice:
                    acertos += 1
        if chance == "U":
            for i in range (0,len(U)-1):
                if U[i] in pcchoice:
                    acertos += 1
        if chance == "C":
            for i in range (0,len(C)-1):
                if C[i] in pcchoice:
                    acertos += 1
        
        if erros == 1:
            desenhaboneco(erros-1)
        if erros == 2:
            desenhaboneco(erros-1)
        if erros == 3:
            desenhaboneco(erros-1)
        if erros == 4:
            desenhaboneco(erros-1)
        if erros == 5:
            desenhaboneco(erros-1)
        if erros == 6:
            desenhaboneco(erros-1)
        if erros == 7:
            desenhaboneco(erros-1)


       
       

window.exitonclick()



