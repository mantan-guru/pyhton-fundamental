"""
basic syntax list book
"""

list_book = ['Seven Habit', 'How to Influence People', 'First Things First', '40DX']
print('Show Variabel list book')
print(list_book)

print('\nProces all with for in')
for book in list_book :
    print(book)


print('\nVariabel list_book with index')
print(list_book[0])
print(list_book[2])

print('\nShow list_book with for in range')
for i in range(0, len(list_book)):
    print(list_book[i])

list_book = [1, 'Kenji Volume 2', -313, 3.14]
print('\nShow with for in range, where the data type of each element is different')
for i in range(0, len(list_book)):
    print(list_book[i])

print('\nreturn the original value of the book list')
list_book = ['Seven Habit', 'How to Influence People', 'First Things First', '40DX']
print('\nadd one list book')
list_book.append('Dunia Matematik Kelas 5')
for i in range(0, len(list_book)):
    print(list_book[i])


#clear list
print('\n clear list using method clear()')
list_book.clear()
for i in range(0, len(list_book)):
    print(list_book[i])

#change list element
list_book = ['Seven Habit', 'How to Influence People', 'First Things First', '40DX']
list_book[0] = 'Eight habit'
print('\nChange first element')
for i in range(0, len(list_book)):
    print(list_book[i])

#using pop
print('\nUsing Pop to clear last element')
list_book.pop()
for i in range(0, len(list_book)):
    print(list_book[i])

print('\nUsing Pop to clear first element')
list_book.pop(0)
for i in range(0, len(list_book)):
    print(list_book[i])

#using appen to add element in last index
list_book.append('Matematika Teknik')
print(list_book)

#using insert to add element in specify index
list_book.insert(1, 'Data Minning')
print(list_book)

#using pop
print('\n POP -4')
list_book = ['Seven Habit', 'How to Influence People', 'First Things First', '40DX']
list_book.pop(-4)
for i in list_book:
    print(i)

#using del
print('\n Command Del')
list_book = ['Seven Habit', 'How to Influence People', 'First Things First', '40DX']
del list_book[1]

for i in range(0, len(list_book)):
    print(list_book[i])

