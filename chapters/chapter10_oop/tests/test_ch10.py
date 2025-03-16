import pytest
from ..exercises.exercise_68 import Vector3D
from ..exercises.exercise_69 import TaxCalculator
from ..exercises.exercise_70 import Circle, Shape, Square
from ..exercises.exercise_71 import Author, Book, Genre
from ..exercises.exercise_72 import BookShelf
from ..exercises.exercise_73 import Library
from ..exercises.exercise_74 import Account, Card, Customer
from ..exercises.exercise_75 import BankCustomer
from ..exercises.exercise_76 import Box
from ..exercises.exercise_77 import create_content, Blogger, Vlogger
from ..exercises.exercise_78 import Course, Student, Professor


def test_e68():
    v1 = Vector3D(1, 2, 3)
    v2 = Vector3D(4, 5, 6)
    v3 = v1 + v2
    assert isinstance(v3, Vector3D)
    assert v3.x == 5
    assert v3.y == 7
    assert v3.z == 9
    v4 = v1 - v2
    assert isinstance(v4, Vector3D)
    assert v4.x == -3
    assert v4.y == -3
    assert v4.z == -3


def test_e69():
    tax_calculator = TaxCalculator()
    assert tax_calculator.calculate_tax(0) == 0
    assert tax_calculator.calculate_tax(10_000) == 0
    assert tax_calculator.calculate_tax(10_001) == 1000.1
    assert tax_calculator.calculate_tax(50_000) == 5000
    assert tax_calculator.calculate_tax(50_001) == 10_000.2
    assert tax_calculator.calculate_tax(100_000) == 20_000
    assert tax_calculator.calculate_tax(150_000) == 45_000


def test_e70():
    assert issubclass(Square, Shape)
    assert issubclass(Circle, Shape)
    square = Square(5)
    assert square.area() == 25
    circle = Circle(5)
    assert circle.area() == 78.54


def test_e71():
    author = Author("John", "Doe")
    assert author.first_name == "John"
    assert author.last_name == "Doe"
    book = Book("The Book", author, 2024, Genre.Fiction)
    assert book.title == "The Book"
    assert book.author == author
    assert book.publication_year == 2024
    assert book.genre == Genre.Fiction


def test_e72():
    author = Author("John", "Doe")
    book = Book("The Book", author, 2024, Genre.Fiction)

    shelf = BookShelf()
    assert shelf.get_books() == []
    shelf.add_book(book)
    assert shelf.get_books() == [book]
    assert shelf.get_books_by_genre(Genre.History) == []
    assert shelf.get_books_by_genre(Genre.NonFiction) == []
    assert shelf.get_books_by_genre(Genre.Fiction) == [book]

    shelf.remove_book(book)
    assert shelf.get_books() == []
    assert shelf.get_books_by_genre(Genre.Fiction) == []
    book2 = Book("Biography Book", author, 2024, Genre.Biography)
    book3 = Book("History Book", author, 2024, Genre.History)
    shelf.add_book(book2)
    shelf.add_book(book3)
    assert shelf.get_books_by_genre(Genre.Fiction) == []
    assert shelf.get_books_by_genre(Genre.Biography) == [book2]
    assert shelf.get_books_by_genre(Genre.History) == [book3]


def test_e73():
    shelf_A_books = [
        Book("The Book", Author("John", "Doe"), 2024, Genre.Fiction),
        Book("Another Book", Author("John", "Doe"), 2024, Genre.Fiction),
    ]
    shelfA = BookShelf(shelf_A_books)
    assert shelfA.get_books() == shelf_A_books
    shelf_B_books = [
        Book("Biography Book", Author("John", "Doe"), 2024, Genre.Biography),
        Book("History Book", Author("John", "Doe"), 2024, Genre.History),
    ]
    shelfB = BookShelf(shelf_B_books)
    assert shelfB.get_books() == shelf_B_books

    library = Library()
    assert library.get_books() == []
    library.add_shelf(shelfA)
    library.add_shelf(shelfB)
    assert set(library.get_books()) == set(shelf_A_books + shelf_B_books)

    assert library.is_book_in_library(shelf_A_books[0]) is True
    assert (
        library.is_book_in_library(
            Book("Non Existing Book", Author("John", "Doe"), 2024, Genre.Fiction)
        )
        is False
    )
    library.remove_shelf(shelfA)
    assert set(library.get_books()) == set(shelf_B_books)


def test_e74():
    customer = Customer("John", "Doe")
    card = Card(
        card_number="1234",
        card_holder="John Doe",
        account_number="1234",
        expiration_date="2024-12-31",
        pin="1234",
    )
    assert isinstance(card, Card)
    account = Account("1234", customer, 1000, [card])
    assert isinstance(account, Account)
    assert account.account_number == "1234"


def test_e75():
    customer = BankCustomer("John", "Doe")
    account1 = Account("acc-1234", customer, 1000)
    card1 = Card("1234", "John Doe", "acc-1234", "2024-12-31", "1234")
    account1.add_card(card1)

    account2 = Account("acc-5678", customer, 2000)
    card2 = Card("5678", "John Doe", "acc-5678", "2024-12-31", "5678")
    account2.add_card(card2)

    assert customer.get_total_balance() == 0.0
    customer.add_account(account1)
    assert customer.get_total_balance() == 1000
    customer.add_account(account2)
    assert customer.get_total_balance() == 3000
    assert customer.get_card("1234") == card1
    assert customer.get_card("5678") == card2
    assert customer.get_account("acc-1234") == account1
    assert customer.get_account("acc-5678") == account2

    assert customer.deposit("acc-1234", 500) is None
    assert customer.get_account("acc-1234").balance == 1500
    assert customer.get_total_balance() == 3500

    with pytest.raises(ValueError):
        customer.withdraw("acc-1234", 1_000_000, "1234", "1234")
    with pytest.raises(ValueError):
        customer.withdraw("acc-1234", 1_000, "1234", "WRONG_PIN")


def test_e76():
    box1 = Box[int]()
    box1.add(5)
    assert isinstance(box1.get(), int)
    assert box1.get() == 5

    box2 = Box[float]()
    box2.add(5.5)
    assert isinstance(box2.get(), float)

    box3 = Box[str]()
    box3.add("Hello")
    assert isinstance(box3.get(), str)
    assert box3.get() == "Hello"


def test_e77():
    assert create_content(Blogger(), "New Post") == "Creating a new post: New Post"
    assert (
        create_content(Vlogger(), "New Video")
        == "Creating a new video: New Video with path: /videos/New Video.mp4"
    )

    class NotAContentCreator:
        pass

    with pytest.raises(AttributeError):
        create_content(NotAContentCreator(), "New Content")


def test_e78():
    course = Course("Python Programming", "CS101")
    assert course.course_name == "Python Programming"
    assert course.course_code == "CS101"
    assert course.professor is None
    assert course.students == []

    professor = Professor("Dr. Clark", "clark@uni.edu", "1234")
    course.assign_professor(professor)

    student_names = ["Alice", "Bob", "Charlie"]
    students = [
        Student(name, f"{name.lower()}@uni.edu", f"{name.lower()}1234")
        for name in student_names
    ]
    for student in students:
        student.enroll(course)

    assert course.professor == professor
    assert set(course.list_students()) == set(student_names)

    course2 = Course("Mathematics", "MATH101")
    assert course2.professor is None
    assert course2.students == []
    professor2 = Professor("Dr. Smith", "smith@uni.edu", "5678")
    course2.assign_professor(professor2)
    assert course2.professor == professor2
    assert course2.students == []
