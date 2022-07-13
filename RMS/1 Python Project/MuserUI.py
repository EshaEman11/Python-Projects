from MUser import Muser
class MuserUI:
    @staticmethod
    def menu():
        print("****************")
        print("1. Sign In")
        print("2. Sign Up")
        print("3. Exit")
        print("Enter Option")
        option = int(input())
        return option

    @staticmethod
    def printList(usersList):
        for user in usersList:
            print(user.username, user.userpassword, user.userRole)

    @staticmethod
    def takeinputfromConsole():
        userName = input("Enter Username: ")
        userpassword = input("Enter Your password: ")
        userRole = input ("Enter User Role; ")
        user = Muser(userName, userpassword, userRole)
        return user     

    @staticmethod
    def takeinputwithoutrole():
     username = input("Enter Username: ")
     userpassword = input("Enter Userpassword")
     user = Muser(username, userpassword, None)
     return user
