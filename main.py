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

    def __str__(self):
        sum_ = 0
        num_ = 0
        for i in self.grades:
            sum_ += sum(self.grades[i])
            num_ += len(self.grades[i])

        av = sum_ / num_
        cour_prog = 0
        p = str()
        while cour_prog < len(self.courses_in_progress):
            p += self.courses_in_progress[cour_prog] + ' '
            cour_prog += 1

        cour_fin = 0
        z = str()
        while cour_fin < len(self.finished_courses):
            z += self.finished_courses[cour_fin] + ' '
            cour_fin += 1


        res = f'Имя: {self.name}, Фамилия: {self.surname}, Средняя оценка за задания: {av}, ' \
              f'Курсы в процессе изучения: {p}, Завершенные курсы: {z}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент.')
            return
        a = sum(other.grades['Python']) / len(other.grades['Python'])
        b = sum(self.grades['Python']) / len(self.grades['Python'])
        return a < b

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор.')
            return
        a = sum(other.grades['Python']) / len(other.grades['Python'])
        b = sum(self.grades['Python']) / len(self.grades['Python'])
        return a < b

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        global av
        av = 0
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                av += grade
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}, Фамилия: {self.surname}'
        return res


lec = Lecturer('Mark', 'Seferovic')
lec_1 = Lecturer('John', 'Star')
stud = Student('Ivan', 'Petrov','male')
stud_1 = Student('Maria', 'Ivanova','female')
stud_2 = Student('Irina', 'Stoyanova','female')
rew = Reviewer('Mr', 'Smirnov')
rew_1 = Reviewer('Ms', 'Marple')

stud.courses_in_progress += ['Python']
stud.finished_courses += ['Web']
stud.courses_in_progress += ['Java']
stud_1.courses_in_progress += ['Python']
stud_1.finished_courses += ['Java']
stud_2.courses_in_progress += ['Back_end']
stud_2.courses_in_progress += ['Front_end']

lec.courses_attached += ['Python']
lec.courses_attached += ['Java']
lec.courses_attached += ['Web']
lec_1.courses_attached += ['Front_end']
lec_1.courses_attached += ['Back_end']
lec_1.courses_attached += ['Data_science']


rew.courses_attached += ['Python']
rew.courses_attached += ['Java']
rew.courses_attached += ['Data_science']
rew_1.courses_attached += ['Python']
rew_1.courses_attached += ['Web']
rew_1.courses_attached += ['Java']

rew.rate_hw(stud, 'Python', 10)
rew.rate_hw(stud_1, 'Python', 9)
rew.rate_hw(stud_2, 'Python', 7)
rew.rate_hw(stud, 'Python', 6)
rew.rate_hw(stud_1, 'Python', 10)
rew.rate_hw(stud_2, 'Python', 10)
rew.rate_hw(stud, 'Java', 5)
rew.rate_hw(stud, 'Java', 5)

stud.rate_lec(lec, 'Python', 10)
stud_1.rate_lec(lec, 'Python', 9)
stud.rate_lec(lec, 'Java', 6)
stud.rate_lec(lec, 'Java', 5)

stud_2.rate_lec(lec_1, 'Front_end', 5)
stud_2.rate_lec(lec_1, 'Front_end', 5)
stud_2.rate_lec(lec_1, 'Back_end', 10)
stud_2.rate_lec(lec_1, 'Back_end', 10)

def av_grade_course_stud(students, course):
    i = 0

    grad = []

    while i < len(students):
        if isinstance(students[i], Student) and (course in students[i].courses_in_progress or students[i].finished_courses):
           grad += students[i].grades[course]
           i += 1

        else:
            i += 1


    s = round(sum(grad)/len(grad),2)

    return(s)


def av_grade_course_lect(lector, course):
    i = 0

    grad = []
    while i < len(lector):
        if isinstance(lector[i], Lecturer) and course in lector[i].courses_attached:
            grad += lector[i].grades[course]
            i += 1

        else:
            i += 1

    s = round(sum(grad) / len(grad), 2)

    return (s)








