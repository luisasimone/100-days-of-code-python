import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

word_guess = ["_"] * len(chosen_word)

game_over = False
lives = 6

print(hangman_art.logo)

while not game_over:
    print("".join(word_guess))
    letter_guess = input("Guess a letter: ").lower()

    if letter_guess in word_guess:
        print(f"You've already guessed {letter_guess}")

    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == letter_guess:
                word_guess[i] = letter_guess
            print(hangman_art.stages[lives])

        if letter_guess not in chosen_word:
            lives -= 1
            print(f"You guessed {letter_guess}, that's not in the word. You lose a life.")
            print(hangman_art.stages[lives])
            print(f"You have {lives} lives left.")

        if lives == 0 or ("".join(word_guess)) == chosen_word:
            game_over = True

if "_" not in word_guess:
    print("You win!")
else:
    print(f"You lose! The word was {chosen_word}")


