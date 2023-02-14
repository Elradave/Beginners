
correct_pass = input('Create Your Password: ')
hackpass = ''
print('''Password Created successfully!!!


''')
while True:
    user_pass = (input('Please input your password to continue >>> '))
    if user_pass == correct_pass:
        print('Login successful')
        break
    else:
        print('''Incorrect Password
Do you wanna hack this device?
Yes/No''')
        password_hack = input('>> ')
        if password_hack.lower() == 'yes':
            import random
            import string

            while True:
                num = ''
                alpha = ''
                for digit in correct_pass:
                    for unit in range(100):
                        if digit.isalpha():
                            alpha = random.choice(string.ascii_letters.lower())
                            if alpha == digit:
                                print(f'{hackpass}{alpha}')
                                hackpass += alpha
                                print(f'Found Password>> {hackpass + " "}')
                                break
                            else:
                                print(f'{hackpass}{alpha}{num}')

                        elif digit.isnumeric():
                            num = str(random.randint(0, 9))
                            if num == digit:
                                print(f'{hackpass}{num}')
                                hackpass += num
                                print(f'Found Password>> {hackpass + " "}')
                                break
                            else:
                                print(f'{hackpass}{alpha}{num}')
                hackpass = ''
                break
        elif password_hack.lower() == 'no':
            print('Hacking Bot Deactivated')
        else:
            print('Invalid command!')
