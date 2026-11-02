"""Hangman Game - a simple text-based word guessing game."""
import random

# List of 5 predefined words
WORDS = ["python", "hangman", "computer", "keyboard", "program"]
MAX_WRONG = 6


def play():
    word = random.choice(WORDS)          # random: pick a secret word
    guessed = []                         # list: letters guessed so far
    wrong = 0

    print("=== Welcome to Hangman! ===")
    print(f"The word has {len(word)} letters. You can make {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:             # while loop: keep playing
        # strings: build the display like  p _ t h _ n
        display = " ".join(ch if ch in guessed else "_" for ch in word)
        print("Word:", display)
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print("Guessed letters:", ", ".join(guessed) if guessed else "none")

        if "_" not in display:
            print(f"\nCongratulations! You guessed the word: {word}")
            return

        guess = input("Guess a letter: ").strip().lower()

        # if-else: validate and check the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
        elif guess in guessed:
            print("You already guessed that letter.\n")
        elif guess in word:
            guessed.append(guess)
            print("Good guess!\n")
        else:
            guessed.append(guess)
            wrong += 1
            print("Wrong guess!\n")

    print(f"Game over! The word was: {word}")


if __name__ == "__main__":
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break