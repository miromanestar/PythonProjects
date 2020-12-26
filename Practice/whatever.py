print("Please give a number between 1 and 10")
input1 = int(input())

if(1 < input1 < 10):
    for i in range(input1, 100):
        if(i != 56):
            print(i, end=" ")
        else:
            print('\033[92m', 56 - input1, '\033[0m', end=' 5')
