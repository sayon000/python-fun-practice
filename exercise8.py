#Make a two-player Rock-Paper-Scissors game.

gameOver = False
p1Wins = 0
p2Wins = 0
decision = ""
p1Attack = ""
p2Attack = ""

print("Let's play rock paper scissors friends")
while not gameOver:
    p1Attack = input("Player 1, choose Rock, Paper, or Scissors: ")
    while p1Attack.lower() != "rock" and p1Attack.lower() != "paper" and p1Attack.lower() != "scissors":
        p1Attack = input("Oops, that was not right. Choose Rock, Paper, or Scissors: ")
    p1Attack = p1Attack.lower()
    p2Attack = input("Player 2, choose Rock, Paper, or Scissors: ")
    p2Attack = p2Attack.lower()
    while p2Attack.lower() != "rock" and p2Attack.lower() != "paper" and p2Attack.lower() != "scissors":
        p2Attack = input("Oops, that was not right. Choose Rock, Paper, or Scissors: ")
    p2Attack = p2Attack.lower()
    if p1Attack == p2Attack:
        print("Tie")
    elif p1Attack == "paper" and p2Attack == "rock":
        p1Wins+=1
        print("Player one wins")
    elif p1Attack == "rock" and p2Attack == "paper":
        print("Player two wins")
        p2Wins+=1
    elif p1Attack == "rock" and p2Attack == "scissors":
        print("Player one wins")
        p1Wins+=1
    elif p1Attack == "scissors" and p2Attack == "rock":
        print("Player two wins")
        p2Wins+=1
    elif p1Attack == "scissors" and p2Attack == "paper":
        print("Player one wins")
        p1Wins+=1
    elif p1Attack == "paper" and p2Attack == "scissors":
        print("Player two wins")
        p2Wins+=1
    else:
        print("THIS WAS NOT INTENDED")
    print("Player one wins: " + str(p1Wins) + " Player two wins: " + str(p2Wins))
    decision = input("Do you want to play again? Y/N: ")
    while decision.upper() != "Y" and decision.upper() != "N":
        decision = input("Incorrect input. Please type Y or N for your decision: ")
    if decision == "N":
        gameOver = True

print("Final Count: Player one wins: " + str(p1Wins) + " Player two wins: " + str(p2Wins))

