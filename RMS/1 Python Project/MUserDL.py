import os.path
from MUser import Muser
class MuserDL:
    usersList = []
    
    @staticmethod
    def adduserintolist(user):
        MuserDL.usersList.append(user)
 
    @staticmethod
    def SignIn(user):
        for storedUser in MuserDL.usersList:
            if(storedUser.username == user.username and storedUser.userpassword == user.userpassword):
                return storedUser
        return None   

    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line[0], line[1], line[2]

    @staticmethod
    def readdatafromfile(path):
        if(os.path.exists(path)):
            filevariable = open(path,'r')
            records = filevariable.read().split("\n")
            filevariable.close()       
            for line in records:
                username, userpassword, userRole = MuserDL.parseData(line)
                user = Muser(username, userpassword, userRole)
                MuserDL.adduserintolist(user)
            return True
        else:
            return False      

    @staticmethod
    def storedUserintofile(user, path):
        file = open(path,'a')
        file.write("\n" + user.username + "," + user.userpassword + "," + user.userRole)              
        file.close()