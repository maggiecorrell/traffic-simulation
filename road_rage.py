class Car:
    def __init__(self, position, car_in_front=None):
        self.position = position
        self.speed = 0
        self.length = 5
        """ Max Speed/Second"""
        self.max_speed = 33.3
        self.buffer = self.speed
        self.accelerate = 2
        self.car_in_front = car_in_front

    def __repr__(self):
        return "Position: {}, Speed: {}, Car in front: {}".format(self.position, self.speed, self.car_in_front)

    def change_speed(self):
        if self.speed + self.accelerate <= self.max_speed:
            self.speed += self.accelerate

    def new_position(self):
        self.position += self.speed

    def add_relative_car(self, relative_car):
        self.car_in_front = relative_car


class Road:
    def __init__(self, number_of_cars=30, length=1000):
        self.number_of_cars = number_of_cars
        self.length = length
        self.cars = []

    def place_cars(self):
        position = 0
        for _ in range(self.number_of_cars):
            self.cars.append(Car(position))
            position += self.length/self.number_of_cars

    def relative_position(self):
        for idx, car in enumerate(self.cars):
            print(self.cars[idx])
            try:
                car.add_relative_car(self.cars[idx + 1])
            except IndexError:
                
            # except IndexError:
            #     car.add_relative_car(self.cars[0])


Rainbow = Road()
Rainbow.place_cars()
Rainbow.relative_position()
print(Rainbow.cars[7])
