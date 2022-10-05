total = 100
print ("The total is ", total)
total = total + 99
print ("The total is now", total)
total -= 1
print ("The total is", total)
total *= 4
print ("The total is", total)
total /= 2
print ("The total is", total)
total = 98.2
count = 5
numbers = [100, 199, 198, 792, 396.0]

average = sum(numbers)/len(numbers)

print("Average:", round(average,5))

print(type(False))
print(type(1000))
print(type(100.111))
print(type("Hello"))
print(type(True))
print(type(100 / 5))
print(type(100 // 5))

print (10 + 10)
print ("10 + 10")

print("ABC" * 10)
print("The operator (*) is printing the given string operand (ABC) ten times ")

name= input("What is your name?")
#("George")

address= input("What is your address?")
#("Leeds")

contact_information= input("What is your contact information?")
#("G.Adkins2335@student.leedsbeckett.ac.uk")


print(len(name))

#age = int(input("Enter your age: "))
#print("in one year your age will be", age + 1)


# ("This code doesn't work because an addition operator is trying to be added to a string type and interger type operand which cannot be done.")

age = input("What is your age")
age = int(age)
print("in one year your will be", age + 1)

age = input("Enter your age ")
age = int(age)

age= input("What is your birth year?")
age = int(age)
print(age * age)


# = "I would have "thought" you knew better!"

# This code does not work because there needs to be single quotation marks at the start


print("\t This is a line that starts with a tab \n \t \t This new line starts with two tabs")

print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\nHello There!\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

print("""This text spans three lines,
"and includes both single ('),
and double quotes ("). """)

surname ="Palin"
initial = surname[0]


print (surname [3])

#print (surname [10])
#IndexError: string index out of range

surname = "Palin"
last = surname[0]

print (surname [-2])

surname = "Palin"
print (surname [1:5])

print (surname [:4])

primes = list
primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

print (primes [:4])

names = list
names =["Tim", "Bill", "Graeme"]
print (names)

names.insert( 2, "George")
names.insert( 3, "Mike")

print (names)

nums =list
nums = [1,2,3] * 5
("It will show the list 5 times")
print (nums)
