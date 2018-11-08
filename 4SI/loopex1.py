i = 0
total = 0

while i < 200:
    total += i**2
    i += 1
print(total)
print(i)

######################################

WORD = "perec"
MAX_ATTEMPT = 10

guess = None
attempt = MAX_ATTEMPT

while guess != WORD and attempt:
    guess = input("Guess the word:\n")
    if guess == WORD:
        break
    else:
        attempt -= 1
