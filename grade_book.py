# grade book using python
# as module

def add_course(course, course_name):
    course[course_name] = []

def add_grade(courses,course_name,grade):
    if course_name in courses:
        courses[course_name].append(grade)
    
    else:
        print("course not found ")

def calculate_overall_grade(courses, course_name):
    if course_name in courses:
        grades = courses[course_name]
        overall_grade = sum(grades) / len(grades)
        return overall_grade
    else:
        print("course not found.")
        return None
