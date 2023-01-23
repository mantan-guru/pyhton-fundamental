"""
Program Perulangan  membaca buku dengan while
"""

book_total = 10
print(f'ibu berkata, "Baca semua buku"')

books_read_count = 0

#use while to repeate the statemen
while books_read_count < book_total  :
    books_read_count = books_read_count + 1
    print(f'Book {books_read_count} has been read')

print(books_read_count)
