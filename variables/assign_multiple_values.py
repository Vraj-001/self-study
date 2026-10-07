# python allows you to asign multiple values to multiple variables in one line:
x, y ,z = "Red", "blue", "green"
print(x)
print(y)
print(z)

# One value to multiple variables: you can assign same value to multiple variables
a = b = c = "black"
print(a)
print(b)
print(c)

# unpack a collection: if you have a collection of values in an list, tuple etc. python allows you to extract the values into variables. this is calles unpackign
fruits = ["apple", "banana", "mango"]
d, e, f = fruits
print(d)
print(e)
print(f)