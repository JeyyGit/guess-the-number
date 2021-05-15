import random

size = input("Number size: ")
while size.isnumeric() == False:
    print("Please input a proper number.")
    size = input("Number size: ")
#size = 10

lis = list(range(1, int(size) + 1))
rig = random.choice(lis)
#rig = 9
print(lis)
inp = 0
sco = 0

def acti(funci):
    lis.index(int(funci)) + 1
    return int(funci)
def actr(funcr):
    lis.index(rig)
    return funcr

while rig != int(inp):
    inp = input("Guess the number: ")
    if inp.isnumeric() == False:
        print("Please input a proper number: ")
    elif lis.count(int(inp)) < 1:
        print("That number is not on the list.")
    elif rig == int(inp):
        print("Your guess is right!")
        sco += 1
        print("You guessed " + str(sco) + " times.\n")
    elif actr(rig) - 2 < acti(inp) < actr(rig) + 2:
        print("Your guess is very very close.")
        sco += 1
        print("You guessed " + str(sco) + " times.\n")
    elif actr(rig) - 4 < acti(inp) < actr(rig) + 4:
        print("Your guess is very close.")
        sco += 1
        print("You guessed " + str(sco) + " times.\n")
    elif actr(rig) - 6 < acti(inp) < actr(rig) + 6:
        print("Your guess is close.")
        sco += 1
        print("You guessed " + str(sco) + " times.\n")
    else:
        print("Your guess is far.")
        sco += 1
        print("You guessed " + str(sco) + " times.\n")
