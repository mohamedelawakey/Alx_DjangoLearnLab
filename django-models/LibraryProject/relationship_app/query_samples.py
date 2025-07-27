from relationship_app.models import Author, Book, Librarian, Library
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    book = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in book:
        print(f"- {book.title}")
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library_name}:")
    for book in books:
        print(f"- {book.title}")
def librarians_for_library(library_name):
    library = Library.objects.get(name=library_name)
    Librarian = Librarian.objects.get(library=library)
    print(f"The librarian for {library_name} is {librarian.name}")
