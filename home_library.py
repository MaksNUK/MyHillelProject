class Home_library:
    def fake_db():
        fake_db = csv.reader("fake_db.csv", delimiter=',')
        print(fake_db)

        def add_book(self):

            pass

        def remove_book(self):
            pass

        def sort_book(self):
            pass

    class Book:
        def __init__(self, title, author, genre, height, publisher):
            self.title = title
            self.author = author
            self.genre = genre
            self.height = height
            self.publisher = publisher


if __name__ == "__main__":
    Home_library.fake_db()
