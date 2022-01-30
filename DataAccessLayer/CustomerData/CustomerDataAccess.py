from Models.Customer import Customer

def AddCustomer(customer):
    f = open('Data/Customers.csv', 'a')
    f.write(customer.__repr__())
    f.close()

def GetCustomers():
    f = open('Data/Customers.csv', 'r')
    customerlist = []
    for line in f.readlines()[1:]:
        row = line.split(',')
        tempcustomer = Customer(row[0],row[1],row[2],row[3])
        customerlist.append(tempcustomer)
        f.close()
    return customerlist

def PrintGetCustomers(customerlist):
    for customer in customerlist:
        print("ID:" ,customer.id,"Name:" ,customer.name,"City:" ,customer.city,"Age:",customer.age)


def FindCustomerByName(name):
    for customer in GetCustomers():
        if name == customer.name:
            print("Successfully print\n")
            return customer.__repr__().translate({ord(','): " " })


def FindCustomerByID(id):
    for customer in GetCustomers():
        if id == customer.id:
            return True
        else:
            continue
    else:
        return False

def FindCustomerByID2(id,name):
    for customer in GetCustomers():
        if id == customer.id and name == customer.name:
            return True
        else:
            continue


def RemoveCustomerByName(name):
    f = open("Data/Customers.csv", "r")
    lines = f.readlines()
    flag = False
    for index,line in enumerate(lines):
        if name in line:
            print("Successfully Removed Customer\n")
            del lines[index]
            flag = True
    if not flag:
        print("No such customer,please try again.\n")

    f.close()

    new_file = open("Data/Customers.csv", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()

# PrintGetCustomers(GetCustomers())

# def FindCustomerByID(id):
#     for customer in GetCustomers():
#         if id == customer.id:
#             # print(book.id, type(book.id))
#             # print(book.type, type(book.type))
#             # print(book)
#             # print(type(book))
#             return Customer(int(customer.id),customer.name,customer.city,customer.age)


            # print(book.id, book.name, book.author, book.date, book.type)
            # print(type(book.id), type(book.name), type(book.author), type(book.date), type(book.type))

# print(FindCustomerByID("1"),type(FindCustomerByID("1")))
