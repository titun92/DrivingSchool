import csv
from datetime import datetime,timedelta
from Models.Loans import Loans
from DataAccessLayer.BooksData.BookDataAccess import ReturnBookNameByID
from DataAccessLayer.CustomerData.CustomerDataAccess import ReturnCustomerNameByID

def AddLoan(loan,book):
    loan.returndate = MapReturnTime(book.type)
    print(loan)
    f = open('Data//loans.csv', 'a')
    f.write(loan.__repr__())
    f.close()

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
        row = line.split(',')
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
            print("\n\nCustomer ID:",loan.custid
                  ,"Book ID:",loan.bookid,
                  "Loan Date:",loan.loandate,
                  "Return Date:",loan.returndate,
                  "The Customer",ReturnCustomerNameByID(loan.custid),
                  " is being late returning the book",
                  ReturnBookNameByID(loan.bookid))
        # elif str(loan.returndate) < datetime.now().strftime("%x"):
        #     print(loan.returndate, "not late")
        else:
            return "error"

def RemoveLoanByName(custid,bookid):
    lines = list()
    found = False
    with open('Data//loans.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        # writer = csv.writer(new_list, delimiter=',')
        for row in reader:
            lines.append(row)
            if custid in row[0] and bookid in row[1]:
                lines.remove(row)
                found = True
        if not found :
            return found
                # print(row[0:2])


    with open('Data//loans.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
        return found



