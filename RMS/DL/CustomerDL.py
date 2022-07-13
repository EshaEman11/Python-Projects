import os.path
from BL.Customer import Customer

class CustomerDL:
    CustomerList = []

    path = "customer.txt"

    @staticmethod
    def addCustomerInList(customer):
        CustomerDL.CustomerList.append(customer)

    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line[0], line[1], line[2]

    @staticmethod
    def readCustomerFromFile():
        if os.path.exists(CustomerDL.path):
            file = open(CustomerDL.path, "r")
            record = file.read().split("\n")
            file.close()
            for line in record:
                CustomerName, CustomerBill, BooksBuy = CustomerDL.parseData(line)
                b = Customer(CustomerName, CustomerBill, BooksBuy)
                CustomerDL.addCustomerInList(b)
            return True
        else:
            n = input()
            return False

    @staticmethod  
    def storecustomerIntoFile(customer, path):
       file = open(path, 'a')
       file.write("\n" + customer.CustomerName + "," + customer.CustomerBill + "," + customer.BooksBuy)
       file.close()
    
    @staticmethod
    def RemoveCustomer(customer):
        i = 0
        for c in CustomerDL.CustomerList:
            if(c.CustomerName == customer):
                CustomerDL.CustomerList.pop(i)
                return True
            i = i+1
        return False