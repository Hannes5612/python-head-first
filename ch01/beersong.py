word = 'bottles'

for beers_num in range(99, 0, -1):
    print(beers_num, word, "of beer on the wall.")
    print(beers_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beers_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        if beers_num - 1 == 1:
            word = "bottle"
        print(beers_num - 1, word, "on the wall.")
    print()
