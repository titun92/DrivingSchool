from Models.Customer import Customer

def AddCustomer(customer):
    f = open('Data//Customers.csv', 'a')
    f.write(customer.__repr__())
    f.close()

def GetCustomers():
    f = open('Data//Customers.csv', 'r')
    customerlist = []
    for line in f.readlines()[1:]:
        row = line.replace('\n', '').split(',')
        tempcustomer = Customer(row[0],row[1],row[2],row[3])
        customerlist.append(tempcustomer)
    f.close()
    return customerlist


def PrintGetCustomers(customerlist):
    for customer in customerlist:
        print(customer.id,"  -  ",customer.name,"  -  ",customer.city,"  -  ",customer.age)
        # print("ID:" ,customer.id,"Name:" ,customer.name,"City:" ,customer.city,"Age:",customer.age)


def FindCustomerByName(name):
    for customer in GetCustomers():
        if name == str(customer.name):
            print("Customer ID  - Customer Name  - Customer City  -  Customer Age")
            return customer.__repr__().translate({ord(','): "      -      " })
    else:
        print("Didnt found customer",name,"\n")

def ReturnCustomerNameByID(id):
    for customer in GetCustomers():
        if id == customer.id:
            return customer.name.__repr__()
    else:
        return False

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
    customerlist = GetCustomers()
    headers = 'id,name,city,age'
    g = open('Data//Customers.csv', 'w')
    g.write(headers)
    g.close()
    f = open('Data//Customers.csv', 'a')
    count = 0
    flag = False
    for cust in customerlist:
        if cust.name == name:
            flag = True
            print(str(cust.name),'was removed\n')
        else:
            f.write('\n'f'{cust.id},{cust.name},{cust.city},{cust.age}')
        count +=1
    if not flag:
        print(name,"not in the customer list.\n")
    f.close()

# PrintGetCustomers(GetCustomers())

