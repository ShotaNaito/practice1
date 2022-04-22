import random

def judge(m, t):
    if m == t:
        return "Draw."
    if m == "rock":
        if t == "paper":
            return "Lose."
        else:
            return "Win."
    elif m == "paper":
        if t == "scissors":
            return "Lose."
        else:
            return "Win."
    elif m == "scissors":
        if t == "rock":
            return "Lose."
        else:
            return "Win."
    else:
        return "Fuck you."

while True:
    theirhand = random.choice(("rock", "paper", "scissors")) 
    myhand = input("Choose your hand.\n")
    print(f"Your hand is {myhand}.")
    print(f"Their hand is {theirhand}.")
    result = judge(myhand, theirhand)
    print(f"Result: {result}")
    if (result == "Win." or result == "Lose." or result == "Fuck you."):
        break
print("The end.")



