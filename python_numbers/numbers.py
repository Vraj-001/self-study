# there are three types of numbers "int", "float", "complex"

#int or integer is a whole number, positive or negative, without decimals, of unlimited leangth
x = 1

#float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#float can also be scientific numbers with an "e" to indicate the power of 10
y = 2.8

#complex numbers are written with a "j" as the imaginary part
z = 1j

#convert int to float
a = float(x)

#convert float into int
b = int(y)

#convert int to complex
c = complex(z)

print(a)
print(b)
print(c)

print(type(x))
print(type(y))
print(type(z))

#Random number:- python does not have random() function to make a random number, but python has a built-in module called random that cna be used to make random numbers:
import random
print(random.randrange(1, 10))