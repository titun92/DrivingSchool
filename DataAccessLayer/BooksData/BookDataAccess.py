from Models.Book import Book

def AddBook(book):
    f = open('Data\Books.csv', 'a')
    f.write(book.__repr__())
    f.close()

def GetBooks():
    f = open('Data\Books.csv', 'r')
    booklist = []
    for line in f.readlines()[1:]:
        row = line.split(',')
        tempbook = Book(row[0],row[1],row[2],row[3],row[4])
        booklist.append(tempbook)
        f.close()
    return booklist

def PrintGetBooks(booklist):
    for book in booklist:
        print(book.id,book.name,book.author,book.date,book.type)

def FindBookByIDTrue(id):
    for book in GetBooks():
        if id == book.id:
            return True
        else:
            continue
    return False


def FindBookByID2(id):
    for book in GetBooks():
        if id == book.id:
            return Book(int(book.id),book.name,book.author,book.date,int(book.type))
    else:
        return False
# print(FindBookByID("1"),type(FindBookByID("1")))

def FindBookByName(name):
    for book in GetBooks():
        if name == book.name:
            return book.__repr__().translate({ord(','): " " })

def RemoveBookByName(name):
    f = open("Data\Books.csv", "r")

    lines = f.readlines()
    for index,line in enumerate(lines):
        if name in line:
            print("Successfully print\n")
            del lines[index]
    f.close()

    new_file = open("Data\Books.csv", "w+")

    for line in lines:
        new_file.write(line)

    new_file.close()