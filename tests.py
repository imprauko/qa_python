from main import BooksCollector
import pytest


class TestBooksCollector:

    @pytest.mark.parametrize(
        'valid_names_books',
        [
            'П',
            'Вт',
            'Тридцать девятьТридцать девятьТридцать ',
            'Сорок сорок сорок сорок сорок сорок соро',
        ]
    )

    def test_add_new_book_valid_add(self, valid_names_books):
        collector = BooksCollector()

        collector.add_new_book(valid_names_books)

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'not_valid_names_books',
        [
            '',
            'Сорок один сорок один сорок один сорок од',
            'Сорок два сорок два сорок два сорок два со',
        ]
    )
    def test_add_new_book_not_valid_not_add(self, not_valid_names_books):
        collector = BooksCollector()
        collector.add_new_book(not_valid_names_books)

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_same_book_not_add(self):
        collector = BooksCollector()
        collector.add_new_book("Книга")
        collector.add_new_book("Книга")

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('valid_genres', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_valid_set(self, valid_genres):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', valid_genres)
        assert collector.books_genre['Книга']==valid_genres

    @pytest.mark.parametrize('not_valid_genres', ['', 'Драмы'])
    def test_set_book_genre_not_valid_not_set(self, not_valid_genres):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', not_valid_genres)
        assert collector.books_genre['Книга'] == ''

    def test_get_books_genre_show_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        books = collector.get_books_genre()
        assert books == collector.books_genre

    def test_get_book_genre_show_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        genre = collector.get_book_genre('Книга')
        assert genre == "Фантастика"

    @pytest.mark.parametrize('valid_genres', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_valid_show_books(self, valid_genres, bookscollector):

        assert len(bookscollector.get_books_with_specific_genre(valid_genres)) == 2

    def test_get_books_for_children_show_books(self, bookscollector):
        assert len(bookscollector.get_books_for_children()) == 6

    def test_add_book_in_favorites_exist_book_add(self, bookscollector):
        bookscollector.add_book_in_favorites('Книга')
        assert len(bookscollector.favorites) == 1

    def test_add_book_in_favorites_not_exist_book_not_add(self, bookscollector):
        bookscollector.add_book_in_favorites('Фильм')
        assert len(bookscollector.favorites) == 0

    def test_delete_book_from_favorites_exist_book_delete_favorite(self, bookscollector):
        bookscollector.add_book_in_favorites('Книга')
        bookscollector.delete_book_from_favorites('Книга')
        assert len(bookscollector.favorites) == 0

    def test_get_list_of_favorites_books_show_favorites(self, bookscollector):
        bookscollector.add_book_in_favorites('Книга')
        assert bookscollector.get_list_of_favorites_books()==bookscollector.favorites