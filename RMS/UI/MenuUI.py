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
        #_______________Admin menu_______________
        print("As An Admin");
        print("-------------------------------------------");
        print("You can choose any option from below");
        print("\t1. Add Dish");
        print("\t2. View All Dish");
        print("\t3. Search Dish");
        print("\t4. Delete Dish");
        print("\t5. Add Customer Details");
        print("\t6. View Customer Details");
        print("\t7. Delete Customer");
        print("\t8. Exit")
        op = int(input("\t\tYour Option... "))
        return op;

    @staticmethod  
    def CustomerMenu():
        #_______________Admin menu_______________
        print("As A Customer");
        print("-------------------------------------------");
        print("You can choose any option from below");
        print("\t1. View All Dishes");
        print("\t2. Search Dish");
        print("\t3. Buy Dish");
        print("\t4. Exit");
        op = int(input("\t\tYour Option... "))
        return op;