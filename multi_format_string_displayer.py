name = input()
age = int(input())
city = input()

# 1. Using % formatting
print("My name is %s, I am %d years old, and I live in %s." % (name, age, city))

# 2. Using .format() method
print("My name is {}, I am {} years old, and I live in {}.".format(name, age, city))

# 3. Using f-strings
print(f"My name is {name}, I am {age} years old, and I live in {city}.")
