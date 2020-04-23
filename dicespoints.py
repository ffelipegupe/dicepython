import random

def add(a):
    addition = 0
    for i in a:
        addition += i
    return addition

print("Roling a dice!")
a = []
x = input("Role? (yes/no): ")
while x == "yes":
    aux2 = 0
    aux = 0
    sum = 0
    number = random.randint(1,6)
    if number == 1:
        print("--------")
        print("   1   ")
        print("--------")
        sum += 1
    if number == 2:
        print("--------")
        print("   2   ")
        print("--------")
        sum += 2
    if number == 3:
        print("--------")
        print("   3   ")
        print("--------")
        sum += 3
    if number == 4:
        print("--------")
        print("   4   ")
        print("--------")
        sum += 4
    if number == 5:
        print("--------")
        print("   5   ")
        print("--------")
        sum += 5
    if number == 6:
        print("--------")
        print("   6   ")
        print("--------")
        sum += 6
    a.append(int(sum))
    print("Points so far:", add(a))
    x = input("Role again? (yes/no): ")
if x == "no":
    print("Total Points:", add(a))
    print("Thanks for using this dice!")
