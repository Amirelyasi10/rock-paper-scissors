from random import choice
from colorama import Fore

def rock_paper_scissors(round):
    print(f"{Fore.RED + 'Rock Paper Scissors' + Fore.RESET}\n{'-' * 10}")
    
    user_point = 0
    computer_point = 0
    
    moves_list = ["rock", "paper", "scissors"]
    while round:
        
        while True:
            
            # move info 
            for index, move in enumerate(moves_list, 1):
                print(index, move)
                
            # user move
            user_move = input("Enter a move: ").lower()
            if user_move in moves_list:
                break
            else:
                print("Enter a valid move !")
            print()
        
        # computer move
        computer_move = choice(moves_list)
        
        # show user move and computer move
        print(f"\nuser move: {user_move}\ncomputer move: {computer_move}")
        
        # The moves are checked and points are given to the winner
        if user_move == computer_move:
            print(f"{Fore.CYAN + 'The game was tie.' + Fore.RESET}")
        
        elif user_move == "rock":
            if computer_move == "paper":
                print(f"{Fore.RED + 'The computer won.' + Fore.RESET}")
                computer_point += 1
            elif computer_move == "scissors":
                print(f"{Fore.GREEN + 'The user won.' + Fore.RESET}")
                user_point += 1
                
        elif user_move == "paper":
            if computer_move == "scissors":
                print(f"{Fore.RED + 'The computer won.' + Fore.RESET}")
                computer_point += 1
            elif computer_move == "rock":
                print(f"{Fore.GREEN + 'The user won.' + Fore.RESET}")
                user_point += 1
        
        elif user_move == "scissors":
            if computer_move == "rock":
                print(f"{Fore.RED + 'The computer won.' + Fore.RESET}")
                computer_point += 1
            elif computer_move == "paper":
                print(f"{Fore.GREEN + 'The user won.' + Fore.RESET}")
                user_point += 1
                
        round -= 1
        print()
        
    else:
        print("Finish game...")
        print(f"\nuser point: {user_point}\ncomputer point: {computer_point}")
        
        if user_point == computer_point:
            print(f"{Fore.CYAN + 'The game was tie.' + Fore.RESET}")
        elif user_point > computer_point:
            print(f"{Fore.GREEN + 'The user won.' + Fore.RESET}")
        elif user_point < computer_point:
            print(f"{Fore.RED + 'The computer won.' + Fore.RESET}")

    
game_round = int(input("How many rounds do you want to play? "))
rock_paper_scissors(game_round)   