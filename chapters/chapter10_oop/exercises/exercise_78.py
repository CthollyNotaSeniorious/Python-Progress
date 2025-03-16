# Exercise 78 - Simple University System
# Given the following class definitions.
# Implement the `Student` and `Professor` classes to inherit from the `Person` class.
# See `test_e78()` in `tests/test_ch10.py` for the expected behavior.
from __future__ import annotations


class Course:
    def __init__(self, course_name: str, course_code: str):
        self.course_name = course_name
        self.course_code = course_code
        self.professor: Professor | None = None
        self.students: list[Student] = []

    def add_student(self, student: Student):
        self.students.append(student)

    def assign_professor(self, professor: Professor):
        self.professor = professor

    def list_students(self):
        return [student.name for student in self.students]


class Person:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


# Implement the `Student` and `Professor` classes to inherit from the `Person` class.
class Student:
    def __init__(self, name: str, email: str, student_id: str):
        super().__init__(name, email)
        self.student_id = student_id
        self.enrolled_courses: list[Course] = []

    def enroll(self, course: Course) -> None:
        # Your code should go here.
        ...

    def list_courses(self) -> list[str]:
        # Your code should go here.
        ...


class Professor:
    def __init__(self, name: str, email: str, professor_id: str):
        super().__init__(name, email)
        self.professor_id = professor_id
        self.taught_courses: list[Course] = []

    def assign_course(self, course: Course) -> None:
        # Your code should go here.
        ...

    def list_courses(self) -> list[str]:
        # Your code should go here.
        ...
