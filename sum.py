class Car:
    # Инициализатор
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def drive_to(self, destination):
        print(f"Car {self.model} Driving to", destination)

    def __change_color(self, new_color):
        self.color = new_color
car_subaru = Car('Subaru', 'red')
car_subaru.__change_color('blue')
print(car_subaru.color)
