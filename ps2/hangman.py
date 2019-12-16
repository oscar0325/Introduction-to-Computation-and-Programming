# -*- coding: utf-8 -*-
# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter in letters_guessed:
            continue
        else:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    flag = 0
    if len(letters_guessed) == 0:
        result = '_' * len(secret_word)
        return result, flag
    else:
        if letters_guessed[-1] in secret_word:
            flag = 1

    result = ''
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += '_'

    return result, flag


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letter_list = list(string.ascii_lowercase)
    for letter in letters_guessed:
        letter_list.remove(letter)

    return ''.join(letter_list)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = []
    warnings_time = 3
    print("Welcome to the game Hangman!")
    print("I am thinking of a world that is {} letters long.".format(len(secret_word)))
    print("You have {} warnings left".format(warnings_time))
    i = 6
    while i:
        print('-*' * 20)
        print("You have {} guesses left".format(i))
        print("Avilable letters:{}".format(get_available_letters(letters_guessed)))
        letter = input("Please guess a letter:")
        if str.isalpha(letter) and len(letter) == 1 :
            if letter in letters_guessed:
                if warnings_time == 0:
                    i -= 1
                    print("Oops！ You've already guessed that letter. You now have no warnings:{}".format(result))
                else:
                    warnings_time -= 1
                print("Oops！ You've already guessed that letter. You now have {} warnings:{}".format(warnings_time, result))
            else:
                letter = str.lower(letter)
                if letter in ['a', 'e', 'i', 'o', 'u'] and not (letter in secret_word):
                    i -= 1
                letters_guessed.append(letter)
                result, flag = get_guessed_word(secret_word, letters_guessed)
                if flag:
                    print("Good guess:{}".format(result))
                else:
                    i -= 1
                    print("Oops! That letter is not in my word:{}".format(result))
        else:
            result, flag = get_guessed_word(secret_word, letters_guessed)
            if warnings_time != 0:
                warnings_time -= 1
                print("Oops! That is not a valid letter. You have {} warnings left:{}".format(warnings_time, result))
            else:
                i -= 1
                print("Oops！ You've already guessed that letter. You now have no warnings:{}".format(result))

        if is_word_guessed(secret_word, letters_guessed):
            print('_'*20)
            print("Congratulations, you won!")
            print("You total score for this game is:{}".format( i * len(set(secret_word))))
            return

    print("Sorry, you ran out of guesses. The  word was {}".format(secret_word))
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(my_word) == len(other_word):
        for letter1, letter2 in zip(my_word, other_word):
            if letter1 != '_':
                if letter1 == letter2:
                    continue
                else:
                    return False
            else:
                continue
        return True
    else:
        return False
                



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    words_match = []
    flag = 0
    for word in wordlist:
        if match_with_gaps(my_word, word):
            words_match.append(word)
            flag = 1
    if flag:
        print("Possible word matches are:\n {}".format(words_match))
    else:
        print("No matches found")
            



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
        letters_guessed = []
    warnings_time = 3
    print("Welcome to the game Hangman!")
    print("I am thinking of a world that is {} letters long.".format(len(secret_word)))
    print("You have {} warnings left".format(warnings_time))
    i = 6
    while i:
        print('-*' * 20)
        print("You have {} guesses left".format(i))
        print("Avilable letters:{}".format(get_available_letters(letters_guessed)))
        letter = input("Please guess a letter:")
        if str.isalpha(letter) and len(letter) == 1 :
            if letter in letters_guessed:
                if warnings_time == 0:
                    i -= 1
                    print("Oops！ You've already guessed that letter. You now have no warnings:{}".format(result))
                else:
                    warnings_time -= 1
                print("Oops！ You've already guessed that letter. You now have {} warnings:{}".format(warnings_time, result))
            else:
                letter = str.lower(letter)
                if letter in ['a', 'e', 'i', 'o', 'u'] and not (letter in secret_word):
                    i -= 1
                letters_guessed.append(letter)
                result, flag = get_guessed_word(secret_word, letters_guessed)
                if flag:
                    print("Good guess:{}".format(result))
                else:
                    i -= 1
                    print("Oops! That letter is not in my word:{}".format(result))
        elif letter == '*':
            result, flag = get_guessed_word(secret_word, letters_guessed)
            show_possible_matches(result)
        else:
            result, flag = get_guessed_word(secret_word, letters_guessed)
            if warnings_time != 0:
                warnings_time -= 1
                print("Oops! That is not a valid letter. You have {} warnings left:{}".format(warnings_time, result))
            else:
                i -= 1
                print("Oops！ You've already guessed that letter. You now have no warnings:{}".format(result))

        if is_word_guessed(secret_word, letters_guessed):
            print('_'*20)
            print("Congratulations, you won!")
            print("You total score for this game is:{}".format( i * len(set(secret_word))))
            return

    print("Sorry, you ran out of guesses. The  word was {}".format(secret_word))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    #hangman(secret_word)
    hangman_with_hints(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
