class Car():
    def __init__(self, brand, color, mileage):
        self.brand = brand
        self.color = color
        self.mileage = mileage
    def get_brand(self):
        print(self.brand)
    def set_brand(self,new_brand):
        self.brand = new_brand
    def set_color(self,new_color):
        print(self.color)

a_car = Car('Volvo', 'Blå', 1587)
a_car.get_brand()
a_car.set_brand('Renault')


b_car = Car('Porche', 'svart', 1400)
b_car.get_brand()
b_car.set_brand('Volvo')

car_list = [a_car, b_car]

for car in car_list:
    print(car.brand,car.color,car.mileage)
