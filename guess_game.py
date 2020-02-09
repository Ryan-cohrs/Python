secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        tries_left = guess_limit - guess_count
        print("You have " + str(tries_left) + " tries remaining.")
        guess = input("Enter guess:  ")
        guess_count += 1
    else:
        out_of_guesses = True

if guess == secret_word:
    print("You win!")
else:
    print("You lost!")