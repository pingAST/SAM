class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        if self.grades:
            total_sum = sum(sum(values) for values in self.grades.values())
            total_count = sum(len(values) for values in self.grades.values())
            average_grade = total_sum / total_count
            courses_in_progress = ', '.join(self.courses_in_progress)
            finished_courses = ', '.join(self.finished_courses)
            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\n" \
                f"Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses} \n"
        else:
            return f"Имя: {self.name}\nФамилия: {self.surname}\nНет оценок\n" \
                f"Курсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses} \n"
        
    def __lt__(self, other):
        return sum(sum(values) for values in self.grades.values()) / len(self.grades) < \
               sum(sum(values) for values in other.grades.values()) / len(other.grades)

    def __eq__(self, other):
        return sum(sum(values) for values in self.grades.values()) / len(self.grades) == \
               sum(sum(values) for values in other.grades.values()) / len(other.grades)
    
    def rate_lecture(self, lecturer, course, grade):
        if course in self.courses_in_progress and isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_hw_grade(self, course):
        if course in self.grades:
            return sum(self.grades[course]) / len(self.grades[course])
        else:
            return 0
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        if self.grades:
            average_grade = sum(self.grades) / len(self.grades)
            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}\n"
        else:
            return f"Имя: {self.name}\nФамилия: {self.surname}\nНет оценок\n"
        
    def __lt__(self, other):
        return sum(sum(values) for values in self.grades.values()) / len(self.grades) < \
               sum(sum(values) for values in other.grades.values()) / len(other.grades)

    def __eq__(self, other):
        return sum(sum(values) for values in self.grades.values()) / len(self.grades) == \
               sum(sum(values) for values in other.grades.values()) / len(other.grades)
    
    def average_lecture_grade(self, course):
        if course in self.grades:
            return sum(self.grades[course]) / len(self.grades[course])
        else:
            return 0
    
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_hw_grade_for_course(students, course):
    total_sum = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_sum += sum(student.grades[course])
            count += len(student.grades[course])
    if count > 0:
        return total_sum / count
    else:
        return 0
def average_lecture_grade_for_course(lecturers, course):
    total_sum = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_sum += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    if count > 0:
        return total_sum / count
    else:
        return 0

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

best_student.rate_lecture(cool_lecturer, 'Python', 5)
best_student.rate_lecture(cool_lecturer, 'Python', 7)
best_student.rate_lecture(cool_lecturer, 'Python', 10)

print(best_student.grades)
print(cool_lecturer.grades)

#Задача №3(1)
some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.grades = [9.9, 8.5, 10.0]

some_student = Student('Ruoy', 'Eman', 'Male')
some_student.grades = {'Python': [10, 9, 8], 'Git': [9, 9, 10]}
some_student.courses_in_progress = ['Python', 'Git']
some_student.finished_courses = ['Введение в программирование']

print(some_reviewer)
print(some_lecturer)
print(some_student)


lecturer1 = Lecturer('John', 'Doe')
lecturer2 = Lecturer('Jane', 'Smith')

lecturer1.grades = {'Python': [8, 9, 7], 'Math': [10, 9, 8]}
lecturer2.grades = {'Python': [10, 9, 9], 'Math': [8, 7, 9]}


#Задача №3(2)
print(f'Сравнение Лекторов:')
print(lecturer1 > lecturer2)  # False
print(lecturer1 == lecturer2)  # False

student1 = Student('Ruoy', 'Eman', 'Male')
student2 = Student('Jane', 'Smith', 'Female')

student1.grades = {'Python': [10, 9, 8], 'Math': [9, 9, 10]}
student2.grades = {'Python': [8, 7, 9], 'Math': [10, 9, 8]}

print(f'Сравнение Студентов:')
print(student1 > student2)  # True
print(student1 == student2)  # False
print()

#Задача № 4
print(f'Средняя оценка за домашние задания по курсу Python для студентов: {average_hw_grade_for_course([best_student], "Python")}')
print(f'Средняя оценка за лекции по курсу Python для лекторов: {average_lecture_grade_for_course([cool_lecturer], "Python")}')