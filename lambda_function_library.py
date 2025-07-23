from functools import reduce

square = lambda x: x ** 2
factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1)) if n > 0 else 1

reverse = lambda s: s[::-1]
uppercase = lambda s: s.upper()

filter_evens = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
sum_list = lambda lst: sum(lst)

num = int(input("Enter a number for square and factorial: "))
print("Square:", square(num))
print("Factorial:", factorial(num))

text = input("Enter a string: ")
print("Reversed String:", reverse(text))
print("Uppercase String:", uppercase(text))

lst_input = input("Enter a list of integers separated by spaces: ")
lst = list(map(int, lst_input.strip().split()))
print("Even numbers:", filter_evens(lst))
print("Sum of list:", sum_list(lst))
