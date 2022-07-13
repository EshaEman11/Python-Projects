from BL.Customer import Customer
from DL.CustomerDL import CustomerDL
class CustomerUI:

    @staticmethod
    def  addCustomer():
        #__________Get book data __________
        print("As An Admin")
        print("-------------------------------------------")
        CustomerName = input("Enter Customer Name: ")
        CustomerBill = input("Enter Customer Bill: ")
        BooksBuy = input("Enter Books buy  : ")
        customerDetail = Customer(CustomerName, CustomerBill, BooksBuy)
        return customerDetail

    @staticmethod
    def printCustomer():
        print("Customer Name\t\tCustomerBill\t\tBook Quantity")
        for c in CustomerDL.CustomerList:
            print(str(c.CustomerName)+" \t\t "+str(c.CustomerBill) + "  \t\t\t  " + str(c.BooksBuy))
        option = input()
    
    @staticmethod
    def DeleteCustomer():
        name = input("Enter Customer name: ")
        if(CustomerDL.RemoveCustomer(name)):
            print("Customer Removed Successfully")
        else:
            print("Record not Found")
        op = input()
    