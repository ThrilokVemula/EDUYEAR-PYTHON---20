All_courses = ['Python','C','C++','Java','HTML & CSS','React JS','Full Stack Web Development','Swift','Django','MySQL','Machine Learning','Deep learning','AI']
name=input("Enter your name: ")
email=input("Enter your email: ")
user = {'name':name,'email':email,'courses':[]}
courses = user['courses']
def show_menu():
    print('\nMENU:')
    print('1.Show All Courses')
    print('2.Show Enrolled Courses')
    print('3.Show profile')
    print('4.EXIT')
    n = int(input('Enter your choice: '))
    if n == 1:
        all_courses()
    elif n == 2:
        my_courses()
    elif n == 3:
        show_profile()
    elif n == 4:
        return

def all_courses():
    print(All_courses)
    m = int(input('Enter the number of the course to enroll: '))
    print('The enrolled course is :',All_courses[m])
    courses.append(All_courses[m])
    All_courses.remove(All_courses[m])
    print('The details of the candidate are:\n',user)
    show_menu()
    
def my_courses():
    print(courses)
    show_menu()
    
def show_profile():
    for key in user.keys():
        print(key,':',user[key])
    show_menu()

show_menu()    

