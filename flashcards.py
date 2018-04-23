# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 16:16:51 2018

@author: admin
"""
import pandas as pd 
import time
import os


#######################  FUNCTIONS FOR THE FLASHCARD SYSTEM
def añadir_nuevo_tema():
    nombre_tema_nuevo = input("Whats the name of the new topic?: ")
    temas.append(nombre_tema_nuevo)
    nuevo_tema = pd.DataFrame()
    nuevo_tema["Pregunta"] = ""
    nuevo_tema["Respuesta"] = ""
    nuevo_tema.to_excel("{}.xlsx".format(nombre_tema_nuevo))

def preguntas_aleatorias(tema_seleccionado):
    preg_resp_aleatoria = tema_seleccionado.sample(1)
    p = preg_resp_aleatoria["Pregunta"]
    r = preg_resp_aleatoria["Respuesta"]
    return p, r

def jugar(temas):
    aciertos = 0
    fallos = 0
    print("")
    print("This are the topics: ", temas)
    tema = input("In which topic do you wanna play?: ")
    tema_seleccionado = pd.read_excel("{}.xlsx".format(tema))
    #questions system
    for _ in range(1,4):
        print("Question", _, "is: ")
        p, r = preguntas_aleatorias(tema_seleccionado)
        print(p)
        time.sleep(3)
        saber_respuesta = input("Press 'r' and then 'intro' to see the answer: ")
        if saber_respuesta == "r":
            print("The answers is ", r)
        acierto = input("Did you get the answer?. 'y' = yes / 'n' = no: ")
        if acierto == "y":
            aciertos += 1
        else: 
            fallos += 1
    
    return aciertos, fallos
        
def nivel_de_conocimientos (aciertos):
    if aciertos == 10:
        print("Lo llevas genial")
    elif aciertos < 10 and aciertos >= 8:
        print("Lo llevas bien")
    elif aciertos < 8 and aciertos >= 6:
        print("Lo llevas")
    elif aciertos == 5:
        print("Has sacado una nota justita")
    else: 
        print("Ponte a esutidar alma de dios")
    
def edit(tema_para_modificar, tema):
    print("This are the questions and answers of the topic", tema_para_modificar)
    edicion_de = input("What do you want to edit? Write 'q' for question or 'a' for answer: ")
    if edicion_de == "q":
        numero_pregunta= int(input("What question do you want to edit? Select a number: "))
        edicion = input("Rewrite the question: ")
        tema_para_modificar.loc[numero_pregunta,"Pregunta"] = "{}".format(edicion)
        tema_para_modificar.to_excel("{}.xlsx".format(tema))
    elif edicion_de == "a":
        numero_respuesta= int(input("What question do you want to edit? Select a number: "))
        edicion = input("Rewrite the question: ")
        tema_para_modificar.loc[numero_respuesta,"Respuesta"] = "{}".format(edicion)   
        tema_para_modificar.to_excel("{}.xlsx".format(tema))
def borrar(tema_para_modificar,tema):
    print("These are the q / a in the topic.", tema_para_modificar)
    pregunta_para_borrar = int(input("Select the question to delete: "))
    tema_para_exportar = pd.DataFrame()
    tema_para_exportar = tema_para_modificar.drop(tema_para_modificar.index[pregunta_para_borrar])
    tema_para_exportar.to_excel("{}.xlsx".format(tema))

def nueva_pregunta(tema_para_modificar, tema):
    p = input("Write the question you want to add: ")
    r = input("Write the asnwer to the last question: ")
    tema_para_modificar = tema_para_modificar.append(pd.Series(['{}'.format(p), '{}'.format(r)], index=['Pregunta','Respuesta']), ignore_index=True)
    tema_para_modificar.to_excel("{}.xlsx".format(tema))
#######################
#Menu for choosing the actions. You can play the game, edit flashcards or create a new category

temas = os.listdir(".")
temas.remove("flashcards.py")

while True: 
    action = input("Welcome to 'Flash Card, the game'. Please write '1' to play game, '2' to edit flashcards or'3' for create a new category, '4' to exit. The press 'intro': ")
    #in "1" you play the game
    if action == "1":
        aciertos, fallos = jugar(temas)
        print("You finished the match. You get: ", aciertos,"/10 points.")
        nivel_de_conocimientos(aciertos)
        print("Thanks for play 'Flash Card, the game'. Hope see you soon.")
    elif action == "2":
            accion_de_edicion = input("What do you want to do? '1' to edit / '2' to delete / '3' to add a new question - answer: ")
            print("These are the topics: ", temas)
            tema = input("Which Topic do you wanna modify?: ")
            tema_para_modificar = pd.read_excel("{}.xlsx".format(tema))
            if accion_de_edicion == "1":
                edit(tema_para_modificar,tema)
                False
            elif accion_de_edicion == "2":
                borrar(tema_para_modificar,tema)
                False
            elif accion_de_edicion == "3":
                nueva_pregunta(tema_para_modificar,tema)
                False
    elif action == "3":
        añadir_nuevo_tema()
    elif action == "4":
        break
    else: 
        break
