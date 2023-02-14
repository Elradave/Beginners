print('Calculator By Elradave')
print('''This is a basic Calculator. Please do not incluse Logs or indices.
eg. 2 x 2 ''')
while True:
    math = input("> ")
    import Operation
    math.split(' ')
    first_number = int(math.split()[0])
    op = math.split()[1]
    second_number = int(math.split()[2])
    sol = Operation.Arithmetics(first_number, second_number)
    if op == '+':
        ans = Operation.Arithmetics.plus(sol)
        print(ans)
    elif op == '-':
        ans = Operation.Arithmetics.minus(sol)
        print(ans)
    elif op == '/':
        ans = Operation.Arithmetics.divide(sol)
        print(ans)
    elif op == '*':
        ans = Operation.Arithmetics.times(sol)
        print(ans)
    elif op == 'x':
        ans = Operation.Arithmetics.times(sol)
        print(ans)
    elif op == ' ':
        print('Please Delete a space')
    else:
        print('Invalid Operation')

