import random
from words import word_list

def word():
    pick_ran =random.choice(word_list)
    return pick_ran.upper()

def play(word):
    word_completion = "_" *len(word)
    guess = False
    guess_letter = []
    guess_word = []
    tries = 6
    print("Lets play Hangman")
    print(display_hangman(tries))#add function of hangman 
    print(word_completion)
    print("")
    while not guess and tries > 0:
        guessed = input("Please give a letter or word: ").upper()
        if len(guessed) == 1 and guessed.isalpha():
            if guessed in guess_letter:
                print(f"you alrady guesssed the letter {guessed}")
            elif guessed not in word:
                print(f'{guessed} is not in the word.')
                tries -= 1
                guess_letter.append(guessed)
            else:
                print(f"Good job {guessed} is in the word!")
                guess_letter.append(guessed)
                word_as_list = list(word_completion)
                indices = [i  for i , letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guessed
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guess = True
        elif len(guessed) == len(word) and guessed.isalpha():
            if guessed in guess_word:
                print(f"You already guessed the word {guessed}")
            elif  guess != word:
                print(f"{guessed} is not the word")
                tries -=1
                guess_word.append(guessed)
            else:
                print("Not a valid guess.")
            print(display_hangman(tries))
            print(word_completion)
            print("")

        if guess:
            print("Congrats,you've guessed the word! You Win!")
        else:
            print(f"Sorry try again you ran out of tries, and the word was {word}")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    words = word()
    play(words)
    while input("Play again? (Y/N)").upper() == "Y".upper():
        words = word()
        play(words)

if __name__ == "__main__":
    main()