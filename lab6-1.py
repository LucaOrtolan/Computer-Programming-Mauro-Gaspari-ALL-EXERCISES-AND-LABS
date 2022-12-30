# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 11:37:32 2022

@author: Luca
"""

# Considering the list of QF courses that includes the course name,
# the professor and a short description of the course. Implement and
# test the following operations:
# – get_professor(course_name) returns the professor.
# – get_description(course_name) returns the description.
# – get_courses(string) return the list of courses whose name
# include ‘string’.

epelm={37500:["Economia Industriale Avanzata", "Luca Lambertini", "10CFU"],
       32248:["Metodi Quantitativi", "Natascia Angelini", "12CFU"],
       32917:["Econometria Avanzata", "Roberto Golinelli", "10CFU"],
       32424:["Microeconomia Avanzata", "Nadia Burani", "10CFU"],
       32423:["Macroeconomia Avanzata", "Paolo Manasse", "10CFU"],
       96100:["Environmental Economics and Policy", "Emanuele Campiglio", "10CFU"],
       31932:["Economia e Tecnica dei Mercati Finanziari", "Giuseppe Lusignani", "12CFU"],
       37499:["Politiche Comunitarie", "Giovanna Marchianò", "10CFU"],
       97342:["Metodi Econometrici per la Valutazione di Politiche Pubbliche", "Guglielmo Barone", "5CFU"],
       37262:["Computer Programming", "Mauro Gaspari", "6CFU"]}

def get_professor(course):
    print(epelm[course][1])

get_professor(32248)

def get_description(course):
    print(epelm[course][0])

get_description(32248)
    
def get_courses(string):
    courses=[]
    for value in epelm:
        if string in value:
            courses.append(value)
    return courses
        
        
get_courses("Avanzata")
    