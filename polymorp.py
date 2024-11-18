class car:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def move(self):
        print(f'{self.name} is moving')
class boat:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def move(self):
        print(f'{self.name} is moving')
class flight:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def move(self):
        print(f'{self.name} is moving')
car1=car("bmw","toyota")
boat1=boat("yacht","weee")
flight1=flight("airbuds","auuu")
for x in (car1,boat1,flight1):
    x.move()
   



    