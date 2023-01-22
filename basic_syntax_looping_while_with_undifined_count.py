"""
Program Perulangan  membaca buku dengan while
"""

book_count = 10
print(f'ibu berkata, "Baca semua buku"')

understood_count = 0
read_count = 0

#use while to repeate the statemen
while read_count < book_count * 2  :
    read_count = read_count + 1
    if understood_count == 9 :
        print(f'buku ke {understood_count + 1 } belum paham')
    else :
        understood_count = understood_count + 1
        print(f'buku ke {understood_count} sudah dibaca dan dipahami')

print(f'jumlah_buku_yang_sudah_dibaca_dan_dipahami adalah {understood_count}')
if understood_count == book_count:
    print('Bu, semua buku bisa dipahami')
else :
    print(f'Bu, tidak semua buku dipahami, budi hanya bisa memahami {understood_count} buku')

