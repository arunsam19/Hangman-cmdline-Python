import random
#import this

def formWord(word, displayWord, letters):
    for letter in letters:
        positions = [pos for pos, char in enumerate(word) if char == letter]
        for pos in positions:
            displayWord = displayWord[:pos] + letter + displayWord[pos+1:]
    return displayWord

def play_hangman():
    nrOfAttempts = 5
    minWordLength = 4
    bGuessWord = 'y'
    totalFailedAttempts = int(input("How many incorrect attempts you want? "))
    guessedAttempts = 0
    allWords = ['Tester', 'Black', 'Table', 'Duster', 'Pillow', 'House', 'Bike', 'Temple', 'Sheet', 'Laptop', 'Hill', 'Window', 'Mobile', 'Sheep', 'Pillar', 'Train']

    while bGuessWord.lower() == 'y':
        word = random.choice(allWords)
        allWords.remove(word)
        wordLength = len(word)
        displayWord = wordLength * '*'
        lettersGuessed = []
        guessedAttempts = 0
        print("\n")
        while guessedAttempts < totalFailedAttempts:
            print("Word's guess status: " + displayWord)
            print("Attempts remaining: " + str(totalFailedAttempts - guessedAttempts))
            print("Previously guessed failed letters: " + ' '.join(lettersGuessed))
            #lastGuessedLetter = input("Guess a letter: ")
            lastGuessedLetter = input("Guess a letter: ")
            while lastGuessedLetter in lettersGuessed:
                print("Already tried this letter. Guess the letter again.")
                lastGuessedLetter = input("Guess a letter: ")
            while len(lastGuessedLetter) > 1:
                lastGuessedLetter = input("More than a single character is entered. Guess the letter again: ")
            casePair = [lastGuessedLetter, lastGuessedLetter.swapcase()]
            if lastGuessedLetter in word or lastGuessedLetter.swapcase() in word:
                print(lastGuessedLetter + " is in the word\n")
            else:
                print(lastGuessedLetter + " is NOT in the word\n")
                guessedAttempts += 1
                lettersGuessed.append(lastGuessedLetter)
            displayWord = formWord(word, displayWord, casePair)
            if displayWord == word:
                print("The word is: {}".format(word))
                print("*********************************************")
                print("                 SUCCESS                     ")
                print("*********************************************")
                break
            elif guessedAttempts == totalFailedAttempts:
                print("Number of guesses reached maximum. Correct word is: {}. Better try next word".format(word))
                break
        bGuessWord = input(("Do you want to guess the next word (y/n) ?  "))
    print("Guessing game is over. Bye!")

if __name__ == '__main__':
    play_hangman()