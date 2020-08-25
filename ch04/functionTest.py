def vowelCheck(word: str) -> set:
    """This function returns a set of vowels, contained in the argument"""
    vowels = set('aeiou')  # Set of vowels
    found = set(vowels).intersection(set(word))  # Check for intersection
    return found  # return intersected vowels


print(vowelCheck(input('Eomgabe:')))

help(vowelCheck)
