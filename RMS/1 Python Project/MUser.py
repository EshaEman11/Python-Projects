class Muser:
    username = ""
    userpassword = ""
    userRole = ""

    def __init__(self, username, userpassword, userRole):
        self.username = username
        self.userpassword = userpassword
        self.userRole = userRole

    def isAdmin(self):
        if(self.userRole == "Admin"):
            return True
        else:
            return False
