import random

# Basically, this small program takes input from the user and compares it with randomly generated numbers.
# Depending on how many matches appeared between the two sets, the prize will be determined.

# x is for user's input set and y is for the random numbers. Loop iterates for z times. c holds the number input from the user for an iteration and so f does for random number.
x =[]
y = []
z = 12

print("###Welcome to Lotto Game###\nEnter 12 numbers from 1 to 24\nSee how many matches you have with the winning numbers")
print("Prizes as the following:\na- 1 or 12 matches: 50,000 $\nb- 2 or 11 matches: 10,000 $\nc- 3 or 10 matches: 1,000 $\nd- 4 or 9 matches: 100 $")
print("e- 5 or 8 matches: 10 $\nf- 6 or 7 matches: 0 $\n##One turn coasts 10 $, GOOD LUCK##")

while z > 0 :
    try:
        c = int(input('Enter a number from 1 to 24:'))
    except:
        print("Incorrect input")
        continue
    if c < 1 or c > 24:
        print("Your number is not within the range")
        continue
    if c in x:
        print("You already entered {}, please try another number.".format(c))
        continue
    f = random.randint(1,24)
    try:
        while f in y:
            f = random.randint(1,24)
    except:
        do_Nothing = 0
    x.append(c)
    y.append(f)
    print("{} number(s) left to enter".format(z-1))
    z -=1

print("Your numbers are\n{}".format(x))
print("winning numbers are\n{}".format(y))

# Finding how many matches between the two sets and assign it to the variable g
g = 0
for i in x:
    if i in y:
        g +=1

# The results
prize = ""
final_Message = "Congratulations,"
if g == 1 or g == 12:
    prize = "you won 50,000 $. Congratulations!!!"
    final_Message = "JACKPOT!!!"
elif g == 2 or g == 11: prize = "you won 10,000 $"
elif g == 3 or g == 10: prize = "you won 1,000 $"
elif g == 4 or g == 9: prize = "you won 100 $"
elif g == 5 or g == 8: prize = "you won 10 $"
else:
    final_Message = "You did not win this time! Better luck next time."

print("There are {} matches".format(g))
print(final_Message,prize)
