"""
In my chatbot template, my program follows the following requirements:
Welcome the user, collect the users name and age, ask the user how it can help them, and allow
 the user to choose from a menu/list of options on how they can continue the conversation.
"""

def my_age_function(age):
    if age > 0 and age < 18:
        print(f'Oh my, {age}? Trying to start early huh?')
    elif age > 17 and age < 35:
        print(f'{age} was such a year to be alive...')
    elif age > 34 and age < 65:
        print(f'Everyone knows {age} is prime time! ')
    elif age > 64:
        print(f'Wow, {age}? Keep on kicking!')


print('Welcome to the ELite 101 chatbot project!')
name = input('What should we refer to you as? ')
age = int(input(f'Hello {name}! How old are you? '))
my_age_function(age)


print('\nPlease take a look at our following services below: ')
print('1. Placeholder one')
print('2. Placeholder two')
print('3. Placeholder three')
print('4. Exit program')
choice = int(input('How may we help you today? '))

if choice == 1:
    print('Placeholder one')
elif choice == 2:
    print('Placeholder two')
elif choice == 3:
    print('Placeholder three')
elif choice == 4:
    print(f'Thank you for using the program, goodbye {name}! ')
    #ends the program.