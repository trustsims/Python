#GreetUser
def greet_user(username):
    """Display a simple greeting."""
    print("Ni Hao, " + username.title() + "!")

greet_user('Jesse')
greet_user('Trust')
print("...\n")

#TheAddition
def  add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2

    return num3

#Driver Code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
print("...\n")

#Some More Functions
def is_prime(n):
    if n in [2,3]:
        return True
    if (n == 1) or (n%2 ==0):
        return False
    r = 3
    while r * r <= n:
        if  n % r == 0:
            return False
        r += 2
    return True
print(is_prime(78), is_prime(79))
print("...\n")

#TRY_IT_YOURSELF
#Message
def display_message(Audience):
    """Display an Announcement"""
    print( Audience.title() + ", I am learning about this Chapter!")

display_message('William S. Cleveland')
display_message('Guido Vas Rossum')
print("...\n")

#Favorite_Book
def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(f"One of my favorite books is " + title.title() + "!")
favorite_book('Atomic Habits')
favorite_book('Richest Man in Babylon')