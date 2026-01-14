#multiplication function
def multiply(a, b):
    return a * b
#addition function 
def add(a, b):
    return a + b
    
#subtraction function
def subtract(a, b):
    return a - b
    
#division function
def divide(a,b):
    return a/b


def square(a):
    return a ** 2

def cube(a):
    return a ** 3

input_number = int(input("Enter a number"))
n = int(input("Enter the power to which you want to raise the number"))
def square_n(input_number, n):
	return input_number ** n

for i in range(n):
     result = square_n(input_number, n)
     print(input_number, "raised to the power of", n, "is", result )



print("I am going to use the calculator to square 5 ")
sq = square(5)
print(sq)

print("I will now cube 14")
cb = cube(14)
print(cb)

print("I'm going use the calculator functions to multiply 7 and 8")
x = multiply(7,8)
print(x)

print("I am going to use the calculator to add 13 and 48")
y = add(13,48)
print(y)

print("I am going to use the calculator to subract 988 from 2050")
s = subtract(2050,988)
print(s)

print("I am finally going to use the calculator to divide 100 by 4")
d = divide(100,4)
print(d)

