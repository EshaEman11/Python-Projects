from BL.Muser import MUser
class MUserUI:
     @staticmethod
     def menu():
       print(">> Login Menu")
       print("1. SignIn")
       print("2. SignUp")
       print("3. Exit")
       print("Enter Option")
       option = int(input())
       return option

     @staticmethod
     def printList(usersList):
      for user in usersList:
        print(user.userName,user.userPassword, user.userRole)
        option = int(input())

     @staticmethod
     def TakeInputFromConsole():
       userName = input("Enter UserName: ")
       userPassword = input("Enter UserPassword: ")   
       userRole = input("Enter UserRole: ");
       user = MUser(userName, userPassword, userRole)
       return user

     @staticmethod
     def takeInputwithOutRole():
      userName = input("Enter UserName: ")
      userPassword = input("Enter UserPassword: ")
      user = MUser(userName, userPassword, None)
      return user