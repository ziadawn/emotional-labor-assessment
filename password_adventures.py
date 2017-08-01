import random

alphabet_big = 'ABCDEFGHIJKLMNOPQRSTUVWXY'
alphabet_little = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
special_characters = '!@#$%&'

bucket = alphabet_big + alphabet_little + numbers + special_characters

# THIS IS SO UGLY RIGHT NOW

pw_length = input('How many characters do you need? ')
pw_length = int(pw_length)
#other_requirements = input('Do you have any other requirements? ')
uppercase_count = input('How many capital letters? ')
uppercase_count = int(uppercase_count)
number_count = input('How many numbers? ')
number_count = int(number_count)
special_count = input('How many special characters? ')
special_count = int(special_count)

'''
    command = input('what is your command? ')

    if command == 'done':
        break
    elif command == 'left':
        player_j -= 1
    elif command == 'right':
        player_j += 1
    elif command == 'up':
        player_i -= 1
    elif command == 'down':
        player_i += 1
'''

password = uppercase_count + number_count + special_count

i = 0
n = pw_length
password = ''
while i < n:
    password += random.choice(bucket)
    i = i + 1

print(password)


yes = ''
Yes = ''
y = ''


'''
if other_requirements == yes or Yes or y:
    uppercase_count = input('How many capital letters? ')
    uppercase_count = int(uppercase_count)
    number_count = input('How many numbers? ')
    number_count = int(number_count)
    special_count = input('How many special characters? ')
    special_count = int(special_count)
'''

# do i need random.choice above to import from my lists?
# do i need a break?

#else:
#    i = 0
#    n = pw_need1
#    password = ''
#    while i < n:
#        password += random.choice(bucket)
#        i = i + 1
#    print(password)


#i = 0
#n = pw_need1
#password = ''
#while i < n:
#    password += random.choice(bucket)
#    i = i + 1



'''
i = 0
guess = ''
while guess != target:  #can also have while True, then see line 11
    guess = input('Guess a number between 1 and 20: ')
    guess = int(guess)
    if guess == target:
        print('that\'s correct!') #if while True, add "break" to exit loop when true
    else:
        print('that\'s incorrect')
        if guess > target:
            print('too high')
        if guess < target:
            print('too low')
    i = i + 1
'''
