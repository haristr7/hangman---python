import random
from hangman_art import logo
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
word_len = len(chosen_word)
print("The Chosen Word Is: {}".format(chosen_word))
loop_countinues = True
lives = 6

display = []
for word in chosen_word:
    display.append("_")
print(display)

while loop_countinues:
    guess = input("Guess A Letter?: ").lower()

    for word in range(word_len):
        letter = chosen_word[word]

        if guess == letter:
            display[word] = letter

    if guess not in chosen_word:
        lives -=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    if lives == 0:
        print("Game Over!")
        loop_countinues = False
        
    print(f"{' '.join(display)}")

    if "_" not in display:
        loop_countinues = False
        print("We Won Maara!!")
    from hangman_art import stages
    print(stages[lives])
    
