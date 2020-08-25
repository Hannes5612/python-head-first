def lettersCheck(phrase: str, letters: str = 'aeiou') -> set:
    return set(letters).intersection(set(phrase))  # Check for intersection


def vowelCheck(word: str) -> set:
    """This function returns a set of vowels, contained in the argument"""
    vowels = set('aeiou')  # Set of vowels
    return set(vowels).intersection(set(word))  # Check for intersection
