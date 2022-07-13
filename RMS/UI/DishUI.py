from BL.Dish import Dish
from DL.DishDL import DishDL
class DishUI:

    @staticmethod
    def  addDish():
        #__________Get Dish data __________
        print("As An Admin")
        print("-------------------------------------------")
        DishName = input("Enter Dish name: ")
        DishPrice = input("Enter Dish Price: ")
        DishDetail = Dish(DishName, DishPrice)
        return DishDetail

    @staticmethod
    def printList():
        print("Dish Name\t\tDishPrice")
        for c in DishDL.DishList:
            print(str(c.DishName)+" \t\t "+str(c.DishPrice))
        option = input()
    
    @staticmethod
    def viewAllDishes(DishList):
        lenght = len(DishList)
        if (lenght > 0):
                print("As An Admin");
                print("-------------------------------------------");
                print("Name\t\tPrice");
                for i in range(lenght):
                    print(DishList[i].DishName,DishList[i].DishPrice)
        option = int(input())
    
    @staticmethod
    def searchDish():
        print("As An Admin");
        print("-------------------------------------------");
        name = input("Enter Dish Name: ");
        flag = 0;
        for c in DishDL.DishList:
            if(str(c.DishName) == name):
                print("\n\t\t\t\tRECORD FOUND!!");
                print("\nName\t\tPrice");
                print(str(c.DishName)+"\t\t"+str(c.DishPrice))
                flag =1
        if(flag == 0):
            print("\n\t\t\t\tRECORD NOT FOUND!!");
        op = input()
    

    @staticmethod
    def DeleteDish():
        name = input("Enter Dish name: ")
        if(DishDL.RemoveDish(name)):
            print("Dish Removed Successfully")
        else:
            print("Record not Found")
        op = input()
    
    @staticmethod
    def addOrder():
        print("As A Customer");
        print("-------------------------------------------");
        name = input("Enter Dish Name: ");
        flag = 0;
        for c in DishDL.DishList:
            if(str(c.DishName) == name):
                print("\t\t\t\tRECORD FOUND!!");
                print("\nName\t\tPrice");
                print(str(c.DishName)+"\t\t"+str(c.DishPrice))
                print("\n\t\tYOUR BILL IS =" + str(c.DishPrice))
                flag =1
        if(flag == 0):
            print("\n\t\t\t\t Dish Not Available!!");
        op = input()

   