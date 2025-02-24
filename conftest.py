import pytest

from main import BooksCollector
@pytest.fixture(scope='function')
def bookscollector():
    bookscollector = BooksCollector()
    bookscollector.add_new_book('Книга')
    bookscollector.set_book_genre('Книга', 'Фантастика')
    bookscollector.add_new_book('Книга1')
    bookscollector.set_book_genre('Книга1', 'Фантастика')
    bookscollector.add_new_book('Книга2')
    bookscollector.set_book_genre('Книга2', 'Ужасы')
    bookscollector.add_new_book('Книга3')
    bookscollector.set_book_genre('Книга3', 'Ужасы')
    bookscollector.add_new_book('Книга4')
    bookscollector.set_book_genre('Книга4', 'Детективы')
    bookscollector.add_new_book('Книга5')
    bookscollector.set_book_genre('Книга5', 'Детективы')
    bookscollector.add_new_book('Книга6')
    bookscollector.set_book_genre('Книга6', 'Мультфильмы')
    bookscollector.add_new_book('Книга7')
    bookscollector.set_book_genre('Книга7', 'Мультфильмы')
    bookscollector.add_new_book('Книга8')
    bookscollector.set_book_genre('Книга8', 'Комедии')
    bookscollector.add_new_book('Книга9')
    bookscollector.set_book_genre('Книга9', 'Комедии')

    return bookscollector
