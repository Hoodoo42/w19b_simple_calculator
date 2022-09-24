

def add_numbers(num1, num2):
    result = num1 + num2


def multiply_numbers(num1, num2):
    result = num1 * num2


def minus_numbers(num1, num2):
    result = num1 - num2


def divide_numbers(num1, num2):
    result = num1 / num2


def chosen():
    user_choice = input('Choose equation type: ')
    user_choice = int(user_choice)

    if (user_choice == 1):
            user_first_number = input('Please pick a number: ')
            user_first_number = int(user_first_number)

            user_second_number = input('Please pick another number: ')
            user_second_number = int(user_second_number)
            
            result = add_numbers(user_first_number, user_second_number)
            print(result)

    elif (user_choice == 2):
            user_first_number = input('Please pick a number: ')
            user_first_number = int(user_first_number)
        
            user_second_number = input('Please pick another number: ')
            user_second_number = input(user_second_number)
            multiply_numbers(user_first_number, user_second_number)

    elif (user_choice == 3):
            user_first_number = input('Please pick a number: ')
            user_first_number = int(user_first_number)
            
            user_second_number = input('Please pick another number: ')
            user_second_number = int(user_second_number)
            
            minus_numbers(user_first_number, user_second_number)

    elif (user_choice == 4):
            user_first_number = input('Please pick a number: ')
            user_first_number = int(user_first_number)
            
            user_second_number = input('Please pick another number: ')
            user_second_number = int(user_second_number)
            divide_numbers(user_first_number, user_second_number)

    else:
            print('Please choose between option 1-4')
            user_choice = input('Choose equation type: ')


chosen()
