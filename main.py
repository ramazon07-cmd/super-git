import random

n = random.randint(0, 10)
guess = int(input("0 dan 10gacha: "))

if n == guess:
    print("Topdingiz")
else:
    print("Topa olmadingiz")
