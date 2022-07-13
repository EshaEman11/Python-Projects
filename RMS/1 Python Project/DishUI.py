from Dish import Dish
from DishDL import DishDL
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
    def printList (DishList):
      for dish in DishList:
        print(dish.DishName,dish.DishPrice)
    
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
   