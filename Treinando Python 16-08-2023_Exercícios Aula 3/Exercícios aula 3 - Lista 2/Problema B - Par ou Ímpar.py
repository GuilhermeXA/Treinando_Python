repeticao = int(input())
for i in range(0, repeticao):
    num = int(input())
    if num == 0:
        print('NULL')
    elif num < 0:
        if num % 2 == 0:
            print('EVEN Negative')
        else:
            print('ODD Negative')
    else:
        if num % 2 == 0:
            print('EVEN Positive')
        else:
            print('ODD Positive')
