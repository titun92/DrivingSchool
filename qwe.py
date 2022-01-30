print("You Chose the Option for Adding a new Loan,")
print("id of the customer and id of the book\n")
tempidforbook = input("enter the ID of the book: \n")

if FindLoanedByIDTrue(tempidforbook, GetLoans()) != True and FindBookByIDTrue(tempidforbook) == True:
    y = FindBookByID2(tempidforbook)
    loan = Loans(int(input("please Enter the ID of the Customer: \n")), y.id, datetime.now().strftime("%x"), y.type)
    AddLoan(loan, y)
    print("successfully Loaned Book:", y.name, "\nCustID - BookID - LoanDate - ReturnDate\n", loan, "\n")
else:
    print("\nThis book is already taken, or not in the book list, please choose another book.\n")
