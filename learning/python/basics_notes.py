#formattedstrings
from importlib.metadata import files
from logging import StringTemplateStyle

first = 'John'
last = 'Smith'
msg = f'{first} [{last}] is a coder '
print(msg)

#stringmethods
course = 'Python For Beginners'
len(course) #number of characters in a string, general purpose function
course.upper() #converts string to uppercase
course.lower() #converts string to lowercase
course.find('p') #return index of first appearance of character, case-sensitive
course.replace('Beginners', 'Absolute Beginners') #replaces characters in a string
course.title() # capitalizes the first letter or each word in the string

print('Python' in course) # checking if string is in variable, returns True or False

#arithmetic operations
print(1/2) #float division
print(1//2) #int division (just shows the int value from the float ex. 0.5 -> 0)
print(3**2) #exponent
print(3%2) #remainder
#augmented assignment operator
x = 10
x += 3 #add 3, x = 13
x -= 3 #subtract 3, x = 10

#FOLLOW PEMDAS (ORDER OF OPERATION)

#mathfunctions
x = 2.9
round(x) #rounds to nearest int
abs(x) #absolute value

#math module
import math
math.ceil(2.9) #int rounding up, ex. 3
math.floor(2.9) #int rounding down, ex. 2

#if statements exercise
price = 1000000
credit = input('Is your credit good or bad? ')
down_payment = 0

if credit == 'good':
    down_payment += (0.10*price)
else:
    down_payment += (0.20*price)

print(f'Down Payment: ${down_payment}')

#whileloops
i=1
while i<=5:
    print(i)
    i+=1
print('Done')

#guessinggame
secret = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret:
        print('You Won!')
        break
else:
    print('You Lose!')

#forloops
for item in range(10):
    print(item)

#nestedloops
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

#exercise
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#2D Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

#listmethods
number = [5,2,1,7,4]
number.append(13) #adds item to the end of the list
number.insert(0,1) #adds item at certain index and pushes the other numbers to the right#number.remove(5) #removes item
number.pop() #removes last item in the list
number.index(5) # return index of first appearance of that item
number.count(5) #returns occurences of item
number.sort() #sorted in ascending order
numbers.reverse() #sorted in decsending order
numbers2 = numbers.copy() #so you have the original and the edited one

letters = ['a', 'b', 'g', 'f', 'b', 'a']
new_letters = []
for letter in letters:
    if letter not in new_letters:
        new_letters.append(letter)
print(new_letters)

#tuples and unpacking
coordinates = (1,2,3)
x, y, z = coordinates #unpacking, can be used for lists as well
print(x, y, z)

#dictionaries
customer = {
    'name': 'John Smith',
    'age' : 30,
    'is_verified' : True
}
print(customer['name'])
print(customer.get('name'))
print(customer.get('birthdate', 'Jan 1 1980'))

numbers = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

phone = input('Phone: ')
for num in phone:
    print(numbers.get(num), end = ' ')

#functions
def greet_user(first_name, last_name = 'Smith'): #if one has a parameter and the other doesnt, the parameter must be the second argument
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print('Start')
greet_user('John','Smith')
greet_user('Mary', 'Smith')
greet_user(last_name = 'Smith', first_name = 'John')
print('Finish')

def square(number):
    return number ** 2 #if you use print instead you will get the output 9 n\ None
print(square(3))

#exception
try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age can\'t be 0')
except ValueError:
    print('Invalid Value')

#classes
class Point: #defines new types
    def move(self):
        print('move')
    def draw(self):
        print('draw')

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()
point2 = Point() #different instance than point 1

#constructors
class Point:
    def __init__(self, x, y): #constructs/creates an object
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')
point = Point(10,20)
print(point.x) #prints 10

#exercise
class Person:
    def __init__(self, name): #takes the name parameter
        self.name = name

    def talk(self):
        print(f'Hi I am {self.name}!')


john = Person('John Smith')
john.name #prints John Smith
john.talk() #prints Hi I am John Smith!

bob = Person('Bob Smith')
bob.name # prints Bob Smith
bob.talk() #prints Hi I am Bob Smith!

#inheritance
class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    def bark(self):
        print('bark')

class Cat(Mammal):
    def meow(self):
        print('meow')

dog1 = Dog()
dog1.walk() #prints walk

cat1 = Cat()
cat1.meow() #prints meow

#modules
import _____.py #allows you to use functions of another file
#from converters import kg_to_lbs #does the same as above
#converters.function
________________________________________________________________
#packages: container for multiple modules, directory/file
#1. create a new directory/pythonpackage ex. ecommerce
#2. add a new python file to the directory named __init__, treats directory as package
#3. add new python file ex. shipping and in the module add all functions related to that section ex. calc shipping costs
#4. must import entire module, ex. ecommerce.shipping, ecommerce.shipping.calc_shipping(), from ecommerce.shipping import calc_shipping(), calc_tax(), from ecommerce import shipping
_________________________________________________________________
#generating random values
import random
for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20)) #random ints between 10 and 20

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members) #chooses random item in list
print(leader)

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second


dice = Dice()
print(dice.roll()) #prints (diceroll1, diceroll2) ex. (1,4)

#files and directories

#Absolute Path: path starting at root of hard disk ex. c:\Program Files\Microsoft
#Relative Path: path starting from current directory

#from pathlib import Path
#path = Path('ecommerce')
#path.exists(), shows if path is in the directory
#path.mkdir, return None, but creates a new directory
#path.rmdir, removes directory
#path = Path()
#print(path.glob('*'), shows all the files and directories in a given path
#path.glob('*.*'), only gives files no directories
#path.glob('*.py') gives only the py files, path.global('*.xls') gives all excel spreadsheets

#for file in path.glob('*.py')
    #print(file)



