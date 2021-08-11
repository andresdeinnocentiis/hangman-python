from colorama import Fore
from random import *
from os import system
from word import *
from screen import *


import sys

class Player:
    def __init__(self):
        #self.__name = name
        self.__topass = False
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name    
    
    def guess_letter(self, lang): 
        if lang == "english":
            guess = input("Guess a letter: ").upper()
            while not guess.isalpha():
                print("Error. You can only guess letters. Other characters are NOT allowed.") 
                guess = input("Guess a letter: ").upper()
        elif lang == "spanish":
            guess = input("Adivine una letra: ").upper()
            while not guess.isalpha():
                print("Error. Solamente puede adivinar letras. Otros caracteres NO estan permitidos.") 
                guess = input("Adivine una letra: ").upper()
        elif lang == "french":
            guess = input("Devinez une lettre: ").upper()
            while not guess.isalpha():
                print("Erreur. Vous pouvez seulement écrire des lettres. Autres caractères sont INTERDITS.") 
                guess = input("Devinez une lettre: ").upper()
        else:
            guess = input("Угадайте букву: ").upper()
            while not guess.isalpha():
                print("Ошибка. Вы можете выбрать только буквы. Другие симболы НЕ разрешаются.") 
                guess = input("Угадайте букву: ").upper()
        return guess
    
    def guess_word(self, lang):
        if lang == "english":
            guess = input("Guess the word: ").upper()
            while not guess.isalpha():
                print("Error. You can only guess words. Other characters are NOT allowed.") 
                guess = input("Guess the word: ").upper()
        elif lang == "spanish":
            guess = input("Adivine una palabra: ").upper()
            while not guess.isalpha():
                print("Error. Solamente puede adivinar palabras. Otros caracteres NO estan permitidos.") 
                guess = input("Adivine una palabra: ").upper()
        elif lang == "french":
            guess = input("Devinez un mot: ").upper()
            while not guess.isalpha():
                print("Erreur. Vous pouvez seulement écrire des mots. Autres caractères sont INTERDITS.") 
                guess = input("Devinez un mot: ").upper()
        else:
            guess = input("Угадайте слово: ").upper()
            while not guess.isalpha():
                print("Ошибка. Вы можете выбрать только слова. Другие симболы НЕ разрешаются.") 
                guess = input("Угадайте слово: ").upper()        
        return guess
    
    #def ask_for_help(self, word:Word):
        #return word.set_help(True)
        
    
    def says_pass(self):
        self.__topass = True
        return self.__topass
           
    def set_pass(self, topass:bool):
        self.__topass = topass
   
    def get_pass(self):
        return self.__topass

    def __str__(self):
        return self.get_name()