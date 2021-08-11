from colorama import Fore



def language(lang:str, phrase_number:int, player=None,players=None,failed_attempts=None, *args, **kwargs)->str:
    script = ""

    if lang == "english":
        if phrase_number == 1:
            script = f"{Fore.YELLOW}===================\n|  H A N G M A N  |\n==================={Fore.RESET}\n\nSelect mode:\n\n1. vs. COM\n2. vs. Player\n\n__________________________\n\n0. GO BACK\n__________________________"
        elif phrase_number == 2:
            script = "Select mode: "
        elif phrase_number == 3:
            script = "Error. You can only choose between the numbers 1, 2 or 0."
        elif phrase_number == 4:
            script = "Error. You can only enter the option number."
        elif phrase_number == 5:
            script = "DIFFICULTY:\n\n1. EASY\n2. MEDIUM\n3. HARD\n4. GOD MODE\n\n__________________________\n\n0. EXIT GAME\n__________________________"
        elif phrase_number == 6:
            script = "Select difficulty: "
        elif phrase_number == 7:
            script = "Please enter the player's name: "
        elif phrase_number == 8:
            script = "Player"
        elif phrase_number == 9:
            script = "Please insert the amount of players that are going to play: "
        elif phrase_number == 10:
            script = "Error. You can only enter a number."
        elif phrase_number == 11:
            script = "Select the number of the player that will type the word: "
        elif phrase_number == 12:
            script = "___________________________\nWhat would you like to do?:\n\n1. Guess letter\n2. Guess word\n3. Pass\n4. Ask for help\n___________________________"
        elif phrase_number == 13:
            script = "Select an option: "
        elif phrase_number == 14:
            script = "Error. You can only choose between the numbers 1 to 4."
        elif phrase_number == 15:
            script = f"{Fore.LIGHTCYAN_EX}It's {player} - {players[player]}'s turn: {Fore.RESET}"
        elif phrase_number == 16:
            script = Fore.GREEN+"---------------------------------\n Thank you for playing Hangman. \n---------------------------------\n"+Fore.RESET
        elif phrase_number == 17:
            script = f"{Fore.YELLOW}CURRENT PLAYERS:{Fore.RESET}\n"
        elif phrase_number == 18:
            script = "will type the word:"
        elif phrase_number == 19:
            script = Fore.LIGHTBLUE_EX + "-------------\nGAME STARTED\n-------------" + Fore.RESET
        elif phrase_number == 20:
            script = "CURRENT GUESSES: \n"
        elif phrase_number == 21:
            script =  "has chosen:"
        elif phrase_number == 22:
            script = f"{Fore.RED}Wrong choice.{Fore.RESET}"
        elif phrase_number == 23:
            script = f"{Fore.RED}GAME OVER. YOU LOST.{Fore.RESET}"     
        elif phrase_number == 24:
            script =  f"{Fore.CYAN}GAME OVER. YOU WIN!!!{Fore.RESET}"
        elif phrase_number == 25:
            script =  "tried the word:"
        elif phrase_number == 26:
            script =  "has guessed correctly!!"
        elif phrase_number == 27:
            script =  "The word was:"
        elif phrase_number == 28:
            script =  f"{Fore.CYAN}GAME OVER. YOU WIN!!!.{Fore.RESET}"
        elif phrase_number == 29:
            script =  "has guessed horribly wrong.."
        elif phrase_number == 30:
            script =  f"{Fore.RED}GAME OVER. EVERYONE LOST BECAUSE OF"
        elif phrase_number == 31:
            script = "chickend out and passes.." 
        elif phrase_number == 32:
            script =  f"{Fore.MAGENTA} isn't very good at this, so he asked for help.{Fore.RESET}"
        elif phrase_number == 33:
            script = f"WHAT A LOSER..{Fore.RESET}"
        
        
        
            
    if lang == "spanish":
        if phrase_number == 1:
            script = f"{Fore.YELLOW}=====================\n|  A H O R C A D O  |\n====================={Fore.RESET}\n\nElija la modalidad:\n\n1. vs. COM\n2. vs. Jugador\n\n__________________________\n\n0. VOLVER\n__________________________"
        elif phrase_number == 2:
            script = "Elija la modalidad: "
        elif phrase_number == 3:
            script = "Error. Solamente puede elegir entre los números 1, 2 or 0."
        elif phrase_number == 4:
            script = "Error. Solamente puede elegir el número de la opción."
        elif phrase_number == 5:
            script = "DIFICULTAD:\n\n1. FÁCIL\n2. INTERMEDIO\n3. DIFÍCIL\n4. MODO DIOS\n\n__________________________\n\n0. SALIR DEL JUEGO\n__________________________"
        elif phrase_number == 6:
            script = "Seleccione la dificultad: "
        elif phrase_number == 7:
            script = "Por favor ingrese el nombre del jugador: "
        elif phrase_number == 8:
            script = "Jugador"
        elif phrase_number == 9:
            script = "Por favor ingrese la cantidad de jugadores: "
        elif phrase_number == 10:
            script = "Error. Solamente puede ingresar un número."
        elif phrase_number == 11:
            script = "Seleccione el número del jugador que va a elegir la palabra: "
        elif phrase_number == 12:
            script = "___________________________\nQué quiere hacer?:\n\n1. Adivinar letra\n2. Adivinar palabra\n3. Pasar\n4. Pedir ayuda\n___________________________"
        elif phrase_number == 13:
            script = "Elija la opción: "
        elif phrase_number == 14:
            script = "Error. Solamente puede elegir entre los números 1 a 4."
        elif phrase_number == 15:
            script = f"{Fore.LIGHTCYAN_EX}Es el turno de {player} - {players[player]}: {Fore.RESET}"
        elif phrase_number == 16:
            script = Fore.GREEN+"---------------------------------\n Gracias por jugar al Ahorcado. \n---------------------------------\n"+Fore.RESET
        elif phrase_number == 17:
            script = f"{Fore.YELLOW}JUGADORES ACTUALES:{Fore.RESET}\n"
        elif phrase_number == 18:
            script = "escribirá la palabra:"
        elif phrase_number == 19:
            script = Fore.LIGHTBLUE_EX + "-----------------\nCOMIENZA EL JUEGO\n-----------------" + Fore.RESET
        elif phrase_number == 20:
            script = f"INTENTOS: \n"
        elif phrase_number == 21:
            script =  "ha elegido:" 
        elif phrase_number == 22:
            script = f"{Fore.RED}Elección equivocada.{Fore.RESET}"  
        elif phrase_number == 23:
            script = f"{Fore.RED}JUEGO TERMINADO. HAN PERDIDO.{Fore.RESET}"         
        elif phrase_number == 24:
            script = f"{Fore.CYAN}JUEGO TERMINADO. HAN GANADO!!!{Fore.RESET}" 
        elif phrase_number == 25:
            script =  "ha intentado con la palabra:"
        elif phrase_number == 26:
            script =  "ha adivinado correctamente!!"
        elif phrase_number == 27:
            script =  "La palabra era:"
        elif phrase_number == 28:
            script =  f"{Fore.CYAN}JUEGO TERMINADO. HAN GANADO!!!{Fore.RESET}"
        elif phrase_number == 29:
            script =  "no ha adivinado correctamente.."
        elif phrase_number == 30:
            script =  f"{Fore.RED}JUEGO TERMINADO. TODOS HAN PERDIDO POR CULPA DE"
        elif phrase_number == 31:
            script =  "se asustó y eligió pasar.."
        elif phrase_number == 32:
            script =  "no es muy bueno en esto, asi que pidió ayuda."
        elif phrase_number == 33:
            script = f"QUE PERDEDOR..{Fore.RESET}"
        
        
            
    if lang == "french":
        if phrase_number == 1:
            script = f"{Fore.YELLOW}=====================\n|  L E   P E N D U  |\n====================={Fore.RESET}\n\nSélectionnez le mode:\n\n1. vs. COM\n2. vs. Joueur\n\n__________________________\n\n0. RETURNER\n__________________________"
        elif phrase_number == 2:
            script = "Sélectionnez le mode: "
        elif phrase_number == 3:
            script = "Erreur. Vous pouvez seulement choisir entre les nombres 1, 2 ou 0."
        elif phrase_number == 4:
            script = "Erreur. Vous pouvez seulement saisir le nombre de la option."
        elif phrase_number == 5:
            script = "DIFFICULTÉ:\n\n1. FACILE\n2. INTERMÉDIAIRE\n3. DIFFICILE\n4. MODE DIEU\n\n__________________________\n\n0. QUITTER LE JEU\n__________________________"
        elif phrase_number == 6:
            script = "Saisissez la difficulté: "
        elif phrase_number == 7:
            script = "Veuillez saisir le prénom du joueur: "
        elif phrase_number == 8:
            script = "Joueur"
        elif phrase_number == 9:
            script = "Veuillez saisir la quantité de joueurs: "
        elif phrase_number == 10:
            script = "Erreur. Vous pouvez seulement entrer un nombre."
        elif phrase_number == 11:
            script = "Saisissez le nombre du joueur qui écrira le mot: "
        elif phrase_number == 12:
            script = "___________________________\nQu'est-ce que vous voulez faire?:\n\n1. Deviner une lettre\n2. Deviner un mot\n3. Passer\n4. Demander de l'aide\n___________________________"
        elif phrase_number == 13:
            script = "Sélectionnez l'option': "
        elif phrase_number == 14:
            script = "Erreur. Vous pouvez seulement choisir entre les nombres 1 à 4."
        elif phrase_number == 15:
            script = f"{Fore.LIGHTCYAN_EX}C'est le tour de {player} - {players[player]}: {Fore.RESET}"
        elif phrase_number == 16:
            script = Fore.GREEN+"---------------------------------\n Merci d'avoir joué au Pendu. \n---------------------------------\n"+Fore.RESET
        elif phrase_number == 17:
            script = f"{Fore.YELLOW}JOUEURS ACTUELS:{Fore.RESET}\n"
        elif phrase_number == 18:
            script = "écrira le mot:"
        elif phrase_number == 19:
            script = Fore.LIGHTBLUE_EX + "---------------\nLE JEU COMMENCE\n---------------" + Fore.RESET
        elif phrase_number == 20:
            script = "ESSAIS"
        elif phrase_number == 21:
            script =  "a choisi:" 
        elif phrase_number == 22:
            script =  f"{Fore.RED}Choix erroné.{Fore.RESET}" 
        elif phrase_number == 23:
            script = f"{Fore.RED}JEU TERMINÉ. VOUS AVEZ PERDU.{Fore.RESET}"   
        elif phrase_number == 24:
            script = f"{Fore.CYAN}JEU TERMINÉ. VOUS AVEZ GAGNÉ!!!{Fore.RESET}" 
        elif phrase_number == 25:
            script = "a essayé avec le mot:" 
        elif phrase_number == 26:
            script =  "a deviné correctement!!"
        elif phrase_number == 27:
            script = "Le mot était:" 
        elif phrase_number == 28:
            script =  f"{Fore.CYAN}JEU TERMINÉ. VOUS AVEZ GAGNÉ!!!.{Fore.RESET}"
        elif phrase_number == 29:
            script =  "n'a pas deviné correctement.."   
        elif phrase_number == 30:
            script =  f"{Fore.RED}JEU TERMINÉ. TOUS ONT PERDU À CAUSE DE"
        elif phrase_number == 31:
            script =  "a paniqué et a choisi de passer.."
        elif phrase_number == 32:
            script =  "n'est pas doué pour ça, il a donc demandé de l'aide."    
        elif phrase_number == 33:
            script = f"QUEL PERDANT..{Fore.RESET}"
                
                
    if lang == "russian":
        if phrase_number == 1:
            script = f"{Fore.YELLOW}=====================\n|  В Е С Е Л И Ц А  |\n====================={Fore.RESET}\n\nВыберите режим игры:\n\n1. vs. КОМ\n2. vs. Игрок\n\n__________________________\n\n0. НАЗАД\n__________________________"
        elif phrase_number == 2:
            script = "Выберите режим игры: "
        elif phrase_number == 3:
            script = "Ошибка. Вы можете выбрать только между числами 1, 2 или 0."
        elif phrase_number == 4:
            script = "ОШИБКА. Вы можете ввести только число опции."
        elif phrase_number == 5:
            script = "СЛОЖНОСТЬ:\n\n1. ЛЁГКИЙ\n2. УМЕРЕННЫЙ\n3. ЖЁСТКИЙ\n4. РЕЖИМ БОГА\n\n__________________________\n\n0. ВЫЙТИ ИЗ ИГРЫ\n__________________________"
        elif phrase_number == 6:
            script = "Выберите сложность: "
        elif phrase_number == 7:
            script = "Пожалуйста, введите имя игрока: "
        elif phrase_number == 8:
            script = "Игрок"
        elif phrase_number == 9:
            script = "Пожалуйста, введите количесиво игроков: "
        elif phrase_number == 10:
            script = "ОШИБКА. Вы можете ввести только числа."
        elif phrase_number == 11:
            script = "Выберите число игрока, кто напишет слово: "
        elif phrase_number == 12:
            script = "___________________________\nЧто вы хотите сделать?:\n\n1. Угадать букву\n2. Угадать слово\n3. Пасс\n4. Попросить помощи\n___________________________"
        elif phrase_number == 13:
            script = "Выберите опцию: "
        elif phrase_number == 14:
            script = "Ошибка. Вы можете выбрать только между числами 1 до 4."
        elif phrase_number == 15:
            script = f"{Fore.LIGHTCYAN_EX}Теперь пришла очередь {player} - {players[player]}: {Fore.RESET}"
        elif phrase_number == 16:
            script = Fore.GREEN+"---------------------------------\n Спасибо, что играли в Веселицу. \n---------------------------------\n"+Fore.RESET
        elif phrase_number == 17:
            script = f"{Fore.YELLOW}НЫНЕШНИЕ ИГРОКИ:{Fore.RESET}\n"
        elif phrase_number == 18:
            script = "напишет слово:"
        elif phrase_number == 19:
            script = Fore.LIGHTBLUE_EX + "---------------\nИГРА НАЧИНАЕТСЯ\n---------------" + Fore.RESET
        elif phrase_number == 20:
            script = "ПОПЫТКИ"
        elif phrase_number == 21:
            script =  "выбрал:" 
        elif phrase_number == 22:
            script =  f"{Fore.RED}Неправильный выбор.{Fore.RESET}" 
        elif phrase_number == 23:
            script =  f"{Fore.RED}ИГРА ОКОНЧЕНА. ВЫ ПРОИГРАЛИ.{Fore.RESET}"
        elif phrase_number == 24:
            script = f"{Fore.CYAN}ИГРА ОКОНЧЕНА. ВЫ ВЫИГРАЛИ!!!{Fore.RESET}" 
        elif phrase_number == 25:
            script =  "попробовал со словом:"
        elif phrase_number == 26:
            script = "угадал правильно!!" 
        elif phrase_number == 27:
            script = "Слово было:" 
        elif phrase_number == 28:
            script = f"{Fore.CYAN}ИГРА ОКОНЧЕНА. ВЫ ВЫИГРАЛИ.{Fore.RESET}" 
        elif phrase_number == 29:
            script =  "неправильно угадал.."
        elif phrase_number == 30:
            script = f"{Fore.RED}ИГРА ОКОНЧЕНА. ВЫ ВСЕ ПРОИГРАЛИ ИЗ-ЗА" 
        elif phrase_number == 31:
            script =  "струсил и предпочёл пасс.."
        elif phrase_number == 32:
            script =  "плохо получается, так что он обратился за помощью."
        elif phrase_number == 33:
            script = f"КАКОЙ ОН ЛОХ..{Fore.RESET}"    
                    
    return script