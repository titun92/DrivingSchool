class Customer:
    def __init__(self,id,name,city,age):
        self.id = id
        self.name = name
        self.city = city
        self.age = age

    def __repr__(self):
        return f"\n{str(self.id)},{self.name},{self.city},{str(self.age)}"