"""
All of the basic syntax in programing lenguange is consist of :
1.  sequential  : sequetial step
2.  branching :  jump step if condition are met
3. looping  :  repeat the same steps  many times until conditions are met
"""

# sequential

print(f'ibu berkata, "pergi ke toko" ')
print(f'budi  berkata, "Baik apa yang saya akan lakukan di toko" ')
print(f'ibu berkata, "Beli satu botol susu dan jika ada telor beli 6"')
print(f'ibu berkata, "Beli satu botol susu dan jika ada telor beli 6"')
print(f'maka budi  berangkat ke toko ')
print(f'dan pergi berbelanja')

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
        print(f'Budi membli 6 botol susu')
else:
    print(f'budi tidak jadi membeli 1 botol susu')

print(f'budi pulang')