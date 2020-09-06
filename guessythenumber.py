#GUESS the NUMBER GAME
print('Welcome to mast game of guess the number')
n = 18
number_of_guesses = 1
print("NOTICE:- sirf 9 chances hai.")
while(number_of_guesses<=9):
    guess_number = int(input("guess the number"))
    if guess_number<18:
        print("Bada number try karo.")
    elif guess_number>18:
        print("chota number try karo.")
    else:
        print("jabardast, aap jeet gaye.")
        print(number_of_guesses,"no.of guesses he took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
   print("Game Over")
        

