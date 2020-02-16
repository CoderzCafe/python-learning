

class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def getfullname(self):
        return str(self.fname +" "+ self.lname)



class User(Person):

    def __init__(self, fname, lname, nationality=None):
        super(User, self).__init__(fname, lname)
        if nationality is not None:
            self.nationality = nationality

    def userdescription(self):
        print("User name: ", self.getfullname(), "\n Nationality: ", self.nationality)
