
""" Parent class  """

class Person:
    def __init__(self, fname, lname, age, nationality):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.nationality = nationality

    def get_fname(self):
        return self.fname

    def set_fname(self, fname=None):
        if fname is not None:
            self.fname = fname

    def get_lname(self):
        return self.lname

    def set_lname(self, lname=None):
        if lname is not None:
            self.lname = lname

    def get_age(self):
        return str(self.age)

    def set_age(self, age=None):
        if age is not None:
            self.age = age

    def get_nationality(self):
        return str(self.nationality)

    def set_nationality(self, nationality=None):
        if nationality is not None:
            self.nationality = nationality

    def fullname(self):
        return str(self.fname + " " + self.lname)

    def describeuser(self):
        print("\n Name: " + str(self.fullname()) +
              "\n Age: " + str(self.get_age()) +
              "\n Nationality: " + str(self.get_nationality()) + "\n")


""" creating child class """
class User(Person):

    def __init__(self, fname, lname, age, nationality, isAuthenticated):
        super(User, self).__init__(fname, lname, age, nationality)
        self.isAuthenticated = isAuthenticated

    def get_isAuthenticated(self):
        return self.isAuthenticated

    def set_isAuthenticated(self, isAuthenticated=None):
        if isAuthenticated is not None:
            self.isAuthenticated = isAuthenticated

    def describeuser(self):
        print("\n Name: " + self.fullname() +
              "\n Age: " + self.get_age() +
              "\n Nationality: " + self.get_nationality()+
              "\n User is authenticated: " +str(self.get_isAuthenticated())+"\n")


## creating u1 object User

## getting input from user
fname = str(input("Enter your first name: "))
lname = str(input("Enter your last name: "))
age = str(input("Enter your age: "))
nationality = str(input("Enter your nationality: "))


u1 = User(fname, lname, age, nationality, True)
u1.describeuser()