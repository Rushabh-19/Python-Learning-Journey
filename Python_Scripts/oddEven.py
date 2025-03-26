i = int(input('Enter a number:'))
while True:
    if i % 2 == 0:
        print("The number is even")
        break
    elif i % 2 != 0:
        print("The number is odd")
        break
    else:
        print('please enter a proper number')
        continue
