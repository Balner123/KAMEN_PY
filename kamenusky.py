import random

# kamen, papir , nuzky
print("KAMENUSKY\n"
      "1 = kamen\n"
      "2 = papir\n"
      "3 = nuzky\n")

try_again = 'y'

while try_again == 'y' or try_again == '':
    pc = random.randint(1, 3)
    ai = input("zadej cislo (1-3) : ")

    if not ai.isdigit() or int(ai) not in [1, 2, 3]:
        print("Zadejte platné číslo (1-3)!")
        continue

    ai = int(ai)

    if (ai == 1 and pc == 3) or (ai == 2 and pc == 1) or (ai == 3 and pc == 2):
        print("YOU WIN !!!\n")
    elif ai == pc:
        print("DRAW !!!\n")
    else:
        print("YOU LOST !!!\n")

    print(f"pc => {pc}\n you => {ai}\n")

    try_again = input("Continue? (y/N) : ").lower()
