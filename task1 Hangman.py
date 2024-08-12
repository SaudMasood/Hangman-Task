#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def select_random_word():
    words = ["python", "programming", "hangman", "challenge", "code"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = select_random_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")
    print("Guess the word!")

    while attempts > 0:
        current_display = display_word(word, guessed_letters)
        if "_" not in current_display:
            print(f"Congratulations! You've guessed the word: {word}")
            break

        print(f"Word: {current_display}")
        print(f"Attempts remaining: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word:
            print(f"Good job! {guess} is in the word.")
            guessed_letters.append(guess)
        else:
            print(f"Sorry, {guess} is not in the word.")
            attempts -= 1
            guessed_letters.append(guess)

        if attempts == 0:
            print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman()


# In[ ]:




