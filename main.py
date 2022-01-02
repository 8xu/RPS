import art
from colorama import Fore
from random import randint
from os import system
from sys import exit

def clear(): # Clearing the screen after each round
    system('cls' or 'clear')

replay = 'Y'
while replay == 'Y' or 'y':
    clear()
    print(Fore.LIGHTMAGENTA_EX + art.welcome)
    choice = int(input(Fore.WHITE + '0 for Rock, 1 for Paper, 2 for Scissors: \n'))
    if choice == 0 or 1 or 2:
        if choice == 0: print(art.rock)
        elif choice == 1: print(art.paper)
        elif choice == 2: print(art.scissors)
    else: 
        print(Fore.WHITE + "Kindly enter an Valid Number 0 , 1 , 2 only")

    print(Fore.CYAN + 'Computer choice: \n' + Fore.WHITE)
    computer_choice = randint(0, 2)
    if computer_choice == 0: print(art.rock)
    elif computer_choice == 1: print(art.paper)
    elif computer_choice == 2: print(art.scissors)

    num = str(choice) + str(computer_choice)
    if num == '02' or num == '10' or num == '21': print(Fore.GREEN + 'You won!')
    elif num == '00' or num == '11' or num == '22': print(Fore.YELLOW + 'It\'s a tie')
    else: print(Fore.RED + 'You\'ve lost. Better luck next time.')
    replay = input(Fore.RESET + "Want to play again?\nType: 'Y' to play again. Type: 'N' to exit. \n")
    if replay == 'N':
        exit()
    clear()

## feel free to fork this repository and make your own version of the game!