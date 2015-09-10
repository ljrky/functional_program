from random import random

# procedure version
time = 5
car_positions = [1, 1, 1]

while time:
    # decrease time
    time -= 1

    print ''
    for i in range(len(car_positions)):
        # move car
        if random() > 0.3:
            car_positions[i] += 1

        # draw car
        print '-' * car_positions[i]

# purely functional version
print '\npurely functional version'


def move_car(car_position):
    return map(lambda x: x + 1 if random() > 0.3 else x, car_position)


def output_car(car_position):
    return '-' * car_position


def run_step_of_race(state):
    return {'time': state['time'] - 1,
            'car_positions': move_car(state['car_positions'])}


def draw(state):
    print ''
    print '\n'.join(map(output_car, state['car_positions']))


def race(state):
    draw(state)
    if state['time']:
        race(run_step_of_race(state))


race({'time': 5,
      'car_positions': [1, 1, 1]})


def zero(s):
    if s[0] == '0':
        return s[1:]


def one(s):
    if s[0] == '1':
        return s[1:]


def rule_sequence(s, rules):
    for rule in rules:
        s = rule(s)
        if s is None:
            break
    return s


def rule_sequence_recursive(s, rules):
    if s is None or not rules:
        return s
    else:
        return rule_sequence_recursive(rules[0](s), rules[1:])


print rule_sequence('0101', [zero, one, zero])
print rule_sequence_recursive('0101', [zero, one, zero])

print rule_sequence('011', [zero, one, zero])
print rule_sequence_recursive('011', [zero, one, zero])