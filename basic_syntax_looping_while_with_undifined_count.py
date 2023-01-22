"""
Program Perulangan  membaca buku dengan while
"""

jumlah_buku = 10
print(f'ibu berkata, "Baca semua buku"')

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
jumlah_total_baca = 0

#use while to repeate the statemen
while jumlah_total_baca < jumlah_buku * 2  :
    jumlah_total_baca = jumlah_total_baca + 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9 :
        print(f'buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami +  1 } belum paham')
    else :
        jumlah_buku_yang_sudah_dibaca_dan_dipahami = jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1
        print(f'buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami')

print(f'jumlah_buku_yang_sudah_dibaca_dan_dipahami adalah {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')
if jumlah_buku_yang_sudah_dibaca_dan_dipahami == jumlah_buku:
    print('Bu, semua buku bisa dipahami')
else :
    print(f'Bu, tidak semua buku dipahami, budi hanya bisa memahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku')

