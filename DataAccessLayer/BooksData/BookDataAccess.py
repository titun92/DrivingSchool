from Models.Book import Book

def AddBook(book):
    f = open('Data//Books.csv', 'a')
    f.write(book.__repr__())
    f.close()

def GetBooks():
    f = open('Data//Books.csv', 'r')
    booklist = []
    for line in f.readlines()[1:]:
        row = line.replace('\n', '').split(',')
        tempbook = Book(row[0],row[1],row[2],row[3],row[4])
        booklist.append(tempbook)
        f.close()
    return booklist

def PrintGetBooks(booklist):
    for book in booklist:
        print(book.id," - ",book.name," - ",book.author," - ",book.date," - ",book.type)

def FindBookByIDTrue(id):
    for book in GetBooks():
        if id == book.id:
            return True
        else:
            continue
    return False

def ReturnBookNameByID(id):
    for book in GetBooks():
        if id == book.id:
            return book.name.__repr__()
    else:
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
        if name == str(book.name):
            print("Book ID - Book Name - Book Author - Published - Loan Type")
            return book.__repr__().translate({ord(','): "    -    " })
    else:
        print("Didnt found Book", name, "\n")

def RemoveBookByName(name):
    booklist = GetBooks()
    headers = 'id,name,author,published,type'
    g = open('Data//Books.csv', 'w')
    g.write(headers)
    g.close()
    f = open('Data//Books.csv', 'a')
    count = 0
    flag = False
    for book in booklist:
        if book.name == name:
            flag = True
            print(str(book.name),'was removed\n')
        else:
            f.write('\n'f'{book.id},{book.name},{book.author},{book.date},{book.type}')
        count +=1
    if not flag:
        print(name,"is not in the book list, please try again.\n")
    f.close()