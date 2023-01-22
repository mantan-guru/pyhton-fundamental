"""
All of the basic syntax in programing lenguange is consist of :
1.  sequential  : sequetial step
2.  branching :  jump step if condition are met
3.  looping  :  repeat the same steps  many times until conditions are met
"""

# sequential

print(f'Mother says, "go to the store"')
print(f'Budi says, "Okay, what should I do at the store?"')
print(f'Mother says, "Buy one bottle of milk and if there are eggs, buy six."')
print(f'So Budi goes to the store')
print(f'and goes shopping')

# branching
total_milk_bottles = 173
total_eggs = 1587

print(f"The number of milk bottles is  {total_milk_bottles} bottle")
print(f"The number of eggs is {total_eggs} pieces")
if total_milk_bottles > 0 :
    print(f'Budi checks the prices and it turns out his money is enough.')
    if total_eggs == 0 :
        print(f'Budi buys 1 bottle of milk')
    else:
        print(f'Budi buys 1 bottle of milk and 6 eggs')
else:
    print(f'Budi decides not to buy 1 bottle of milk.')

print(f'Budi goes home')