sum = reduce(lambda result, x: result + x, [0, 1, 2, 3, 4])
print sum
print reduce(lambda result, x: result + x, [0, 1, 2, 3, 4], 0)

sentences = ['Mary read a story to Sam and Isla.',
             'Isla cuddled Sam.',
             'Sam chortled.']

result = 0
for sentence in sentences:
    result += sentence.count('Sam')

print result

print reduce(lambda result, x: result + x.count('Sam'), sentences, 0)
