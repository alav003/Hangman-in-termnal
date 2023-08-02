import random
import string
from words import words

def get_valid_word(words_list):
    word = random.choice(words_list)
    while '-' in word or ' ' in word:
        word = random.choice(words_list)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word.upper())
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print('You have used these letters:', ', '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word.upper()]
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used that letter. Please try again.')
        else:
            print('Invalid character. Please try again.')

        if set(word.upper()) == used_letters:
            break

    if len(word_letters) == 0:
        print('Congratulations! You guessed the word:', word.upper())
    else:
        print('Sorry, you ran out of attempts. The word was:', word.upper())

if __name__ == "__main__":
    hangman()

