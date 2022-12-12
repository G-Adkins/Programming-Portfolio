# I started the code by adding the import random code
import random

# Next I had to create my lists with 8 words in each list so that there could be at least 500 different passwords
FOOD = ["tomato",  "onion", "pasta", "bread", "chocolate", "cheese", "pizza", "apple"]

COUNTRIES = ["brazil", "germany", "senegal", "latvia", "luxembourg", "canada", "morocco", "japan"]

ANIMALS = ["kangaroo", "koala", "cat", "panda", "dog", "shark", "sloth", "frog"]

# I had to keep asking the user for the number of passwords they needed until they entered a number between 1 and 24.
while True:
    try:
        n = int(input("How many passwords are needed? "))
        if n < 1 or n > 24:
            print("You need to pick a value between 1 and 24.")
        else:
            break
    except ValueError:
        print("You need to enter a number.")

# I then added the code that would put one word from each list together
print("Your passwords are:")
for i in range(1, n + 1):
    # Generate a random password
    food = random.choice(FOOD)
    countries = random.choice(COUNTRIES)
    animals = random.choice(ANIMALS)
    password = food + countries + animals
    # Display the password
    print(f"  {i}. {password}")
