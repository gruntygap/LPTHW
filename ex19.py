def fish_and_chips(fish_count, chip_packs):
    print "You have %d fishes!" % fish_count
    print "You have %d packs of chips" % chip_packs
    print "Man... That's enough for a party!"
    print "Get a blanket? \n"

print "We can just give the function numbers directly."
print "For example, this is going to input the numbers 20, and 30"

fish_and_chips(20, 30)

print "Or we can use variables from our script:"
amount_of_fish = 10
amount_of_chips = 50

fish_and_chips(amount_of_fish, amount_of_chips)

print "We can even do math inside the function calls"
fish_and_chips(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
fish_and_chips(amount_of_fish + 100, amount_of_chips + 10)

print "We can even accept an input and run it through:"

amount_of_fish = int(raw_input("Please type the amount of fish you want: "))
amount_of_chips = int(raw_input("Please type the amount of chips you want: "))
fish_and_chips(amount_of_fish, amount_of_chips)