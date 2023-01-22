"""
Program Perulangan  membaca buku dengan while
"""

buku = 10
print(f'ibu berkata, "Baca semua buku"')

jumlah_paham = 0
jumlah_baca = 0

#use while to repeate the statemen
while jumlah_baca < buku * 2  :
    jumlah_baca = jumlah_baca + 1
    if jumlah_paham == 9 :
        print(f'buku ke {jumlah_paham + 1 } belum paham')
    else :
        jumlah_paham = jumlah_paham + 1
        print(f'buku ke {jumlah_paham} sudah dibaca dan dipahami')

print(f'jumlah_buku_yang_sudah_dibaca_dan_dipahami adalah {jumlah_paham}')
if jumlah_paham == buku:
    print('Bu, semua buku bisa dipahami')
else :
    print(f'Bu, tidak semua buku dipahami, budi hanya bisa memahami {jumlah_paham} buku')

