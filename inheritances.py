class Customer:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def names(self):
        return self.firstname + " " + self.lastname
x=Customer("lil","jack")
print(x.names())