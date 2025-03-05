print("odd numbers and even numbers within the limit you need")

limit = int(input("Enter a range of your odd and even list: "))

odd = [i for i in range(1, limit) if i % 2 == 1]
even = [i for i in range(1, limit) if i % 2 == 0]
print(f"Odd numbers:\n{odd}")
print(f"Even numbers:\n{even}")