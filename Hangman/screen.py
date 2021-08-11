from colorama import Fore
from random import *
from os import system
import sys


class Screen(object):
    def __init__(self) -> None:
        super().__init__()
        
    
    def createScreen(self, error1 = False, error2 = False, error3 = False, error4 = False, error5 = False, error6 = False):    
        screen = []
        for line in range(11):
            row = []
            for column in range(11):
                row.append("   ")
            screen.append(row)
        
        for i, char in enumerate(screen[1]):
            char = Fore.LIGHTYELLOW_EX + "___"  + Fore.RESET
            if i > 2 and i < 7:
                screen[1][i] = char
                
        for i, char in enumerate(screen[2]):
            if i == 2:
                screen[2][i] = Fore.LIGHTYELLOW_EX + "  |" + Fore.RESET
            if i == 7:
                screen[2][i] = Fore.LIGHTYELLOW_EX + "|  " + Fore.RESET
                
        for i, char in enumerate(screen):
            if i > 1 and i < 10:
                for pos, ch in enumerate(screen[i]):
                    if pos == 2:
                        screen[i][pos] = Fore.LIGHTYELLOW_EX + "  |" + Fore.RESET
                        
        for i, char in enumerate(screen[-2]):
            if i > 0 and i < 5:
                screen[-2][i] = Fore.LIGHTMAGENTA_EX + "¯¯¯" + Fore.RESET
            if i == 0:
                screen[-2][i] = Fore.LIGHTMAGENTA_EX + "  |" + Fore.RESET
            if i == 5:
                screen[-2][i] = Fore.LIGHTMAGENTA_EX + "|  " + Fore.RESET 
        for i, char in enumerate(screen[-1]):
            screen[-1][i] = Fore.GREEN + "¯¯¯" + Fore.RESET       
        
        if error1 == True:
            screen[3][7] = self.error1()
        if error2 == True:
            screen[4][7] = self.error2()
        if error3 == True:
            screen[4][6] = self.error3()
        if error4 == True:
            screen[4][8] = self.error4()
        if error5 == True:
            screen[5][6] = self.error5()
        if error6 == True:
            screen[5][7] = self.error6()
            
              
        return screen
    
    def convertString(self, screen):
        screen_str = ""
        for row in screen:
            for column in row:
                screen_str += column
            screen_str += "\n"
            
        return screen_str
    
    
    def error1(self):
        error1 = Fore.LIGHTWHITE_EX + "O  " + Fore.RESET
        return error1
    def error2(self):
        error2 = Fore.YELLOW + "|" + Fore.RESET
        return error2
    def error3(self):
        error3 = Fore.YELLOW + "  /" + Fore.RESET
        return error3
    def error4(self):
        error4 = Fore.YELLOW + "\\  " + Fore.RESET
        return error4
    def error5(self):
        error5 = Fore.BLUE + "  /" + Fore.RESET
        return error5
    def error6(self):
        error6 = Fore.BLUE + " \\  " + Fore.RESET
        return error6
    
    