def create_courses():
    print("Enter course name:")
    c = input()
    return c

def show_employees(employees):
    print(f"{len(employees)} employees")
    for employee in employees:
        print(employee)

def register_on_courses(employe, course):
    course_reg[employe] = course
    print(f"{employe} registered on course {course}")



course_reg = {}
course = create_courses()
employees = ["Ivan", "Peter", "Anton"]
show_employees(employees)
employee = register_on_courses(employees[1], course)
