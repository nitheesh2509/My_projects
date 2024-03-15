import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "kiwi", "strawberry", "pineapple", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Incorrect guess!")
            incorrect_guesses += 1
            print(f"Attempts left: {max_attempts - incorrect_guesses}")
            if incorrect_guesses >= max_attempts:
                print("Sorry, you've run out of attempts. The word was:", word)
                break
        else:
            print("Correct guess!")

        display = display_word(word, guessed_letters)
        print(display)

        if "_" not in display:
            print("Congratulations! You've guessed the word:", word)
            break

hangman()
