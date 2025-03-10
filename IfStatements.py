#pcc simple example
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else: 
        print(car.title())
print()
cities = ['cities','lusaka','harare','lilongwe',]
for city in  cities:
    if city == 'cities':
        print(city.upper())
    else:
        print(city.title())
print()

#Conditional Tests
#Checking For Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
#Numerical Camparisons
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
age = 19
if age != 21:
    print("True") 
#Checking Multiple Conditions
age_0 = 19
if age_0 != 22:
    print("True")
if age_0 <= 21:
    print("True")
if age_0 >= 21:
    print("True")
#IfStatement(CodeBasics)
num = input("Enter a Number:")
num = int(num)
if num%2==0:
    print("Number is even")
else: 
    print("Number is odd")    

     
