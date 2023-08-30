"""Create a class called Author. This class will create Author objects that has an author name and a list of 
books that the author published."""

class Author:
    def __init__(self, name): # def initializer method
        self.name = name 
        self.books = [] # set books to empty list

    def publish(self, title): # takes the title of a book as an argument. Add the title of this book to this objects books list
        if title not in (self.books): # only books not in the books list can be added
            self.books.append(title)
        else:
            print(f'Sorry, the book {title} is already registered under author {self.name}.')

    def __str__(self): # define string method, returns author name and book(s), otherwise the string no books is returned. 
        # long verion of empty 
        """if self.books: # empty list will be False, list with an item will be True
            book_list = ', '.join(self.books)
        else:
            book_list = 'No books'"""
        # one line code that performs same operation as above code: 
        book_list = ', '.join(self.books) or 'No books for this Author'
        return f"Author\'s Name: {self.name}, Book Title(s): {book_list}"

def main(): # main function will create Author objects to test the Author Class

    author1 = Author('James Berry')
    author1.publish('Chicken Legs All Day')
    author1.publish('Mary Had a Little Chicken')

    author2 = Author('Jay Her')

    print(author1)
    print(author2)

    author1.publish('Chicken Legs All Day')

main() # call main function

