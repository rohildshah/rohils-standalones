import time
    from random import randint
    score = 0
    correct_symbols = ["Rock", "Paper", "Scissors", "rock", "paper", "scissors"]
    win_loose_condition1 = ["Rock", "rock"]
    win_loose_condition2 = ["Paper", "paper"]
    win_loose_condition3 = ["Scissors", "scissors"]
    print("You have chosen Rock, Paper, Scissors.")
    time.sleep(1)
    print("\nChoose rock, paper, or scissors by typing in rock, paper, or scissors\n")
    time.sleep(1)
    while True:
        while True:
            connector = 0
            number = (randint(1,3))
            time.sleep(0.5)
            choose = input("\nType in your choice here: ")
            if choose in correct_symbols:
                connector = connector + 1
                break
            elif choose != correct_symbols: 
                print("That is not a valid answer.\n")
                time.sleep(0.5)
                print("Please try again.")
                time.sleep(0.5)
        if connector == 1:
            print("\n\n\nYou chose", choose)
            if number == 1:
                print("Computer chose Rock")
                if choose in win_loose_condition1:
                    print("\nYou Tied!\n")
                if choose in win_loose_condition2:
                    print("\nYou Win!\n")
                    score = score + 1
                    forward_yes_no = input("If you want to play again, type y. If not, type n")
                    if forward_yes_no == "n":
                        return
                if choose in win_loose_condition3:
                    print("\nYou Lost!\n")
                    score = score - 1
            if number == 2:
                print("Computer chose Paper")
                if choose in win_loose_condition1:
                    print("\nYou Lost!\n")
                    score = score - 1
                if choose in win_loose_condition2:
                    print("\nYou Tied!\n")
                if choose in win_loose_condition3:
                    print("\nYou Win!\n")
                    score = score + 1
                    forward_yes_no = input("If you want to play again, type y. If not, type n")
                    if forward_yes_no == "n":
                        return
            if number == 3:
                print("Computer chose Scissors")
                if choose in win_loose_condition1:
                    print("\nYou Win!\n")
                    score = score + 1
                    forward_yes_no = input("If you want to play again, type y. If not, type n")
                    if forward_yes_no == "n":
                        return
                if choose in win_loose_condition2:
                    print("\nYou Lost!\n")
                    score = score - 1
                if choose in win_loose_condition3:
                    print("\nYou Tied!\n")
            time.sleep(0.5)
            print("Your score is now:", score)
            time.sleep(2)
            a=3
            while a > 0:
                a = a - 1
                print("\nStarting new game....\n")
                time.sleep(0.5)



