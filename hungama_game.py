import random

# List of 5 predefined words
words = ["python", "game", "computer", "college", "coding"]

# Select a random word
word = random.choice(words)

# To keep track of guessed letters
guessed_word = ["_"] * len(word)

# Maximum wrong attempts
max_attempts = 6
attempts = 0

print("🎯 Welcome to Hungama Game 🎯")
print("Guess the word! You have", max_attempts, "wrong attempts.\n")

# Game loop
while attempts < max_attempts and "_" in guessed_word:
    print("Word:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("✅ Correct guess!\n")
    else:
        attempts += 1
        print("❌ Wrong guess! Attempts left:", max_attempts - attempts, "\n")

# Check win or lose
if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("😢 Game Over! The word was:", word)
