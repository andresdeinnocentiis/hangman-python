from colorama import Fore
from random import *
from os import system
import sys

class Word:
    def __init__(self):
        self.__word = ""
        
        
    
    def type_word(self, lang):
        
        if lang == "english": 
            word = input("Choose the word you want your opponent to guess: ").upper()
            while not word.isalpha():
                print("Error. You can only enter words. Other characters are NOT allowed.") 
                word = input("Choose the word you want your opponent to guess: ").upper()
        elif lang == "spanish": 
            word = input("Escriba la palabra a adivinar: ").upper()
            while not word.isalpha():
                print("Error. Solamente puede ingresar palabras. Otros caracteres NO estan permitidos.") 
                word = input("Escriba la palabra a adivinar: ").upper()
        elif lang == "french": 
            word = input("Choisissez le mot à deviner: ").upper()
            while not word.isalpha():
                print("Erreur. Vous pouvez seulement écrire des mots. Autres caractères sont INTERDITS.") 
                word = input("Choisissez le mot à deviner: ").upper()
        else: 
            word = input("Выберите слово, которое надо угадать: ").upper()
            while not word.isalpha():
                print("Ошибка. Вы можете выбрать только слова. Другие симболы НЕ разрешаются.") 
                word = input("Выберите слово, которое надо угадать: ").upper()
                
        return word
    
    def set_word(self, word):
        self.__word = word
    
    def get_word(self):
        return self.__word
    
    def choose_random_word(self, difficulty, lang):
        word = ""
        
        if difficulty == 1:
            difficulty = "easy"
        elif difficulty == 2:
            difficulty = "medium"
        elif difficulty == 3:
            difficulty = "hard"
        elif difficulty == 4:
            difficulty = "god mode"
        
        if lang == "english":
            folder = "Hangman\\english\\"
            if difficulty == "easy":
                file_name = "easy.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
            elif difficulty == "medium":
                file_name = "medium.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
            elif difficulty == "hard":
                file_name = "hard.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
            else:
                file_name = "god_mode.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
        elif lang == "spanish":
            folder = "Hangman\\espanol\\"
            if difficulty == "easy":
                file_name = "facil.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
            elif difficulty == "medium":
                file_name = "intermedio.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
            elif difficulty == "hard":
                file_name = "dificil.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
            else:
                file_name = "modo_dios.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
        elif lang == "french":
            folder = "Hangman\\francais\\"
            if difficulty == "easy":
                file_name = "facile.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
            elif difficulty == "medium":
                file_name = "intermediaire.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
            elif difficulty == "hard":
                file_name = "difficile.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
            else:
                file_name = "mode_dieu.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
        elif lang == "russian":
            folder = "Hangman\\russian\\"
            if difficulty == "easy":
                file_name = "easy.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
            elif difficulty == "medium":
                file_name = "medium.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
            elif difficulty == "hard":
                file_name = "hard.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
            else:
                file_name = "god_mode.txt"
                file = open(folder+file_name,"r",encoding="utf-8")
                words = file.readlines()
                word = str(choice(words)).upper()
        file.close()
        word_list = []   
        for letter in word:
            word_list.append(letter)
        word_list.remove("\n")
        final_word = ""
        for letter in word_list:
            final_word += letter
        return final_word
        
    
    def hide_word_show_letters(self, word:str, current_word = "", boolguess:bool = False, guess = ""):
        letters_shown = 0
        letters = 0
        letters_list = []
        are_repeated = False
        current_word_list = []
        hidden_word = ""
        
        for i in word:
            letters_list.append(i)
      
        
            
        #HERE I COUNTED WHICH LETTERS WERE REPEATED SO THAT I COULD SHOW THEM, INSTEAD OF COVERING THEM:
        
        letters_dic_count = {} 
        copy_letters_list = letters_list.copy()
        for letter in copy_letters_list:
            if letter in letters_dic_count:
                letters_dic_count[letter] += 1
            else: 
                letters_dic_count[letter] = 1

        repetitions = 0
        
        
        
        if not boolguess:
        
            #HERE I CREATED A BOOLEAN TO DETERMINE WHETHER WERE THERE REPEATED LETTERS OR NOT:
            
            for i in letters_dic_count: 
                if letters_dic_count[i] > 1:
                    repetitions += letters_dic_count[i]
            if repetitions > 0:
                are_repeated = True
                
            #HERE I ESTABLISHED THAT IT WILL ONLY SHOW 2 LETTERS:
            letters_shown = 2
            
            #HERE I COUNTED HOW MANY LETTERS DOES THE WORD HAVE
            for i in word: 
                letters += 1
            
            
            if not are_repeated:
                letters_shown = 2
                if len(word) <= 3:
                    letters_shown = 1
                
                list_to_replace = []
                letters_to_replace = letters - letters_shown

                list_to_replace = sample(letters_list, letters_to_replace)
                for index, letter in enumerate(letters_list):
                    if letter in list_to_replace:
                        letters_list[index] = "_" 
                    else:
                        letters_list[index] = letter
                
                
            
                
            else: # IF ARE REPEATED LETTERS
                #HERE I CREATED THE LIST OF REPEATED LETTERS:
                list_repeated = []
                list_repeated_final = []
                list_to_replace = []
                #letters_to_replace = letters - letters_shown
                for letter in letters_dic_count:
                    if letters_dic_count[letter] > 1:
                        list_repeated.append(letter)
                #if int(repetitions) >= 2:
                if len(list_repeated) > 1 and len(word) > 4:
                    list_repeated_final = sample(list_repeated,2)
                    for i in letters_list:
                        if i not in list_repeated_final:
                            list_to_replace.append(i) 
                    for index, letter in enumerate(letters_list):
                        if letter in list_to_replace:
                            letters_list[index] = "_"
                else:
                    list_repeated_final = sample(list_repeated,1)
                    
                #HERE I CREATED THE LIST OF LETTERS TO REPLACE IF THERE'RE REPEATED LETTERS:
                    for i in letters_list:
                        if i not in list_repeated_final:
                            list_to_replace.append(i)   
    
                #HERE I HIDE THE NECESSARY LETTERS:                      
                
                    for index, letter in enumerate(letters_list):
                        if letter in list_to_replace:
                            letters_list[index] = "_"    
                
                        
            hidden_word = letters_list 
                        
        elif boolguess and guess: # IF ANY PLAYER TRYED TO GUESS:
            for index, letter in enumerate(current_word):
                current_word_list.append(letter)
            for index, letter in enumerate(copy_letters_list):
                if letter != guess and current_word_list[index] == "_":
                    letters_list[index] = "_"
            
            

            hidden_word = letters_list       
        
        
          
        return hidden_word
                
    def string_color_shown_letters(self,hidden_word):
        word = ""
        for letter in hidden_word:
            if letter != "_":
                letter = Fore.BLUE + letter + Fore.RESET + " "
            else:
                letter += " "
            word += letter
        return word
