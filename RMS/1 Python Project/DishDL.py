import os.path
from Dish import Dish

class DishDL:
    DishList = []

    @staticmethod
    def addDishIntoList(dish):
        DishDL.DishList.append(dish)

    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line[0], line[1]

    @staticmethod
    def readDishFromFile(path):
       if (os.path.exists(path)):
           fileVariable = open(path, 'r')
           records = fileVariable.read().split("\n")
           fileVariable.close()
           for line in records:
                DishName, DishPrice = DishDL.parseData(line)
                Dish = Dish(DishName, DishPrice)
                DishDL.addDishIntoList(path)
           return True
       else:
           return False

    @staticmethod  
    def storeDishIntoFile(dish, path):
       file = open(path, 'a')
       file.write("\n" + dish.DishName + "," + dish.DishPrice)
       file.close()

    @staticmethod
    def sorting():
        #list.sort()
        #DishDL.DishList.sort(lambda x, y : x.price.CompareTo(y.price))

        DishDL.DishList.sort()
        print(DishDL.DishList)
        input()
        
