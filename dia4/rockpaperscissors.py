import random

print("Welcome to the rockpaperscissors game!")
print(" 0 for Rock | 1 for Paper | 2 for Scissors ")
electionplayer=int(input())
electionPC=random.randint(0,2)

if electionplayer==electionPC:
    print(f"Player chose {electionplayer}")
    print(f"Computer chose {electionPC}")
    print("It's a tie!")
elif electionplayer==0 and electionPC==1:
    print(f"Player chose {electionplayer}")
    print(f"Computer chose {electionPC}")
    print("Computer wins!")
elif electionplayer==0 and electionPC==2:
    print(f"Computer chose {electionPC}")
    print(f"Player chose {electionplayer}")
    print(f"Player wins!")
elif electionplayer==1 and electionPC==0:
    print(f"Computer chose {electionPC}")
    print(f"Player chose {electionplayer}")
    print(f"Player wins!")
elif electionplayer==1 and electionPC==2:
    print(f"Computer chose {electionPC}")
    print(f"Player chose {electionplayer}")
    print(f"Computer wins!")
elif electionplayer==2 and electionPC==0:
    print(f"Computer chose {electionPC}")
    print(f"Player chose {electionplayer}")
    print(f"Computer wins!")
elif electionplayer==2 and electionPC==1:
    print(f"Computer chose {electionPC}")
    print(f"Player chose {electionplayer}")
    print(f"Player wins!")
else:
    print(f"Choose a valid option!")