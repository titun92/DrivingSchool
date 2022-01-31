import csv
from csv import writer
from datetime import datetime,timedelta
from Models.Loans import Loans
from DataAccessLayer.BooksData.BookDataAccess import ReturnBookNameByID
from DataAccessLayer.CustomerData.CustomerDataAccess import ReturnCustomerNameByID

def AddLoan(loan,book):
    loan.returndate = MapReturnTime(book.type)
    f = open('Data//loans.csv', 'a', newline='')
    f.write(loan.__repr__())
    f.close()


# def AddLoan(loan,book):
#     loan.returndate = MapReturnTime(book.type)
#     with open('Data//loans.csv', 'a') as f:
#         writer = csv.writer(f)
#         writer.writerow(loan)


# def AddLoan(loan,book):
#     loan.returndate = MapReturnTime(book.type)
#     with open('Data//loans.csv', 'a') as f:
#         f = writer(f)
#         f.writerow(loan.__str__())


def MapReturnTime(type):
    today = datetime.now()
    if type == 1:
        return (today + timedelta(days=10)).strftime("%x")
    elif type == 2:
        return (today + timedelta(days=5)).strftime("%x")
    elif type == 3:
        return (today + timedelta(days=2)).strftime("%x")
    else:
        return "ERROR"

def GetLoans():
    f = open('Data//loans.csv', 'r')
    loanlist = []
    for line in f.readlines()[1:]:
        row = line.replace('\n', '').split(',')
        temploan = Loans(row[0],row[1],row[2],row[3])
        loanlist.append(temploan)
        f.close()
    return loanlist

def PrintGetLoans(loanlist):
    for loan in loanlist:
        print(loan.custid,"  -  ",loan.bookid,"  -  ",loan.loandate,"  -  ",loan.returndate)


def FindLoanedByIDTrue(bookid,loanlist):
    for i in loanlist:
        if i.bookid == bookid:
            return True
        else:
            continue
    return False

def FindLoanedByIDTrue2(custid,loanlist):
    for i in loanlist:
        if i.custid == custid:
            return True
        else:
            continue
    return False

def PrintLateLoans(loanlist):
    for loan in loanlist:
        if str(loan.returndate) < datetime.now().strftime("%x"):
            print("\n\nThe Customer",ReturnCustomerNameByID(loan.custid),
                  " is being late returning the book",ReturnBookNameByID(loan.bookid),
                  "\nCustomer ID:",loan.custid,"Book ID:",loan.bookid,"Loan Date:",
                  loan.loandate,"Return Date:",loan.returndate)
        # elif str(loan.returndate) < datetime.now().strftime("%x"):
        #     print(loan.returndate, "not late")
        else:
            return "error"

def RemoveLoanByName(custid,bookid):
    loanlist = GetLoans()
    headers = 'custid,bookid,loandate,returndate'
    g = open('Data//loans.csv', 'w')
    g.write(headers)
    g.close()
    f = open('Data//loans.csv', 'a')
    count = 0
    found = False
    for loan in loanlist:
        if loan.custid == custid and loan.bookid == bookid:
            found = True
            print(loan.__repr__(),'was removed\n')
        else:
            f.write('\n'f'{loan.custid},{loan.bookid},{loan.loandate},{loan.returndate}')
        count +=1
    if not found:
        return found
    f.close()





