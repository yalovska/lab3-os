import numpy as np

class Student:
    """Зберігає інформацію про студента та його оцінки."""
    def __init__(self, student_id, name):
        if not student_id or not name:
            raise ValueError("ID та ім'я не можуть бути порожніми")
        self.student_id = student_id
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        """Додає оцінку студенту."""
        if not 0 <= grade <= 100:
            raise ValueError("Оцінка має бути в діапазоні [0, 100]")
        self.grades.append(grade)

    def get_average(self):
        """Розраховує середній бал студента."""
        if not self.grades:
            return 0.0
        # Використовуємо numpy для розрахунку
        return np.mean(self.grades)

class Course:
    """Зберігає список студентів, зарахованих на курс."""
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = {} # Використаємо словник для швидкого пошуку за ID

    def enroll_student(self, student):
        """Зараховує студента на курс."""
        if student.student_id in self.students:
            raise ValueError(f"Студент з ID {student.student_id} вже на курсі")
        self.students[student.student_id] = student

    def get_class_average(self):
        """Розраховує середній бал по всьому курсу."""
        all_student_averages = []
        if not self.students:
            return 0.0
            
        for student in self.students.values():
            avg = student.get_average()
            if avg > 0: # Враховуємо тільки студентів, що мають оцінки
                all_student_averages.append(avg)
        
        if not all_student_averages:
            return 0.0
            
        # Використовуємо numpy для фінального середнього
        return np.mean(all_student_averages)