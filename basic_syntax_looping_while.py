"""
Program Perulangan  membaca buku dengan while
"""

jumlah_buku = 10
print(f'ibu berkata, "Baca semua buku"')

jumlah_buku_yang_sudah_dibaca = 0

#use while to repeate the statemen
while jumlah_buku_yang_sudah_dibaca < jumlah_buku  :
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    print(f'buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca')

print(jumlah_buku_yang_sudah_dibaca)
