#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""

    return letter in word

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""

    return word[spot] == letter

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""

    result = ""
    for i in range(5):
        if inSpot(myGuess[i], word, i):
            result = result + myGuess[i].upper()
        elif inWord(myGuess[i], word):
            result = result + myGuess[i].lower()
        else:
            result = result + "*"

    return result


def main():
    #Pick a random word from the list of all words
    with open("words.txt", 'r') as wordFile:
        content = wordFile.read()

    wordList = []
    for word in content.split("\n"):
        cleanWord = word.strip().lower()
        if len(cleanWord) == 5 and cleanWord.isalpha():
            wordList.append(cleanWord)

    todayWord = random.choice(wordList)

    #User should get 6 guesses to guess
    guessCount = 0
    guessed = False

    #Ask user for their guess
    #Give feedback using on their word:
    while guessCount < 6 and not guessed:
        myGuess = input("Enter a 5-letter guess: ").lower()

        if len(myGuess) != 5 or not myGuess.isalpha():
            print("Guess must be exactly 5 letters.")
            continue

        rating = rateGuess(myGuess, todayWord)
        print(rating)
        guessCount = guessCount + 1

        if myGuess == todayWord:
            guessed = True
            print("You guessed the word!")

    if not guessed:
        print("Out of guesses. The word was:", todayWord)





if __name__ == '__main__':
  main()
