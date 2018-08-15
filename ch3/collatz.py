def collatz(number):
    ''' Take a number and run it through collatz sequence '''

    if number % 2 == 0:
        print( number // 2 )
        return number // 2
    else:
        print( number * 3 + 1 )
        return number * 3 + 1

num = int(input("Please enter an integer: "))

while True:
    num = collatz(num)

    if num == 1:
        break
