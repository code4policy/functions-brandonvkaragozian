#multiplication function
def multiply(a,b):
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

def square_n_times(a, n): 
    return a ** n
    for _ in range(n):
        result = square(result)
    return result
    
print("squaring 3 over 3 times")
n_times = square_n_times(3, 4)
print(n_times)

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



