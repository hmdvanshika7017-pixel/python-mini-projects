import random

print("Welcome to Number Guessing Game!")
print("Tumhare paas sirf 5 chances hain 😎")
print("-" * 30)

number = random.randint(1, 10)

for attempt in range(1, 6):  # 1 se 5 tak
    guess = int(input(f"Chance {attempt}/5 - Guess a number 1 to 10: "))
    
    if guess == number:
        print(f"Wow! You Won 🎉 {attempt} try me jeet gaye!")
        break  # Game khatam, jeet gaye
    elif guess < number:
        print("Thoda upar jao ⬆️")
    else:
        print("Thoda neeche aao ⬇️")
else:
    # Ye tab chalega jab 5 baar me sahi nahi hua
    print(f"Game Over! 😢 Sahi number tha: {number}")

print("Thanks for playing!")        