def double(arg):
    print('Before:', arg)
    arg = arg * 2
    print('After:', arg)


def change(arg):
    print('Before:', arg)
    arg.append('More data')
    print('After:', arg)


num = 10
saying = 'Hello '
numbers = [42, 256, 16]


double(num)
print(num)
print()

double(saying)
print(saying)
print()

double(numbers)
print(numbers)
print()

change(numbers)
print(numbers)
print()
