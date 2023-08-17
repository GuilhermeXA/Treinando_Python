num1 = int(input())
num2 = int(input())
for i in range(num1, num2):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
