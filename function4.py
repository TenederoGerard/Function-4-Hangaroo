def isWordGuessed (secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):

   word = ""
   for i in secretWord:
        if i in lettersGuessed:
            word+= i
        else:
            word += "_"
   return word

def getAvailableLetters(lettersGuessed):

    alphabet= ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    letter = " "
    for i in alphabet:
        if i not in lettersGuessed:
            letter += i
    return letter 

def hangaroo(secretWord):
   
    print ("Welcome to the game, Hangaroo!")
    print ("The word is " + str(len(secretWord)) + " letters long.")
    lettersGuessed = ''
    guessesLeft = 4
    print ("________________________")
    while True:
        print ("You have " + str(guessesLeft) + " guesses left.")
        print ("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess in lettersGuessed:
            print ("You have already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            print ("That letter is not in the word: " + getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1
        print ("________________________")
        if guessesLeft <= 0:
            print ("Sorry, Better luck next time. The word was " + secretWord)
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print ("Congratulations! You've won!")
            break
