import random
import string

words = ['brand', 'hell', 'fans', 'crumble', 'inspiring', 'jett', 'treble', 'disguise', 'disc', 'bass', 'embed', 'crave', 'plane']

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        print("You have used these letters: ", ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        
        print("Current word: ", ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f"Letter is not in word. You have {lives} lives left")
            
        elif user_letter in used_letters:
            print("You have already used that letter. Please enter another one.")
            
        else:
            print("You didn't type a valid character.")
    if lives == 0:
        print("You died. The word was", word)
    else:
        print('You guessed the word', word)        
            
hangman()