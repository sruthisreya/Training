class Animal:
    def speak(self):
        print("sound")
class Dog(Animal):
    def speak(self):
        print("Barks")
class Cat(Animal):
    def speak(self):
        print("Meow")  
dog=Dog()
cat=Cat() 
dog.speak()
cat.speak()       

