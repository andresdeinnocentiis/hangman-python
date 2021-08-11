from colorama import Fore
from random import *
from os import system
from player import *
import sys
from screen import *
from word import *
import difflib
from language_mod import language

class Game:
    def __init__(self) -> None:
        self.__screen = Screen()
        self.__players = {}
        self.__word = Word()
        self.lang = ""

    def show_lang_menu(self):
        print(f"{Fore.YELLOW}===================\n|  H A N G M A N  |\n==================={Fore.RESET}\n\n{Fore.BLUE}BY @andresdeinnocentiis{Fore.RESET}\n\nSelect your language:\n\n1. English\n2. Español\n3. Français\n4. Русский\n__________________________\n\n0. EXIT GAME\n__________________________")

    def select_lang_menu(self):
        self.show_lang_menu()
        self.lang = input("Select an option from the above: ")

        if self.lang == str(1):
            self.lang = "english"
        elif self.lang == str(2):
            self.lang = "spanish"
        elif self.lang == str(3):
            self.lang = "french"
        elif self.lang == str(4):
            self.lang = "russian"
        elif self.lang == str(0):
            self.exit()

        else:
            print("Error. Invalid option.")
            self.lang = input("Please select an option from the above: ")
        return self.lang

    def show_menu(self, lang):
        menu = language(lang, 1)
        print(menu)

    def select_mode(self, lang):
        can_continue = False
        while not can_continue:
            try:
                mode = int(input(language(lang, 2)))
                if mode != 1 and mode != 2 and mode != 0:
                    print(language(lang, 3))
                else:
                    can_continue = True
            except:
                print(language(lang, 4))
            
        return mode

    def select_difficulty(self, lang):
        difficulty = ""
        can_continue = False
        while not can_continue:
            print(language(lang, 5))
            try:
                difficulty = int(input(language(lang, 6)))
                if difficulty != 1 and difficulty != 2 and difficulty != 3 and difficulty != 4 and difficulty != 0:
                    print(language(lang, 4))
                else:
                    can_continue = True
            except:
                print(language(lang, 4))

        return(difficulty)

    def add_player(self, players, lang) -> dict:
        num = 0
        for i in range(players): 
            player = Player()
            player.set_name(
                input(language(lang,7)).title())
            plr = language(lang,8)

            num += 1
            numplayer = str(num)
            addplayer = f"{plr}{numplayer}"
            self.__players[addplayer] = player

        return self.__players

    def ask_for_players(self, lang):
        players = ""   
        try:
            players = int(input(language(lang,9)))
        except:
            print(language(lang,10))
        
        return(players)

    def set_players(self, players):
        self.__players = players

    def get_players(self):
        return self.__players

    def who_types_word(self, lang, players):
        player = input(language(lang,11))

        for index, plr in enumerate(list(players)):
            if player in plr:
                player = plr
        return player

    def check_guess(self, word: str, guess:str) -> bool:
        correct = False
        
        if len(guess) > 1:
            if guess == word:
                correct = True
        else:
            for index, letter in enumerate(word):
                if letter == guess:
                    correct = True

        return correct


    def help(self, word, hidden_word_list):
        word_list = []
        letters_to_replace = []
        new_word_list = []
        for letter in word:
                word_list.append(letter)
        for index, letter in enumerate(hidden_word_list): 
            if letter == "_":
                letters_to_replace.append(word_list[index])
        help_letter = choice(letters_to_replace)
        
                
        

                
        return help_letter   


    def whose_turn(self, players: dict, turn:int):

        playerturn = list(players)[turn]
        # for index, plr in enumerate(list(players)):
        # if str(turn) in plr:
        #playerturn = plr
        return playerturn

    def show_attempts(self, guesses):
        attempts = ""
        for attempt in guesses:
            attempts += Fore.RED + attempt + Fore.RESET + ", "

        return attempts

    def player_menu(self, lang):
        menu = language(lang, 12)
        print(menu)

    def player_options(self, lang):
        self.player_menu(lang)
        option = ""
        can_continue = False
        while not can_continue:
            try:
                option = int(input(language(lang, 13)))
                if option != 1 and option != 2 and option != 3 and option != 4:
                    print(language(lang, 14))
                else:
                    can_continue = True
            except:
                print(language(lang, 4))

        return option

    def player_plays(self, lang, word: Word, player: Player):
        option = self.player_options(lang)
        move = ""
        if option == 1:
            move = player.guess_letter(lang)
            player.set_pass(False)
        if option == 2:
            move = player.guess_word(lang)
            player.set_pass(False)
        if option == 3:
            move = player.says_pass()
        elif option == 4:
            move = 4

        return move

    def determine_turn(self, lang, turn, players: dict, determine_player: Player) -> Player:

        for player in list(players):
            if player == determine_player:
                print(language(lang, 15,player, players))
                current_player = players[player]

        return current_player

    def exit(self, lang="english"):
        msg = language(lang,16)
        print(msg)

        sys.exit(0)

# PLAY GAME:

    def play(self):
        end = False
        msg = ""
        difficulty = ""
        pl_choose = ""  # THIS IS THE PLAYER THAT WILL CHOOSE THE WORD TO GUESS
        admin = ""  # This will be the player who chose the word, popped out of the dictionary of players
        errors = 0
        guesses = []
        turn = 0
        current_player = ""
        correct_word = ""
        mode = 0
        # while not end:
        ### GAME STEPS: ###

        # 1. SHOW LANG MENU AND SELECT LANG:
        while mode == 0:
            lang = self.select_lang_menu()
            print("\n")
            if lang == 0:
                end = True

                self.exit()
            else:
                # 2.SELECT MODE:
                self.show_menu(lang)
                mode = self.select_mode(lang)

            # 3. IF VS.COM - SELECT DIFFICULTY:
        
        
        if mode == 1:  # VS. COM
            
            difficulty = self.select_difficulty(lang)
            if difficulty == 0:
                self.exit(lang)
                
            # 4. SELECT AMOUNT OF PLAYERS AND ADD THEM TO DE DICTIONARY:
            
            amount_of_players = self.ask_for_players(lang)
            players = self.add_player(amount_of_players, lang)
            
            system('cls')
            
            print(f"{Fore.YELLOW}CURRENT PLAYERS:{Fore.RESET}\n")
            for key, value in players.items():
                print(f"{Fore.BLUE}- {key}:{Fore.RESET} {value}")
            list_players = players.items()
            
            # 5. PICK WORD (FROM FILE OR MAKE THE PLAYER TYPE THE WORD, DEPENDING THE CASE)
            
            word = Word()
            word.set_word(word.choose_random_word(difficulty, lang))

        elif mode == 2:  # VS. PLAYER
            amount_of_players = self.ask_for_players(lang)
            players = self.add_player(amount_of_players, lang)
            system('cls')
            print(language(lang, 17))
            for key, value in players.items():
                print(f"{Fore.BLUE}- {key}:{Fore.RESET} {value}")
            list_players = players.items()
            pl_choose = self.who_types_word(lang, players)
            players_iterator = players.copy()
            for player in players_iterator:
                if player == pl_choose:
                    admin = players.pop(player)
                    
                    # THE PLAYER THAT CHOOSE THE WORD TO GUESS, WON'T BE PLAYING
                    # SHOW WHO WILL BE WRITING THE WORD:
                    print(f"{Fore.YELLOW}{player} - {players_iterator[player]},",language(lang, 18) + Fore.RESET)
                    

            word = Word()
            word.set_word(word.type_word(lang))
            system('cls')
            print(language(lang, 17))
            for key, value in players.items():
                print(f"{Fore.BLUE}- {key}:{Fore.RESET} {value}")
        print("\n")
    # 6. HIDE AND SHOW LETTERS.

        hidden_word_list = Word().hide_word_show_letters(word.get_word())
        hidden_word = Word().string_color_shown_letters(hidden_word_list)
        
        # SHOW "START GAME" MESSAGE:
        msg = language(lang, 19)
        print(msg)

        print("\n")
        
        # PRINT THE WORD WITH HIDDEN LETTERS:
        print(hidden_word)
        
        # CREATE AND SHOW SCREEN:
        s = Screen().createScreen()
        screen = Screen().convertString(s)
        print(screen)

        # 7. PLAYERS PLAY
        # 7.A. CHOOSE PLAYER LOOPING THROUGH THE DICTIONARY OF PLAYERS
        while not end:
            if turn >= len(players):
                turn = 0
            determine_player = self.whose_turn(players, turn)
            current_player = self.determine_turn(lang, turn, players, determine_player)
            turn += 1
            failed_attempts = self.show_attempts(guesses)
            print(language(lang, 20))
            print(f"[{self.show_attempts(guesses)}]")
            
            guess = self.player_plays(lang, word, current_player)
            print("\n")
            if type(guess) == str:
                print(current_player,language(lang,21),guess)
                print("\n")
                if len(guess) == 1:
                    
                    # 7.B. CHECK EACH GUESS AND NEXT PLAYER
                    
                    correct = self.check_guess(word.get_word(), guess)
                    
                    # 7.C. IF WRONG GUESS, ADD PART OF THE BODY
                    
                    if not correct:
                        guesses.append(Fore.RED + guess + Fore.RESET)
                        print(language(lang, 22))
                        print("\n")
                    
                        errors += 1
                        
                        if errors == 1:
                            print(hidden_word)
                            print("\n")
                            s = Screen().createScreen(error1=True)
                            screen = Screen().convertString(s)
                            print(screen)
                            
                        if errors == 2:
                            print(hidden_word)
                            print("\n")
                            s = Screen().createScreen(error1=True, error2=True)
                            screen = Screen().convertString(s)
                            print(screen)
                            
                        if errors == 3:
                            print(hidden_word)
                            print("\n")
                            s = Screen().createScreen(error1=True, error2=True, error3=True)
                            screen = Screen().convertString(s)
                            print(screen)
                            
                        if errors == 4:
                            print(hidden_word)
                            print("\n")
                            s = Screen().createScreen(error1=True, error2=True, error3=True, error4=True)
                            screen = Screen().convertString(s)
                            print(screen)
                            
                        if errors == 5:
                            print(hidden_word)
                            print("\n")
                            s = Screen().createScreen(error1=True, error2=True,
                                                    error3=True, error4=True, error5=True)
                            screen = Screen().convertString(s)
                            print(screen)
                        if errors == 6:
                            print(hidden_word)
                            print("\n")
                            s = Screen().createScreen(error1=True, error2=True,
                                                    error3=True, error4=True, error5=True, error6=True)
                            screen = Screen().convertString(s)
                            print(screen)
                            
                            #GAME OVER MESSAGE:
                            print(language(lang, 23))
                            

                            end = True
                    else:  # IF CORRECT
                        hidden_word_list = Word().hide_word_show_letters(
                            word.get_word(), hidden_word_list, True, guess)
                        hidden_word = Word().string_color_shown_letters(hidden_word_list)
                        print(hidden_word)
                        print("\n")
                        print(screen)
                        print("\n")
                        if "_" not in hidden_word_list:
                            #YOU WIN MESSAGE:
                            print(language(lang, 24))
                            print("\n")
                            end = True
            
                else:
                    correct = self.check_guess(word.get_word(), guess)
                    
                    if correct: #IF THE PLAYER GUESSED THE WORD CORRECTLY:
                        print("\n")
                        print(screen)
                        print("\n")
                        
                        #VICTORY MESSAGES:
                        
                        print(current_player,language(lang, 25), Fore.RED+guess+Fore.RESET)
                        print(current_player,language(lang, 26))
                        print(language(lang, 27), word.string_color_shown_letters(word.get_word()))
                        print(language(lang, 28))
                        print("\n")
                        
                        end = True
                    
                    else: # IF THE PLAYER DIDN'T GUESS THE WORD CORRECTLY:
                    
                        
                        errors = 6
                        print(hidden_word)
                        print("\n")
                        s = Screen().createScreen(error1=True, error2=True,
                                                    error3=True, error4=True, error5=True, error6=True)
                        screen = Screen().convertString(s)
                        print(screen)
                        
                        #DEFEAT MESSAGES:
                        
                        print(current_player,language(lang, 25), Fore.RED+guess+Fore.RESET)
                        print(current_player,language(lang, 29))
                        print(language(lang, 27), word.string_color_shown_letters(word.get_word()))
                        print(language(lang, 30), f"{current_player},", language(lang, 33))

                        end = True
        
            elif type(guess) == bool and guess == current_player.says_pass():
                print(hidden_word)
                print(screen)
                print(f"{Fore.MAGENTA}{current_player}", language(lang, 31) + Fore.RESET)
                print("\n")
                current_player.set_pass(False)
            
            elif guess == 4:
                help_word = self.help(word.get_word(), hidden_word_list) 
                #ASKED FOR HELP MESSAGE:   
                if lang != "russian":
                    print(f"{Fore.MAGENTA}{current_player}", language(lang, 32) + Fore.RESET)
                else:
                    print(f"{Fore.MAGENTA}У {current_player}", language(lang,32) + Fore.RESET)
                print("\n")
                
                hidden_word_list = Word().hide_word_show_letters(word.get_word(),hidden_word_list,True,help_word)
                hidden_word = Word().string_color_shown_letters(hidden_word_list)
                print(hidden_word)
                print(screen)
                print("\n")
                
                if "_" not in hidden_word_list:
                    #YOU WIN MESSAGE:
                    print(language(lang, 28))
                    print("\n")
                    end = True
            

#Main function
def main():

    Game().play()

main()
