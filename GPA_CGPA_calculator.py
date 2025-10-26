def GPA(c_credit, c_grade):
    total = 0
    total_credit = 0
    for i in range(len(c_credit)):
        total += c_credit[i] * c_grade[i]
        total_credit += c_credit[i]
    return total / total_credit


def CGPA(GPA_list, credit_list):
    total = 0
    total_credit = 0
    for i in range(len(GPA_list)):
        total += GPA_list[i] * credit_list[i]
        total_credit += credit_list[i]
    return total / total_credit


def course_credit():
    n = int(input("Number of courses: "))
    c_c = []
    c_g = []
    for i in range(n):
        grade = float(input(f"Input your grade (2.0-4.0) of course {i+1}: "))
        credit = float(input(f"Input your credit of course {i+1}: "))
        c_g.append(grade)
        c_c.append(credit)
    return c_c, c_g


def semester_credit():
    n = int(input("Number of semesters: "))
    c_c = []
    c_g = []
    for i in range(n):
        gpa = float(input(f"Input your GPA (2.0-4.0) of semester {i+1}: "))
        credit = float(input(f"Input your total credit of semester {i+1}: "))
        c_g.append(gpa)
        c_c.append(credit)
    return c_c, c_g


def main():
    choice = int(input('''Enter your choice (1-2):
1. Calculate CGPA
2. Calculate GPA
> '''))

    match choice:
        case 2:
            c_c, c_g = course_credit()
            gpa = GPA(c_credit=c_c, c_grade=c_g)
            print(f"\nYour GPA is: {gpa:.2f}")
        case 1:
            c_c, c_g = semester_credit()
            cgpa = CGPA(GPA_list=c_g, credit_list=c_c)
            print(f"\nYour CGPA is: {cgpa:.2f}")
        case _:
            print("Invalid choice! Please enter 1 or 2.")


main()
