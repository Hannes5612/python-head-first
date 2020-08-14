vowels = set('aeiou')
word = input('Gib her los:')
found = set(vowels).intersection(set(word))
print(found)
