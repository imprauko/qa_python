# qa_python
test_add_new_book_valid_add - проверяет добавление книги с пограничными значениями количества символов в названии.
test_add_new_book_not_valid_not_add - проверяет, что недопустимая по количеству символов в названии книга не будет добавлена в словарь.
test_add_new_book_same_book_not_add - проверяет невозможность добавить уже существующую книгу
test_set_book_genre_valid_set - проверяет добавление всех валидных жанров
test_set_book_genre_not_valid_not_set - проверка невозможности добавить невалидный жанр
test_get_books_genre_show_books_genre - проверка метода вызова словаря книг
test_get_book_genre_show_genre - проверка метода вызова жанра книги по ее названию
test_get_books_with_specific_genre_valid_show_books - проверка вызова списка книг по жанру
test_get_books_for_children_show_books - проверка вызова книг без возрастного рейтинга
test_add_book_in_favorites_exist_book_add - проверка добавления существующей книги в список фаворитов
test_add_book_in_favorites_not_exist_book_not_add - проверка невозможности добавить несуществующую книгу в фавориты
test_delete_book_from_favorites_exist_book_delete_favorite - проверка удаления из списка фаворитов
test_get_list_of_favorites_books_show_favorites - проверка метода вызова списка фаворитов