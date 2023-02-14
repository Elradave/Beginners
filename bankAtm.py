print('Welcome to Ogbonge Bank')
Total = 10000
menu = ''
menugo = False
print('Please enter Menu to start')
while menu != 'cancel' :
    if menugo == True:
        menu = 'menu'
        print('''1 - Deposit
2 - Withdraw
3 - Check Balance''')
    else:
        menu = input('> ').lower()
        if menu == 'menu':
            print('''1 - Deposit
2 - Withdraw
3 - Check Balance''')
            menugo = False
        elif menu == 'cancel' or menu == 'stop':
            print('Thank you for banking with us. We are the Ogbonge Bank in Nigeria')
            break
        else:
            print('Invalid Command')

    deposit = '1'
    withdraw = '2'
    bal = '3'
    while menu == 'menu' or menugo == True:
        menuop = input('> ')
        if menuop == deposit:
            print('Enter the amount you want to deposit: ')
            amnt = ''
            while amnt.lower() != 'cancel':
                amnt = input('> ')
                if amnt.isalpha() == True:
                    print('Invalid character. Only Digits allowed')
                else:
                    if amnt.lower() == '':
                        print('Please enter a Valid amount')
                    elif int(amnt) < 1 or int(amnt) == 1:
                        print('Minimum Depost is $2.')
                    elif amnt.lower() == 'cancel':
                        print('Operation Canceled')
                        print('Press enter to go back to Menu')
                        menugo = True
                        input('> ')
                        break
                    else:
                        Total = int(amnt) + Total
                        print(f'${amnt} successfully deposited')
                        print("Press Enter to go back to Menu")
                        menugo = True
                        input('> ')
                        break
            break
        elif menuop == withdraw:
            print('Enter the amount you want to Withdraw: ')
            amnt = ''
            while amnt.lower() != 'cancel':
                amnt = input('> ')
                if amnt.isalpha() == True:
                    print('Invalid character. Only Digits allowed')
                else:
                    if amnt.lower() == '':
                        print('Please enter a Valid amount')
                    elif int(amnt) > Total:
                        print('Insufficient Funds')
                        print('Back to menu')
                        menugo = True
                        break
                    elif int(amnt) < 1:
                        print('Minimum Withdrawal is $1.')
                    elif int(amnt) == Total:
                        print(f'Current Bal: ${Total}. Withdraw all?')
                        all = input('Yes / No: ').lower()
                        if all == "yes":
                            print(f'Withdrawal of {amnt} processing. Please wait')
                            time = range(1,5)
                            for unit in time:
                                print(unit * '.')
                            Total = Total - int(amnt)
                            print(f'Withdrawal of ${amnt} processed successfully.')
                            menugo = True
                            input('> ')
                            break
                        else:
                            print('''Operation Canceled.'
press enter to go to menu''')
                            menugo = True
                            input('> ')
                            break
                    elif amnt.lower() == 'cancel':
                        print('Operation Canceled')
                        print('Back to Menu')
                        menugo = True
                        break
                    else:
                        print('Please wait your withdrawal is being processed')
                        Total = Total - int(amnt)
                        time = range(1, 5)
                        for unit in time:
                            print(unit * '.')
                        print(f'Withdrawal of ${amnt} processed successfully')
                        print("Press Enter to go back to Menu")
                        menugo = True
                        input('> ')
                        break
            break
        elif menuop == bal:
            print(f'Available Balance is ${Total}')
            menu = 'menu'
            print("Press Enter to go back to Menu")
            menugo = True
            input('> ')
            break
        elif menuop.lower() == 'cancel':
            print('''Operation Canceled
Thank you for Banking with us''')
        else:
            print('Invalid Command')
            menugo = True
            break







