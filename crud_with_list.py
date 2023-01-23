student = []
list_operation = ["Add Student", "Update Student", "Delete Student", "List Student", "exit Program"]

def operation_student():
    for i in range(0, len(list_operation)):
        print(f'{i}. {list_operation[i]}')

def operation_execute(operation):

    if operation == 0 :
        add()
    elif operation == 1 :
        update_student()
    elif operation == 2 :
        delete_student()
    elif operation == 3 :
        list_student()
    else  :
        exit_program()

def add():
    print('Add Student \n')
    student_name = input('Type Student Name : ')
    student.append(student_name)
    operation_student()

def list_student():
    print('--List Student--')
    for i in range(0, len(student)):
        print(f'{i + 1}.  {student[i]}')
    print("\n")
    operation_student()

def update_student():
    print('Update Student')
    for i in range(0, len(student)) :
        print(f'{i + 1}. {student[i]}')
    select_student = int(input('Chose Number Student You want to  Delete :'))


def delete_student():
    print('DELETE STUDENT')
    for i in range(0, len(student)) :
        print(f'{i + 1}. {student[i]}')
    student_delete  = input('Chose Number Student You want to  Delete :')
    student.pop(int(student_delete)- 1)
    operation_student()

def exit_program():
    exit()


operation = 0
print("\n OPERATION")
operation_student()

while operation < 3 :
    select_operation = int(input("\nSelect Operation :  "))
    operation_execute(select_operation)
    # print(student)


