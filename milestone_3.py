import random
# import milestone_2



# if guess in milestone_2.word:
#     print(f"Good guess! {guess} is in the word.")
# else:
#     print(f"Sorry, {guess} is not in the word. Try again.")

word_list = ['apple', 'banana', 'cherries', "strawberries", "mango"]
word = random.choice(word_list)



def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Please guess a letter")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()