#using del with list comprhension
print('\n Command del with list comprehension')
list_book = ['Seven Habit', 'How to Influence People', 'First Things First', '40DX']
del list_book[:] #

for i in list_book:
    print(i)

#using del with list comprhension start
print('\n Command del with list comprehension Start')
list_book = ['Seven Habit', 'How to Influence People', 'First Things First', '40DX']
del list_book[0:-2] #START:END

for i in list_book:
    print(i)

#using del with list comprhension start step end
print('\n Command del with list comprehension start end step')
list_book = ['Seven Habit', 'How to Influence People', 'First Things First', '40DX','Matimatihics', 'Biologi']
del list_book[0:-1:2] #START:END:STEP

for i in list_book:
    print(i)

#Create new List with list comprehension
print('\n Create New list all copy')
list_book = ['1 Seven Habit', '2 How to Influence People', '3 First Things First', '4 40DX','5 Matimatihics', '6 Biologi']
new_list_book = list_book[:]
print('--NEW LIST BOOK--')
for i in new_list_book:
    print(i)

#Create new List with list comprehension GENAP
print('\n Create New list GENAP')
list_book = ['1 Seven Habit', '2 How to Influence People', '3 First Things First', '4 40DX','5 Matimatihics', '6 Biologi']
new_list_book = list_book[1::2]
print('--NEW LIST BOOK--')
for i in new_list_book:
    print(i)

#Create new List with list comprehension GANJIL
print('\n Create New list GENJIL')
list_book = ['1 Seven Habit', '2 How to Influence People', '3 First Things First', '4 40DX','5 Matimatihics', '6 Biologi']
new_list_book = list_book[0::2]
print('--NEW LIST BOOK--')
for i in new_list_book:
    print(i)

#Create new List with list comprehension delete last index
print('\n Create New list GENJIL')
list_book = ['1 Seven Habit', '2 How to Influence People', '3 First Things First', '4 40DX','5 Matimatihics', '6 Biologi']
new_list_book = list_book[0:-1]
print('--NEW LIST BOOK--')
for i in new_list_book:
    print(i)