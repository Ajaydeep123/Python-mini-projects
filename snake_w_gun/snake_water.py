import random

if yes_or_no("Wanna play snake, Water and gun?"):
    print("Noice  :D")
else:
    print("Haan bhot busy ho bhai")

user_score = 0
computer_score = 0
play_count = 0
print("Bohot badiya bro chalo khelte hain!")
opt = ["s", "w", "g"]


while play_count<6:
    play_count += 1
    computer_turn = random.choice(opt)
    user_turn = input("Option choose karle bro:\n's' - Snake\n'w' - Water\n'g' - Gun\n-->")
    if user_turn == "s" or user_turn == "S":
        if computer_turn == "s":
            print("Ohhh,  it's a TIE..!")
        elif computer_turn == "w":
            user_score += 1
            print("is baar jeet gaya! ruk batata hu tujhe")
        else:
            computer_score += 1
            print("Dekh haar gaya na!")
    elif user_turn == "w" or user_turn == "W":
        if computer_turn == "g":
            user_score += 1
            print("jeet gaya tu bhai ")
        elif computer_turn == "w":
            print("Ohhh, it's a TIE...!")
        else:
            computer_score += 1
            print("Bola tha harega tu")
    elif user_turn == "g" or user_turn == "G":
        if computer_turn == "w":
            computer_score += 1
            print("haarna toh tha hi tujhe")
        elif computer_turn == "s":
            user_score += 1
            print("jeet gaya bro,nooice!!")
        else:
            print("Ohhh, it's a TIE...!")
    else:
        print("Sahi value daal bhai, andho ki tarah kyu harkatein kar rha")

print("*" * 50)
if computer_score > user_score:
    print("i'm the OG, Jeetna meri adat hai brO")
    print("Your score: " + str(user_score) +"\nMy score: " + str(computer_score))
elif computer_score < user_score:
    print("congrats man! you won.")
    print("Your score: " + str(user_score) +"\nMy score: " + str(computer_score))
else:
    print("I am Shocked.. Ahhh... it's a TIE")


