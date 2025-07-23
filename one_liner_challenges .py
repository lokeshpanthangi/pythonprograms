from functools import reduce

sus = reduce(lambda x, y: x+y,[i * i for i in range(1,11)])

red = reduce(lambda x, y: x + y, [1, 2, 3, 4])

ed = reduce(lambda x, y: x * y, [1, 2, 3, 4])

nums = [i*i for i in range(1, 11) if i % 2 == 0]

genz = list(map(str.capitalize, ['hello', 'world']))

print(red)
print(ed)
print(nums)
print(genz)
print(sus)