import random
import os
computer = ['stone', 'paper', 'scissor']


def check_win(player, computer):
    # function to check conditions
    print("\t", player.capitalize(), "vs", computer.capitalize())
    if player == "stone" and c == "scissor":
        print("\t Player Wins")
    elif player == "scissor" and c == "paper":
        print("\t Player Wins")
    elif player == "paper" and c == "stone":
        print("\t Player Wins")
    elif player == c:
        print("\t Its a tie.")
    else:
        print("\t Computer Wins")


print("x~x~x~x~Stone-Paper-Scissor~x~x~x~x")
print("Let's Start")
while True:
    print("="*15)
    print("1:Stone\n2:Paper\n3:Scissor")
    ch = input("Enter choice or press 'q' to exit:")
    # os.system('clear')
    player = ""
    c = random.choice(computer)
    if ch == '1':
        player = "stone"
        check_win(player, c)
    elif ch == "2":
        player = "paper"
        check_win(player, c)
    elif ch == "3":
        player = "scissor"
        check_win(player, c)
    elif ch.lower() == "q":
        print("Game Over\nThanks for Playing...!!!")
        break
    else:
        print("Invalid choice....!")


# print("Computer Player")
# print("   1\t   2")
