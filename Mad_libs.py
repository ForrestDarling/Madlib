#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Forrest Darling"



noun1 = input("Please enter a name:")
noun2 = input("Please enter a place:")
verb1 = input("Please enter a verb:")
adj1 = input("Please enter a adjective:")
adj2 = input("Please enter another adjective:")
verbing = input("Please enter a verb ending in 'ing':")
job = input("Please enter a job title:")
celeb = input("Please enter the name of a celebrity:")


print("Once upon a time there was someone named {}.".format(noun1))
print("{} lived in a land called {}.".format(noun1, noun2))
print("All day long {} would spend their time {}.".format(noun1, verbing))
print("People would describe {} as {} and {}.".format(noun1, adj1, adj2))
print("Then one day {} spontaneously arrived in {}.".format(celeb, noun2))
print("Almost immediatley {} and {} began to {} with reckless abandon.".format(celeb, noun1, verb1))
print("After {} went home, {} went back to their job as a {}.".format(celeb, noun1,job))

