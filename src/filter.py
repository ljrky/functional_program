print filter(lambda x: x > 5, [0, 6, 5, 8, 1, 2, 3])

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

people_with_height = filter(lambda x: 'height' in x, people)
print people_with_height
people_height = map(lambda x: x['height'], people_with_height)
print people_height
print reduce(lambda x, result: x + result, people_height, 0) / len(people_height)