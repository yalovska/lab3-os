import pytest
from university import Student, Course

# Тестуємо клас Student
def test_student_creation():
    s = Student(1, "Іван Петренко")
    assert s.student_id == 1
    assert s.name == "Іван Петренко"
    assert s.grades == []

def test_add_grade():
    s = Student(1, "Іван Петренко")
    s.add_grade(90)
    s.add_grade(80)
    assert s.grades == [90, 80]

def test_student_average():
    s = Student(1, "Іван Петренко")
    s.add_grade(90)
    s.add_grade(80)
    assert s.get_average() == 85.0

def test_student_average_empty():
    s = Student(1, "Іван Петренко")
    assert s.get_average() == 0.0

def test_invalid_grade():
    s = Student(1, "Іван Петренко")
    with pytest.raises(ValueError, match="Оцінка має бути"):
        s.add_grade(101)
    with pytest.raises(ValueError, match="Оцінка має бути"):
        s.add_grade(-5)

# Тестуємо клас Course
def test_course_enrollment():
    course = Course("Програмування")
    s1 = Student(1, "Іван Петренко")
    course.enroll_student(s1)
    assert course.students[1] == s1

def test_duplicate_enrollment():
    course = Course("Програмування")
    s1 = Student(1, "Іван Петренко")
    course.enroll_student(s1)
    with pytest.raises(ValueError, match="вже на курсі"):
        course.enroll_student(s1)

def test_class_average():
    course = Course("Програмування")
    s1 = Student(1, "Іван Петренко")
    s1.add_grade(100) # avg 100
    
    s2 = Student(2, "Марія Сидоренко")
    s2.add_grade(80)
    s2.add_grade(90) # avg 85
    
    course.enroll_student(s1)
    course.enroll_student(s2)
    
    # Середнє (100 + 85) / 2 = 92.5
    assert course.get_class_average() == 92.5

def test_class_average_with_no_grades_student():
    course = Course("Програмування")
    s1 = Student(1, "Іван Петренко")
    s1.add_grade(90) # avg 90
    
    s2 = Student(2, "Марія Сидоренко")
    # s2 без оцінок, її середній бал 0.0 і не враховується
    
    course.enroll_student(s1)
    course.enroll_student(s2)
    
    assert course.get_class_average() == 90.0

def test_class_average_empty_course():
    course = Course("Програмування")
    assert course.get_class_average() == 0.0