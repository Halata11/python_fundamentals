import sys
import time

student_name = []
student_id = []
student_age = []
student_email = []
student_class = []
student_grade = []
student_mobile = []


class manager:
    @staticmethod
    def add_student(): #adding student common information
        print('Adding student information:')
        print('Enter student name', end=' ')
        name = input()
        student_name.append(name)

        print('Enter student id', end=' ')
        id = int(input())
        student_id.append(id)

        print('Enter student age', end='')
        age = int(input())
        student_age.append(age)

        print('Enter student email', end='')
        email = input()
        student_email.append(email)

        print('Enter student class', end='')
        class_ = input()
        student_class.append(class_)

        print('Enter student grade', end='')
        grade = float(input())
        student_grade.append(grade)

        print('Enter student mobile phone', end='')
        mobile = int(input())
        student_mobile.append(mobile)

        if mobile < 9:
            print('Wrong number')
            print('Enter valid mobile number')
            print('Thank you')

        else:
            student_mobile.append(mobile)
            print("\n")
            print("\t STUDENT INFORMATION ADDED SUCCESSFULLY.")
            print("\n")

    @staticmethod
    def data_delete(): #deleting student information or certain value
        print('Deleting student info:')


        if len(student_name) == 0 and len(student_id) == 0 and len(student_age) == 0 and len(student_email) == 0\
            and len(student_class) == 0 and len(student_grade) == 0 and len(student_mobile) == 0:
            print('Please enter student information')

        else:
            print('Enter students id')
            id = int(input())
            loc = student_id.index(id)

            student_id.remove(student_id)
            student_mobile.remove(student_mobile)
            student_grade.remove(student_grade)
            student_age.remove(student_age)
            student_class.remove(student_class)
            student_email.remove(student_email)
            student_name.remove(student_name)

            print('Student has been deleted from the dictionary successfully')

    @staticmethod
    def update_info(): # update student info
        print('Update student information')
        print('Thank you for your support')

        if len(student_name) == 0 and len(student_id) == 0 and len(student_age) == 0 and len(student_email) == 0\
            and len(student_class) == 0 and len(student_grade) == 0 and len(student_mobile) == 0:
            print('Please enter student information')

        else:
            print('Choose the element you want to delete', end='')
            print("Example" 'age, mobile, name, email, id, class, grade')
            print('Enter here', end='')
            element = input()

            if element == 'NAME':
                print("ENTER 'OLD NAME' :", end=" ")
                OLD_NAME = input()
                LOC_NAME = student_name.index(OLD_NAME)

                print("ENTER 'NEW NAME' :", end=" ")
                NEW_NAME = input()
                student_name[LOC_NAME] = NEW_NAME
                print("\t 'NAME UPDATED SUCCESSFULLY.")
                print("\n")

            elif element == 'ROLL NUMBER':
                print("ENTER 'OLD ROLL NUMBER' :", end=" ")
                OLD_ROLL_NUMBER = int(input())
                LOC_ROLL = student_id.index(OLD_ROLL_NUMBER)

                print("ENTER 'NEW ROLL NUMBER' :", end=" ")
                NEW_ROLL = int(input())
                student_id[LOC_ROLL] = NEW_ROLL
                print("\t 'ROLL NUMBER UPDATED SUCCESSFULLY.")
                print("\n")

            elif element == 'AGE':
                print("ENTER 'OLD AGE' :", end=" ")
                OLD_AGE = int(input())
                LOC_ROLL = student_age.index(OLD_AGE)

                print("ENTER 'NEW AGE' :", end=" ")
                NEW_AGE = int(input())
                student_age[LOC_ROLL] = NEW_AGE
                print("\t 'AGE UPDATED SUCCESSFULLY.")
                print("\n")

            elif element == 'ADDRESS':
                print("ENTER 'OLD ADDRESS' :", end=" ")
                OLD_ADDRESS = input()
                LOC_ADDRESS = student_email.index(OLD_ADDRESS)

            elif element == 'EMAIL':
                print("ENTER 'OLD EMAIL' :", end=" ")
                OLD_EMAIL = input()
                LOC_EMAIL = student_email.index(OLD_EMAIL)

                print("ENTER 'NEW EMAIL' :", end=" ")
                NEW_EMAIL = input()
                student_email[LOC_EMAIL] = NEW_EMAIL
                print("\t 'EMAIL - ID UPDATED SUCCESSFULLY.")
                print("\n")

            elif element == 'CLASS':
                print("ENTER 'OLD CLASS' :", end=" ")
                OLD_CLASS = input()
                LOC_CLASS = student_class.index(OLD_CLASS)

                print("ENTER 'NEW CLASS' :", end=" ")
                NEW_CLASS = input()
                student_class[LOC_CLASS] = NEW_CLASS
                print("\t 'CLASS UPDATED SUCCESSFULLY.")
                print("\n")

            elif element == 'MOBILE NUMBER':
                print("ENTER 'OLD MOBILE NUMBER' :", end=" ")
                OLD_MOBILE = input()

                print("ENTER 'NEW MOBILE NUMBER' :", end=" ")
                NEW_MOBILE = input()
                MOBILE_NUMBER_LEN = len(OLD_MOBILE)
                phone = len(NEW_MOBILE)

                if MOBILE_NUMBER_LEN < 10:
                    print(end="\n")
                    print("PLEASE ENTER TEN DIGIT MOBILE NUMBER.")
                    print("SYSTEM HAS STOP, PLEASE TRY AGAIN.")
                    sys.exit()
                elif phone < 10:
                    print(end="\n")
                    print("\t PLEASE ENTER VALID TEN DIGIT MOBILE NUMBER.")
                    print("\t SYSTEM WORKING HAS STOP PLEASE TRY AGAIN.")
                    sys.exit()
                else:
                    LOC_MOBILE = student_mobile.index(OLD_MOBILE)
                    student_mobile[LOC_MOBILE] = NEW_MOBILE
                    print("\t 'MOBILE NUMBER UPDATED SUCCESSFULLY.")
                    print("\n")



    @staticmethod
    def display_info(): # display saved info
        print('Displaying student information')

        if len(student_name) == 0 and len(student_id) == 0 and len(student_age) == 0 and len(student_email) == 0\
            and len(student_class) == 0 and len(student_grade) == 0 and len(student_mobile) == 0:
            print('No data has been saved')
            print('Start with step 1')
            time.sleep(5)

        else:
            print("Student's name", end='')

            for x in student_name:
                print(x)
            print()

            print(end='\n')

            print("Student's id", end='')

            for z in student_id:
                print(z)
            print()

            print(end='\n')

            print("Student's mobile", end='')

            for g in student_mobile:
                print(g)
            print()

            print(end='\n')

            print("Student's age",end='')

            for t in student_age:
                print(t)
            print()

            print(end='\n')

            print("Student's email",end='')

            for p in student_email:
                print(p)
            print()

            print(end='\n')

            print("Student's class",end='')

            for w in student_class:
                print(w)
            print()

            print(end='\n')

            print("Student's mobile", end='')

            for o in student_mobile:
                print(o)
            print()

            print(end='\n')

manager = manager()

if __name__ == '__main__':
    print('\n')

    print("Welcome to Kostadin's University")
    run = True

    while run:
        print("Press from the following option : \n")

        print("Press 1 : To Add Student Information.")
        print("Press 2 : To Delete Student Information.")
        print("Press 3 : To Update Student Information.")
        print("Press 4 : To Display Student Information.")
        print("Press 5 : To Exit.")

        option = int(input("ENTER YOUR OPTION : "))
        print("\n")
        print(end="\n")

        if option == 1:
            manager.add_student()
        elif option == 2:
            manager.data_delete()
        elif option == 3:
            manager.update_info()
        elif option == 4:
            manager.display_info()
        elif option == 5:
            print("Thank You! Visit us again.")
            run = False
        else:
            print("Please choose one of the numbers below.")
            print("\n")

