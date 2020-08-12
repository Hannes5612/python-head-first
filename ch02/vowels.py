vowels = ['a', 'e', 'i', 'o', 'u']

word = 'Milliways'

found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

print(found)