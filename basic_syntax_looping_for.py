"""
Program Perulangan  membaca buku dengan for
"""

book_total = 10
print(f'Mother says, "Read all the books"')

books_read_count = 0

#use for to repeate the statemen
for books_read_count in range(1, book_total + 1):
    print(f'Book {books_read_count} has been read')

print(books_read_count)
