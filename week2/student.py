

student_data = {}

def add(name='',department='',stud_id='',age='',grade=''):
    name = input("enter student name")
    department = input("enter student department")
    stud_id: str = input("enter student id")
    age = input("enter student age")
    grade = input("enter student grade")

    added_stud = {
        'name': name,
        'department': department,
        'id': stud_id,
        'age': age,
        'grade': grade
    }
    student_data[name] = added_stud
    print("student added successfully")


def view():
     name = input("enter student name to search")
     if name in student_data:
            stu = student_data[name]
            print("Name:", stu['name'])
            print("department:", stu['department'])
            print("id:", stu['id'])
            print("age:", stu['age'])
            print("grade:", stu['grade'])

     else:
            print("student not found")


def display():
   for name, student in student_data.items():
       print("Name:", student['name'])
       print("department:",student['department'])
       print("age:", student['age'])
       print("grade:",student["grade"])
       print("..........................")



def update():
    name= input("enter student name you want to update")
    if name in student_data:
         stud = student_data[name]
         print("Name:", stud['name'])
         print("department:", stud['department'])
         print("age:", stud['age'])
         print("grade:", stud["grade"])
         new_name = input("enter the new name")
         new_department = input("enter the new department")
         new_age = input("enter the new age")
         new_grade = input("enter the new grade")
         print("student information updated successfully")
         stud['name'] = new_name
         stud['department'] = new_department
         stud['age'] = new_age
         stud['grade'] =new_grade
         print("student information updated successfully")
    else:
     print("student not found")



def delete():
      name = input("please enter the name you want to delete ")
      if name in student_data:
          del student_data[name]
          print("deleted successfully")
      else:
          print("student not found")



def main():
    while True:
        print(".....student database menu.....")
        print("1.Add student")
        print("2.view specific student")
        print("3.Display student")
        print("4.Update student information")
        print("5.Delete student")
        print("6.Exit")

        choice=input("enter your choice\n")
        if choice == '1':
            add()
        elif choice == '2':
            view()
        elif choice == '3':
            display()
        elif choice == '4':
            update()
        elif choice == '5':
            delete()
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()



