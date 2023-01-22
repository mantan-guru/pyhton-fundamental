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
jumlah_botol_susu = 173
jumlah_telur = 1587

print(f"Jumlah botol susu adalah  {jumlah_botol_susu} botol")
print(f"jumlah telur adalah {jumlah_telur} butir")
if jumlah_botol_susu > 0 :
    print(f'Budi mengecek harganya dan ternyata uangnya cukup')
    if jumlah_telur == 0 :
        print(f'Budi membeli 1 botol susu')
    else:
        print(f'Budi membli  1 botol susu dan 6 butir telur')
else:
    print(f'budi tidak jadi membeli 1 botol susu')

print(f'budi pulang')