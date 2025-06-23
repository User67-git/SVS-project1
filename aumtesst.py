# === Libraries ===
import random
import time

#Functions
def intro():  
    print("Quest for $20,000")
    print("You're at Las Vegas Strip")

def LasVegasStrip():  
    print("\nChoose a Path:")

    # options
    print("\n1. Venetian Casino Resort (Plays Blackjack. Each ten players bet $2,000)")
    print("\n2. The Cosmopolitan (Roulette, each person has to bet on number, each player bets $300)")
    print("\n3. Nearest Gas Station (Play Slot Machine)")

    choice = input("> ")
    
    # return 
    if choice == "1":
        return blackjack()
    elif choice == "2":
        return roulette()
    elif choice == "3":
        return slot_machine()
    else:
        return LasVegasStrip()

def blackjack():  #blackjack
    print("\nYou have 1 king (Value = 10) and 1 ace (Value = 1). Do you want to hit?")
    
    # options
    print("\n1. Yes I want to hit.")
    print("2. No I don't want to hit.")
    
    choice = input("> ")
    if choice == "1":
        cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        hit_card = random.choice(cards)

        print("...")  
        time.sleep(2)  # dramatic pause

        print(f"You got a {hit_card}!")

        # return
        if hit_card in ["Jack","Queen","King"]:
            print("Blackjack! You acquire $20,000! Mission complete!")
            return True
        else:
            print("You did not get a black jack and the other oponent did..")
            print("You have fear to lose more money after what had happened, so you return to your investor losing $2,000.")
            return False

    elif choice == "2":
        print("...")
        time.sleep(2)  # dramatic pause
        print("\n9th player got blackjack. Loss of $2,000.")
        print("You have fear to lose more money after what had happened, so you return to your investor with losing $2,000.")
        return False
    else:
        return blackjack()

def roulette():  #roulette
    print("\nYou believe that 1 and 37 are lucky numbers... Choose which number to bet.")
    print("Pick a number between 1 and 37:")

    while True:
        choice = input("> ")
        if choice.isdigit() and 1 <= int(choice) <= 37:
            break
        print("Please enter a valid number between 1 and 37.")

    choice_num = int(choice)
    print("The wheel spins...")
    time.sleep(2)  # dramatic pause

    winning_number = random.randint(1, 37)
    print(f"...and lands on {winning_number}!")

    # return
    if choice_num == winning_number:
        print("It's your lucky day! You won around $22,800!")
        return True
    else:
        print(f"You lost. You keep betting and losing money until you lose around $1,000.")
        print("You have fear to lose more money, so you return to your investor losing around $1,000.")
        return False

def slot_machine():  #slot machine
    print("You believe today is a good day. So you purchase 3,333 tickets.")
    print("Pulling the lever...")
    time.sleep(2)  # dramatic pause

    win_chance = random.randint(1, 100)

    #return 
    if win_chance == 1:
        print("JACKPOT! You won $30,000!")
        return True
    else:
        print("You just wasted $3,333. You had enough, so you went back with shame.")
        return False

def game_loop():  # game loop
    intro()
    while True:
        success = LasVegasStrip()
        
        # return check
        if success:
            break

        retry = input("\nYou failed. Do you want to try again? (yes/no): ").strip().lower()
        if retry != "yes":
            print("You lost.")
            break

# make the game run
game_loop()

