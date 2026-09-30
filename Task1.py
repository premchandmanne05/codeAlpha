import random

# List of 5 predefined words
words = ["python", "computer", "programming", "keyboard", "developer"]

# Select a random word
word = random.choice(words)

guessed_letters = set()
wrong_guesses = 0
max_wrong_guesses = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while wrong_guesses < max_wrong_guesses:

    # Display guessed letters and blanks
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check if the word is completely guessed
    if all(letter in guessed_letters for letter in word):
        print("Congratulations!")
        print("You guessed the word:", word)
        break

    guess = input("Enter one letter: ").lower().strip()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter exactly one letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Incorrect guess!")

else:
    print("\nGame Over!")
    print("The correct word was:", word)