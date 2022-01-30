class Loans:
    def __init__(self,custid,bookid,loandate,returndate):
        self.custid = custid
        self.bookid = bookid
        self.loandate = loandate
        self.returndate = returndate

    def __repr__(self):
        return f"\n{str(self.custid)},{str(self.bookid)},{str(self.loandate)},{str(self.returndate)}"