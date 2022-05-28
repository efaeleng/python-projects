def welcome():
    print('''Simple CLI Calculator''')
    
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
/ for division
* for multiplication
% for modulus
''')

    num_1 = int(input('Please enter the first number: '))
    num_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {}'.format(num_1, num_2), '=', num_1 + num_2)        

    elif operation == '-':
        print('{} - {}'.format(num_1, num_2), '=', num_1 - num_2)

    elif operation == '/':
        print('{} / {}'.format(num_1, num_2), '=', num_1 / num_2)

    elif operation == '*':
        print('{} * {}'.format(num_1, num_2), '=', num_1 * num_2)

    elif operation == '%':
        print('{} % {}'.format(num_1, num_2), '=', num_1 - num_2)

    else:
        print('Not a valid operator, please try again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

welcome()
calculate()
