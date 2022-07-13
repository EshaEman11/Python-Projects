import string
from turtle import clear
import os
class MenuUI:
    @staticmethod
    def mainHeader():
        #_________DISPLAY HEADER___________
        print("\t**********************************************************************")
        print("\t***               Restaurant Mannagement System                    ***")
        print("\t**********************************************************************")
    
    @staticmethod
    def clearScreen():
            #____clear screen_____
        print("Press any key to continue ");
        os.system("cls")

    @staticmethod  
    def adminMenu():
        #_______________Admin menu_____________
        print("As An Admin")
        print("-------------------------------------------")
        print("You can choose any option from below")
        print("\t1. Add Dish")
        print("\t2. View All Dish")
        print("\t3. Sort Dish According to Price")
        print("\t4. Search Dish")
        print("\t5. Delete Dish")
        print("\t6. Add Customer Details")
        print("\t7. View Customer Details")
        print("\t10. Exit")
        op = int(input("\t\tYour Option... "))
        return op