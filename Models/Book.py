class Book:
    def __init__(self,id,name,author,date,type):
        self.id = id
        self.name = name
        self.author = author
        self.date = date
        self.type = type

    def __repr__(self):
        return f"\n{str(self.id)},{self.name},{self.author},{str(self.date)},{self.type}"

    # def __str__(self):
    #     return f"\n{str(self.id)},{self.name},{self.author},{str(self.date)},{self.type}"
