import random
import os
import time

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}

def get_random_letter():
    return random.choice(list(MORSE_CODE_DICT.keys()))

def display_morse_chart():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Morse Code Chart:")
    for letter, code in MORSE_CODE_DICT.items():
        print(f"{letter}: {code}")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    score = 0
    rounds = 5
    allow_chart = False

    print("Welcome to the Morse Code Learning Mini Game!")
    print("You will be given 5 random letters to translate to Morse code.")
    print("Use '.' for dots and '-' for dashes. Good luck!\n")

    for i in range(rounds):
        letter = get_random_letter()
        correct_code = MORSE_CODE_DICT[letter]
        print(f"Round {i+1}: What is the Morse code for '{letter}'?")
        user_input = input("Your answer: ").strip()

        if user_input == correct_code:
            print("Correct!\n")
            score += 1
            allow_chart = False
        else:
            print(f"Incorrect. The correct answer is '{correct_code}'.\n")
            allow_chart = True

            if allow_chart:
                view_chart = input("Type 'hint' to view the Morse Code Chart for 3 seconds or press Enter to skip: ").strip().lower()
                if view_chart == 'hint':
                    display_morse_chart()
                allow_chart = False

    print(f"Game over! Your final score is {score} out of {rounds}.")

if __name__ == "__main__":
    play_game()
