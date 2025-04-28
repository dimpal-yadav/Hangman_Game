import random

def display_hangman(tries):
    stages = [
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |    
           |
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |    
           |
        ''',
        '''
           ------
           |    |
           |    O
           |   
           |    
           |
        ''',
        '''
           ------
           |    |
           |    
           |   
           |    
           |
        '''
    ]
    return stages[tries]

def get_word():
    words = ['python', 'developer', 'hangman', 'challenge', 'programming', 'algorithm', 'function']
    return random.choice(words)

def play_game():
    word = get_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("\n=== Welcome to Hangman ===")
    print(display_hangman(tries))
    print("Word: ", "_ " * len(word))

    while tries > 0 and word_letters:
        guess = input("\nEnter your guess (a single letter): ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter:", guess)
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            tries -= 1
            print(f"❌ Sorry, '{guess}' is not in the word.")
        
        print(display_hangman(tries))
        
        # Show word progress
        current_word = [letter if letter in guessed_letters else '_' for letter in word]
        print("Word: ", ' '.join(current_word))

    if not word_letters:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)

# Start the game
if __name__ == "__main__":
    play_game()
