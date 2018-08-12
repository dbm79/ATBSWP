# This program says hello world and asks for my name.

print('Hello world!')
print('What is your name?')     # ask for their name
myName = input()

print('It is good to meet you {}'.format(myName))

print('The length of your name is:')
print(len(myName))

print('What is your age?')       # ask for user age
myAge = input()

print('You will be {} in a year.'.format(int(myAge)+1))
