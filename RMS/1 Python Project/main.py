from pickle import TRUE
from tkinter import Menu
from DishDL import DishDL
from Dish import Dish
from DishUI import DishUI
from MUser import Muser
from MUserDL import MuserDL
from MuserUI import MuserUI
from MenuUI import MenuUI
import os
from time import sleep

 # Defining Main Function 
def main():
    path = "Data.txt"
    Dishpath = "Dish.txt"
    MuserDL.readdatafromfile(path)
    DishDL.readDishFromFile(Dishpath)
    option = 0
    while (option != 4):
        os.system("cls")
        MenuUI.mainHeader()
        option = MuserUI.menu()

        # SIGN IN

        if (option == 1):
          MenuUI.clearScreen()
          MenuUI.mainHeader()
          user = MuserUI.takeinputwithoutrole()
          user = MuserDL.SignIn(user)
          if (user != None):
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
                    DishUI.printList(DishDL.DishList)
                    input()
                  elif(op == 3):
                    DishDL.sorting()
            elif(user.userRole == "Customer"):
               MenuUI.clearScreen()
               MenuUI.mainHeader()
               print("This is User")

            sleep(3)

            #  SIGN UP

        elif (option == 2): 
           MenuUI.mainHeader()
           user = MuserUI.takeinputfromConsole()
           MuserDL.adduserintolist(user)
           MuserDL.storedUserintofile(user, path)
        
        elif (option == 3):
           break

if __name__ == "__main__":
   main()