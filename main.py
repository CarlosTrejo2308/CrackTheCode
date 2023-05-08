import random
import time

def getCode(length = 4):
    if length > 9:
        raise "Length cannot be greater than 9"

    numbers = [i for i in range(10)]

    code = []
    while length:
        idx = random.randint(0, len(numbers) - 1)
        number = numbers.pop(idx)
        code.append(number)
        length -= 1
    return code

def getUserAttempt(length = 4):
    while True:
        rawInput = input("Try: ")
        if len(rawInput) != length:
            print("Error. Length of code should be: ", length)
            continue

        userGuess = []
        for _ in range(length):
            try:
                userGuess.append(int(rawInput[0]))
                rawInput = rawInput[1:]
            except:
                print("Something went wrong, make sure to only use numbers!")
                break
        return userGuess

def compareCode(guess, code):
    if len(guess) != len(code):
        raise "Code and user guess are not the same length!"

    if guess == code:
        printHints(guess, [bcolors.OKAY]*len(guess))
        return True
    colors = []
    for i in range(len(code)):
        guessNum = guess[i]
        codeNum = code[i]

        if guessNum == codeNum:
            colors.append(bcolors.OKAY)
        elif guessNum in code:
            colors.append(bcolors.MISS)
        else:
            colors.append(bcolors.RED)

    printHints(guess, colors)
    return False

def printHints(guess, colors):
    for num, color in zip(guess, colors):
        print(f"{color}{num}{bcolors.ENDC}", end=" ")
    print()

def game():
    LENGTH = 4
    print("_ " * LENGTH)
    code = getCode()

    attempts = 0
    startTime = time.time()

    while True:
        guess = getUserAttempt()
        win = compareCode(guess, code)
        if win:
            endTime = time.time()
            break
        attempts += 1
    print("You won!")

class bcolors:
    OKAY = '\033[92m'
    MISS = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

game()
# print(f"{bcolors.OKAY}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
