class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



# stud = Student('Petr', 'Semenov', 'male')
# stud.courses_in_progress += ['Python']
# stud.courses_in_progress += ['Java']
# print(stud.name, stud.surname, stud.gender, stud.courses_in_progress)
#
# lector = Lecturer('Ivan', 'Petrov')
# lector.courses_attached += ['Python']
# lector.courses_attached += ['Java']
# print(lector.name, lector.surname, lector.grades, lector.courses_attached)
#
# stud.rate_lec(lector, 'Python', 10)
# stud.rate_lec(lector, 'Java', 7)
# stud.rate_lec(lector, 'Java', 5)
# print(lector.grades)