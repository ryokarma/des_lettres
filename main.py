def timer(time_left):
    import time
    while time_left > 0:
        print(f"Temps restant : {time_left}sec")
        time_left -= 5
        for i in range(5):
            time.sleep(1)
            print(".", end="", flush=True)
    print("Temps écoulé !")

import random

def generate_consonant():
    consonants = "bcdfghjklmnpqrstvwxz"
    return random.choice(consonants)

def generate_vowel():
    vowels = "aeiouy"
    return random.choice(vowels)

letters = ""
counter_letter = 0

def make_choice():
    choice_letter = input("Tapez 1 pour obtenir une consonne, ou 2 pour obtenir une voyelle :")
    if choice_letter == "1":
        return generate_consonant()
    elif choice_letter == "2":
        return generate_vowel()
    else:
        print("Merci de taper uniquement 1 ou 2.")
        return make_choice()

while counter_letter < 10:
    letter = make_choice()
    if letter:
        letters += letter
        counter_letter += 1

print(letters)
timer(30)

proposal = input("Quel est le mot le plus long que vous pouvez écrire avec ces lettres ?")
if proposal
