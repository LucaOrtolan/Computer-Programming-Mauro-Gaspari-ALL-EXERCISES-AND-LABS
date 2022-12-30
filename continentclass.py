# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 14:19:50 2022

@author: Luca
"""

# Write a data type Continent which represents a continent with its name and the associated
# countries. For each country you should store: the name, the capital, the population.
# Implement the following methods:
# addCountry(name,capital,population): add a new country.
# getCapital(name): returns the capital of a country.
# Polulation(): returns the population of all the countries.

class Continent:
    def __init__(self, name):
        self.name= name
        self.countries= {}
        
    def addCountry(self, countryname, capital, population):
        self.countryname= countryname
        self.capital= capital
        self.population= population
        self.countries[countryname]= [capital, population]
        
    def getCapital(self, countryname):
        capital= self.countries[countryname][0]
        return capital
    
    def Population(self):
        s= 0
        for country in self.countries:
            s+= self.countries[country][1]
        return s
    
Europe=Continent("Europe")
Europe.addCountry("Germany","Berlin",80000000)
Europe.addCountry("Italy","Rome",60000000)
Europe.getCapital("Germany")
Europe.getCapital("Italy")
Europe.Population()

Asia=Continent("Asia")
Asia.addCountry("India", "New Delhi", 1400000000)
Asia.addCountry("Pakistan", "Islamabad", 225000000)
Asia.addCountry("Japan", "Tokyo", 125000000)
Asia.getCapital("India")
Asia.getCapital("Pakistan")
Asia.getCapital("Japan")
Asia.Population()  
    