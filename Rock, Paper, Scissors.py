import random


def RockPaperScissors():
    computer = ""
    flag = True
    value = random.randint(1, 3)
    if value == 1:
        computer = "rock"
    elif value == 2:
        computer = "paper"
    elif value == 3:
        computer = "scissor"
    human = input("Choose Rock, Paper or Scissor: ").lower()
    print("Computer Chose: ", computer)
    while flag != False:
        if human == "rock" and computer == "paper":
            print("Paper eats Rock, you loose")
            flag = False
        elif human == "rock" and computer == "scissor":
            print("Rock breaks scissor, you win")
            flag = False
        elif human == "rock" and computer == "rock":
            print("Draw")
            flag = False
        elif human == "paper" and computer == "paper":
            print("Draw")
            flag = False
        elif human == "paper" and computer == "scissor":
            print("Scissor cuts Paper, you loose")
            flag = False
        elif human == "paper" and computer == "rock":
            print("Paper eats Rock, you win")
            flag = False
        elif human == "scissor" and computer == "paper":
            print("Scissor cuts Paper, you win")
            flag = False
        elif human == "scissor" and computer == "scissor":
            print("Draw")
            flag = False
        elif human == "scissor" and computer == "rock":
            print("Rock breaks scissor, you loose")
            flag = False


RockPaperScissors()
