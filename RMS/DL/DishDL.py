import os.path
from BL.Dish import Dish

class DishDL:
    DishList = []
    path = "Dish.txt"

    @staticmethod
    def addDishIntoList(dish):
        DishDL.DishList.append(dish)

    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line[0], line[1]

    @staticmethod
    def readDishFromFile(path):
        if os.path.exists(DishDL.path):
            file = open(DishDL.path, "r")
            record = file.read().split("\n")
            file.close()
            for line in record:
                DishName, DishPrice = DishDL.parseData(line)
                b = Dish(DishName, DishPrice)
                DishDL.addDishIntoList(b)
            return True
        else:
            n = input()
            return False

    @staticmethod  
    def storeDishIntoFile(dish, path):
       file = open(path, 'a')
       file.write("\n" + dish.DishName + "," + dish.DishPrice)
       file.close()

    @staticmethod
    def sorting():
        DishDL.DishList.sort()
        print(DishDL.DishList)
        option = input()

    @staticmethod
    def RemoveDish(book):
        i = 0
        for c in DishDL.DishList:
            if(c.DishName == book):
                DishDL.DishList.pop(i)
                return True
            i = i+1
        return False
        
