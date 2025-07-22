def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

print(celsius_to_fahrenheit(25))
print(fahrenheit_to_celsius(77))
print(celsius_to_kelvin(25))
print(kelvin_to_celsius(298.15))
print(fahrenheit_to_kelvin(77))
print(kelvin_to_fahrenheit(298.15))
