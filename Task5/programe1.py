class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model=model
    def display_info(self):
        print(f" vehicle brand is {self.brand} \n model is {self.model}")
class Car(Vehicle):
    def __init__(self,brand,model,number_of_doors ):
        super().__init__(brand,model)
        self.number_of_doors=number_of_doors
    def display_info(self):
        super().display_info()
        print(f"No of doors:{self.number_of_doors}")


class Bike(Vehicle):
    def __init__(self,brand,model,engine_capacity):
        super().__init__(brand, model)
        self.engine_capacity=engine_capacity
    def display_info(self):
        super().display_info()
        print(f"engine capacity is: {self.engine_capacity}")

car=Car("toyota","hyundai",4)
bike=Bike("pulzer","activa","50cc")

car.display_info()
bike.display_info()