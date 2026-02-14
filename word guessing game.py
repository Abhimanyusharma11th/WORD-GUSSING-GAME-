import random

balance = 10  # starting money 💵

def play_game():
    global balance

    print("Select Level:")
    print("1. Easy 😊 (1 - 50, 7 chances)")
    print("2. Medium 🤔 (1 - 75, 10 chances)")
    print("3. Hard 🙄 (1 - 100, 10 chances)")

    choice = int(input("Enter choice (1/2/3): "))

    if choice == 1:
        max_no = 50
        chances = 7
        level = "Easy"
    elif choice == 2:
        max_no = 75
        chances = 10
        level = "Medium"
    elif choice == 3:
        max_no = 100
        chances = 10
        level = "Hard"
    else:
        print("Invalid choice")
        return

    secret = random.randint(1, max_no)
    guessed = False

    print(f"\n{level} Mode Started")
    print(f"Number range: 1 to {max_no}")
    print(f"Total chances: {chances}")
    print(f"Current balance: ₹{balance}")

    for attempt in range(1, chances + 1):
        print(f"\nChance {attempt}/{chances}")
        guess = int(input("Guess the number: "))

        if guess == secret:
            print("Correct guess!")
            guessed = True

            # Hard mode reward rule
            if level == "Hard" and attempt <= 8:
                balance += 20
                print("You won ₹20 bonus (Hard mode under 8 chances)")
            break
        elif guess < secret:
            print("Too low")
        else:
            print("Too high") 

        # After 8 failed attempts in hard mode
        if level == "Hard" and attempt == 8 and not guessed:
            print("\n8 chances over!")
            if balance >= 10:
                buy = input("Buy extra chances for ₹10? (y/n): ").lower()
                if buy == 'y':
                    balance -= 10
                    print("Extra chances bought. Balance:", balance)
                else:
                    balance -= 5
                    print("₹5 deducted. Balance:", balance)
                    break
            else:
                balance -= 5
                print("Not enough money. ₹5 deducted. Balance:", balance)
                break

    if not guessed:
        print("\nYou lost!")
        print("The number was:", secret)

    print("Final Balance: ₹", balance,"💰💵")


play_game()
