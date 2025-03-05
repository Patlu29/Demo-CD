import random as ra

a = [i for i in range(10, 50, 10)]

print(f"choose a random number from below\n {a}")

num = int(input("Enter selected number: "))

rand_num = ra.choice(a)

if num == rand_num :
    print("you're correct..!")
else:
    print("number is wrong")
    print(f"the number is: {rand_num}")