class Author:
    all = []  # keeps track of all authors

    def __init__(self, name: str):
        if not isinstance(name, str):
            raise Exception("Author name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return a list of related contracts"""
        return [c for c in Contract.all if c.author == self]

    def books(self):
        """Return a list of related books via contracts"""
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date: str, royalties: int):
        """Create and return a new contract"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the total royalties from all contracts"""
        return sum(c.royalties for c in self.contracts())


class Book:
    all = []  # keeps track of all books

    def __init__(self, title: str):
        if not isinstance(title, str):
            raise Exception("Book title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return a list of related contracts"""
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        """Return a list of related authors via contracts"""
        return [c.author for c in self.contracts()]


class Contract:
    all = []  # keeps track of all contracts

    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        # validate
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, (int, float)):
            raise Exception("royalties must be a number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date: str):
        """Return all contracts with the given date"""
        return [c for c in cls.all if c.date == date]
