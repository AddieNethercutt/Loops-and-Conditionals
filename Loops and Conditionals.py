# Choose a number between 1 and 10 and assign it to the variable secret.
secret = 7

# Select another number between 1 and 10 and assign it to the variable guess.
guess = 5

# Write the conditional tests to print the appropriate string.
if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")

# Assign True or False to the variables small and green.
small = True
green = False

# Write if/else statements to print which of these matches those choices: cherry, pea, watermelon, pumpkin.
if small and green:
    print("pea")
elif small and not green:
    print("cherry")
elif not small and green:
    print("watermelon")
else:
    print("pumpkin")

# Use a for loop to print the values of the list [3, 2, 1, 0].
values = [3, 2, 1, 0]
for value in values:
    print(value)

# Assign the value 7 to the variable guess_me, and the value 1 to the variable number.
guess_me = 7
number = 1

# Write a while loop that compares number with guess_me.
while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    number += 1

# Assign the value 5 to the variable guess_me.
guess_me = 5

# Use a for loop to iterate a variable called number over range(10).
for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
