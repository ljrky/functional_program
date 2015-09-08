a = 0
b = 0


def increment_mutable():
    global a
    a += 1
    return a


def increment_immutable(b):
    return b + 1


print a
print increment_mutable()
print a

print b
print increment_immutable(b)
print b
