import random 
from Words import words 
import string


def get_valid_word(words):
    word = random.choice(words) # chooses something randomly from list
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # the letters in the word 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # the letters the user has guessed 

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # prints letters used
        # " ".join(["a", "b", "cd"]) --> "a b cd"
        print(f"You have {lives} lives remaining.\n")
        print("You have used these letters: ", " ".join(used_letters))
        # print("You have", lives, "lives left and you have used letters: ", " ".join(used_letters))

        # prints current word
        word_lists = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_lists), "\n")

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # takes away one life
                print("Letter is not in word.") 
        elif user_letter in used_letters:
            print("You have already used that character. Please try again")
        else: 
            print("Invalid character. Please try again.") 
        print()

    if lives == 0:
        print("You have died. The word was, " + word) 
    else:
        print("You have guessed the word, " + word)


hangman() 