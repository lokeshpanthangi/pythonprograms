squares = [i * i for i in range(0,10)]
print(squares)
evens = [i for i in range(1,10) if i % 2 == 0]
print(evens)
pairs = [(x,y) for x in range(2) for y in range(3)]
print(pairs)