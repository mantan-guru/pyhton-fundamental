"""
Program Perulangan  membaca buku dengan for
"""

jumlah_buku = 10
print(f'ibu berkata, "Baca semua buku"')

jumlah_buku_yang_sudah_dibaca = 0

#use for to repeate the statemen
for jumlah_buku_yang_sudah_dibaca in range(1,jumlah_buku + 1):
    print(f'buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca')

print(jumlah_buku_yang_sudah_dibaca)
