# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 13:06:19 2022

@author: Luca
"""

# Write a program qfinfo, that entering the course ID of a qf course
# prints the title, the professor and the number of credits of that
# course.
# ● Use a dictionary to store the relevant information.

epelm={37500:["Economia Industriale Avanzata", "Luca Lambertini", "10CFU"],
       32248:"Metodi Quantitativi, Natascia Angelini, 12CFU",
       32917:"Econometria Avanzata, Roberto Golinelli, 10CFU",
       32424:"Microeconomia Avanzata, Nadia Burani, 10CFU",
       32423:"Macroeconomia Avanzata, Paolo Manasse, 10CFU",
       96100:"Environmental Economics and Policy, Emanuele Campiglio, 10CFU",
       31932:"Economia e Tecnica dei Mercati Finanziari, Giuseppe Lusignani, 12CFU",
       37499:"Politiche Comunitarie, Giovanna Marchianò, 10CFU",
       97342:"Metodi Econometrici per la Valutazione di Politiche Pubbliche, Guglielmo Barone, 5CFU",
       37262:"Computer Programming, Mauro Gaspari, 6CFU"}

def epelminfo(epelm):
    ID=int(input("Insert course ID: "))
    print(epelm[ID])   

epelminfo(epelm)

