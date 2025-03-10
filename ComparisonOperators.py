temperature = 30

if temperature  == 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

#EXERCISE
number_of_characters = 3

if number_of_characters < 3:
    print("Name must atleast be 3 characters")
if number_of_characters > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")

#RECAP
name = "TRUST"

if len(name) < 3:
    print("Name must atleast be 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")