import random
user_score = 0
computer_score = 0
play_count = 0
print("AAJAO...STONE,PAPER,SCISSOR, khelte hain!")
opt = ["s", "p", "r"]


for i in range(6):
   # play_count += 1
    computer_turn = random.choice(opt)
    user_turn = input("Option choose karle bro:\n's' - Stone\n'p' - Paper\n'r' - Sissor\n-->")
    if user_turn == "s" or user_turn == "S":
        if computer_turn == "s":
            print("Ohhh,  it's a TIE..!")
        elif computer_turn == "p":
            user_score += 1
            print("is baar jeet gaya! ruk batata hu tujhe")
        else:
            computer_score += 1
            print("Dekh haar gaya na!")
    elif user_turn == "p" or user_turn == "P":
        if computer_turn == "s":
            user_score += 1
            print("jeet gaya ")
        elif computer_turn == "p":
            print("Ohhh, it's a TIE...!")
        else:
            computer_score += 1
            print("Bola tha harega tu")
    elif user_turn == "r" or user_turn == "R":
        if computer_turn == "s":
            computer_score += 1
            print("haarna toh tha hi tujhe")
        elif computer_turn == "p":
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

