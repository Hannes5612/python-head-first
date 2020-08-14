vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word or sentence to search for vowels:')

found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)
        found[letter] += 1

for k, v in reversed(sorted(found.items())):
    print('Letter', k, 'found', v, 'times in the given sequence')
