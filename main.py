from DataAccessLayer.CustomerData.CustomerDataAccess import *
from DataAccessLayer.BooksData.BookDataAccess import *
from DataAccessLayer.LoansData.LoansDataAccess import *

from Models.Book import Book
from Models.Customer import Customer
from Models.Loans import Loans

from datetime import datetime




option = 0
while option != 999:
    option = int(input("Hello dear libririan, Welcome to the Library Manager,\n"
                       "Please Choose an Option to continue:\n"
                       "1.Add a New Customer...\n"
                       "2.Add a New Book...\n"
                       "3.Loan a Book...\n"
                       "4.Return a Book...\n"
                       "5.Display All Books...\n"
                       "6.Display All Customers...\n"
                       "7.Display All Loans...\n"
                       "8.Display Late Loans...\n"
                       "9.Find Book by Name...\n"
                       "10.Find Customer By Name...\n"
                       "11.Remove Book...\n"
                       "12.Remove Customer...\n"
                       "or enter the number 999 to exit\n"))
    # add customer
    # customer = Customer(13,"ragnarok","machester",5)

    if option == 1:
        print("You Chose the Option for Adding a new Customer,")
        print("The Program is going to need you to know the next values for the customer, please make sure you know them : ")
        print("id, name, city, age\n")
        id = input("please Enter the ID of the Customer: \n")
        if FindCustomerByID(id) != True:
            customer = Customer(id,input("please Enter the Name of the Customer: \n"),
                            input("please Enter the City of living for the Customer: \n"),
                            input("please Enter the age of the Customer: \n"))

            AddCustomer(customer)
            print("successfully added: ", customer, "\n")
        else:
            print("\nThe id", id, "is aleady in the Customer list, please chose other id.\n")


        # add book
        # AddBook(book)
        # book2 = Book()

    elif option == 2:
        print("You Chose the Option for Adding a new Book,")
        print("The Program is going to need you to know the next values for the customer, please make sure you know them : ")
        print("id(just a number) , name , author, year published (1999 for example), The book type set the maximum loan time for the book:  1 – up to 10 days  2 – up to 5 days  3 – up to 2 days")
        print("just enter a number 1,2 or 3\n")
        id = input("please Enter the ID for the Book: \n")
        if FindBookByIDTrue(id) != True:
            print(FindBookByIDTrue(id))
            book = Book(id,input("please Enter the Name of the Book: \n"),
                        input("please Enter the name of the Author: \n"),
                        int(input("please Enter the year the book was published: \n")),
                        int(input("please Enter the book type set(1 – up to 10 days  2 – up to 5 days  3 – up to 2 days): \n")))
            AddBook(book)
            print("\nSuccessfully added: ", book, "\n")
        else:
            print("\nThe id", id, "is aleady in the Book list, please chose other id.\n")



        # add loan
        # loan = Loans(1,20,datetime.now().strftime("%x"),0)
        # LoansDataAccess.AddLoan(loan,book)

    elif option == 3:
        print("You Chose the Option for Adding a new Loan,")
        print("id of the customer and id of the book\n")
        tempidforbook = input("enter the ID of the book: \n")
        y = FindBookByID2(tempidforbook)
        if FindLoanedByIDTrue(tempidforbook,GetLoans()) != True and y != False:
            loan = Loans(int(input("please Enter the ID of the Customer: \n")),y.id,datetime.now().strftime("%x"),y.type)
            AddLoan(loan,y)
            print("successfully Loaned Book:",y.name,"\nCustID - BookID - LoanDate - ReturnDate\n", loan,"\n")
        else:
            print("\nThis book is already taken, or not in the book list, please choose another book.\n")


        # loan remover or book return
        # RemoveLoanByName("77","30")
    elif option == 4:
        print("You Chose the Option to Return a Book,")
        print("The Program is going to need you to know the next values for the customer, please make sure you know them: ")
        print("Customer id, Book id\n")
        custid = input("Please Enter the Customer ID: ")
        if FindLoanedByIDTrue2(custid,GetLoans()) == True:
            bookid = input("Please Enter the Book ID: \n")
            if FindBookByIDTrue(bookid) == True:
                if RemoveLoanByName(custid,bookid) != False:
                    print("\nsuccessfully removed a Loan\n")
                else:
                    print("Failed to remove")
            else:
                print("\nthe book id:", bookid, "is not in the book list\n")
        else:
            print("\nthe customer", custid, "is not in the list.\n")



        # PrintGetBooks(GetBooks())
    elif option == 5:
        print("You Chose the Option to Display all Books: \n")
        print("Book ID ,Book Name ,Author Name ,Published ,Loan Type \n ")
        PrintGetBooks(GetBooks())
        print("successfully printed\n")
    # print customers
    # PrintGetCustomers(GetCustomers())
    elif option == 6:
        print("You Chose the Option to Display all Customers: \n")
        print("Customer ID, Customer Name, City ,Age \n ")
        PrintGetCustomers(GetCustomers())
        print("successfully printed\n")


        # print loans
        # PrintGetLoans(GetLoans())
    elif option == 7:
        print("You Chose the Option to Display all Loans: \n")
        print("CustId ,BookId, Loandate, Returndate \n ")
        PrintGetLoans(GetLoans())
        print("successfully printed\n")

    # print late loans
    # PrintLateLoans(GetLoans())
    elif option == 8:
        print("You Chose the Option to Display Late Loans: \n")
        print("\ntodays date is,",datetime.now().strftime("%x"))
        PrintLateLoans(GetLoans())
        print("")

        # find book by name
        # print(FindBookByName("harry potter"))
    elif option == 9:
        print("You Chose the Option to Find Book by Name: \n")
        print("Book ID ,Book Name ,Author Name ,Published ,Loan Type \n ")
        print(FindBookByName(str(input("Please enter a book name: \n"))))
        print("successfully printed\n")

        # print(FindCustomerByName("name"))
    elif option == 10:
        print("You Chose the Option to Find Customer by name: \n")
        print("Customer ID, Customer Name, City ,Age \n ")
        print(FindCustomerByName(str(input("Please enter a Customer name: \n"))))
        print("successfully found\n")

    # remove book
    # RemoveBookByName("name")
    elif option == 11:
        print("You Chose the Option to Remove a Book: \n")
        RemoveBookByName(str(input("Please enter a Book name: \n")))
        print("successfully Removed\n")

        # RemoveCustomerByName("name")
    elif option == 12:
        print("You Chose the Option to Remove a Customer: \n")
        RemoveCustomerByName(str(input("Please enter a Customer name: \n")))
    else:
        print("an error")