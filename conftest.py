import pytest

from main import BooksCollector

@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture(scope='function')
def collector1():
    collector1 = BooksCollector()
    collector1.add_new_book("Книга")
    return collector1
