class Rectangle:
    def draw(self):
        print("Drawing a rectangle")
class Circle:
    def draw(self):
        print("Drawing a circle")
def draws(drawing):
    for i in drawing:
        i.draw()
drawing=[Rectangle(),Circle(),Circle()]
draws(drawing)
