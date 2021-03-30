import random

# retunrs a random float number between 0 and 1
x = random.random()
print(x)

# [start, stop)
x = random.randrange(1,3)
print(x)

# [start, stop]
# is an alias for randrange(start, stop+1)
x = random.randint(1,9)
print(x)

# takes a sequence and returns the sequences in a random order
x= [1,2,3]
random.shuffle(x)
print(x)

# returns a random selement from the given sequence
x = [1,2,3,5,'b','m']
y = random.choice(x)
print(y)

# return a list with 14 items, there should be 10 times higher possibility to select 'apple' than the other two
x = ['apple','banana','cherry']
y = random.choices(x, weights=[10,1,1], k=14)
print(y)