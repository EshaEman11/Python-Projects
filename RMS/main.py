from pickle import TRUE
from tkinter import Menu
from DL.DishDL import DishDL
from BL.Dish import Dish
from UI.DishUI import DishUI
from BL.Muser import MUser
from DL.MuserDL import MUserDL
from UI.MuserUI import MUserUI
from UI.MenuUI import MenuUI
from DL.CustomerDL import CustomerDL
from UI.CustomerUI import CustomerUI
import os
from time import sleep

 # Defining Main Function 
def main():
    path = "Data.txt"
    Dishpath = "Dish.txt"
    customerpath = "customer.txt";
    MUserDL.readDataFromFile(path)
    DishDL.readDishFromFile(Dishpath)
    option = 0
    while (option != 4):
        os.system("cls")
        MenuUI.mainHeader()
        option = MUserUI.menu()

        # SIGN IN

        if (option == 1):
          MenuUI.clearScreen()
          MenuUI.mainHeader()
          user = MUserUI.takeInputwithOutRole()
          user = MUserDL.SignIn(user)
          if(user != None):
              if (user.userRole == "Admin"):
                #Admin Menu
                while(True):
                  MenuUI.clearScreen()
                  MenuUI.mainHeader()
                  op = MenuUI.adminMenu()
                  MenuUI.clearScreen()
                  MenuUI.mainHeader()
                  
                  if(op == 1):
                    dish = DishUI.addDish()
                    DishDL.addDishIntoList(dish)
                    DishDL.storeDishIntoFile(dish,Dishpath)
                  
                  elif(op == 2):
                    DishUI.printList()
                  
                  elif(op == 3):
                    DishUI.searchDish()
                  
                  elif(op == 4):
                    DishUI.DeleteDish()

                  elif(op == 5):
                    customer = CustomerUI.addCustomer()
                    CustomerDL.addCustomerInList(customer)
                    CustomerDL.storecustomerIntoFile(customer,customerpath)

                  elif(op == 6):
                    CustomerUI.printCustomer()
                  
                  elif(op == 7):
                    CustomerUI.DeleteCustomer()
                  elif(op == 8):
                    break;
              elif(user.userRole == "Customer"):
                MenuUI.clearScreen()
                MenuUI.mainHeader()
                while(True):
                  MenuUI.clearScreen()
                  MenuUI.mainHeader()
                  op = MenuUI.CustomerMenu()
                  MenuUI.clearScreen()
                  MenuUI.mainHeader()
                  
                  if(op == 1):
                    DishUI.printList()
                  
                  elif(op == 2):
                    DishUI.searchDish()

                  elif(op == 3):
                    DishUI.addOrder()
                  
                  elif(op == 4):
                    break;

              sleep(3)

            #  SIGN UP

        elif (option == 2): 
           MenuUI.mainHeader()
           user = MUserUI.TakeInputFromConsole()
           MUserDL.addUserIntoList(user)
           MUserDL.storeUserIntoFile(user, path)
        
        elif (option == 3):
           break;

if __name__ == "__main__":
   main()