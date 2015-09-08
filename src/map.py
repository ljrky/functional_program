import random

name_lengths = map(len, ["keyu", "ruan", "chen", "haiyan"])
print name_lengths

squares = map(lambda x: x * x, [0, 1, 2, 3, 4])
print squares

names = ['Mary', 'isla', 'sam']
code_names = ['Mr.pink', 'Mr.orange', 'Mr.Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)
print names

names = ['Mary', 'isla', 'sam']
code_names = ['Mr.pink', 'Mr.orange', 'Mr.Blonde']

print map(lambda x: random.choice(code_names), names)

names = ['Mary', 'Isla', 'Sam']

for i in range(len(names)):
    names[i] = hash(names[i])

print names

names = ['Mary', 'Isla', 'Sam']
print map(lambda x: hash(x), names)
print map(hash, names)
