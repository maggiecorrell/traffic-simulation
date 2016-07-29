import random


class Car:
    def __init__(self, position, car_in_front=None):
        self.position = position
        self.speed = 0
        self.length = 5
        """ Max Speed/Second"""
        self.max_speed = 33.3
        self.acceleration = 2
        self.slow_percentage = .1
        self.car_in_front = car_in_front

    def __repr__(self):
        return "Position: {}, Speed: {}".format(self.position, self.speed)

    """ Increase speed by acceleration value """
    def accelerate(self):
        self.speed += self.acceleration
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    """ Decrease speed by acceleration value """
    def decelerate(self):
        self.speed -= self.acceleration
        if self.speed < 0:
            self.speed = 0

    """ Returns boolean if car has enough space to move """
    def is_able_to_move(self):
        front = self.position + self.length
        if self.speed + front >= self.car_in_front.position:
            return False
        else:
            return True

    """ Call accelerate() or decelerate() """
    def change_speed(self):
        if random.random() < self.slow_percentage:
            self.decelerate()
        elif not self.is_able_to_move:
            self.speed = self.car_in_front.speed
        else:
            self.accelerate()

    """ Change position of car on road based on speed """
    def move_car(self, road):
        self.position += self.speed
        if self.position > road.length:
            self.position = self.position % road.length

    """ Adds the car in front to make sure it can move """
    def add_relative_car(self, relative_car):
        self.car_in_front = relative_car


class Road:
    def __init__(self, number_of_cars=30, length=1000):
        self.number_of_cars = number_of_cars
        self.length = length
        self.cars = []

    """ Places all the cars on the appropriately lengthy road """
    def place_cars(self):
        position = 0
        for _ in range(self.number_of_cars):
            self.cars.append(Car(position))
            position += self.length/self.number_of_cars

    """ Adds the next indexed car's information to the car's attributes """
    def relative_position(self):
        print(len(self.cars))
        for idx, car in enumerate(self.cars):
            try:
                self.cars[idx].add_relative_car(self.cars[idx + 1])
            except IndexError:
                self.cars[idx].add_relative_car(self.cars[0])


Rainbow = Road()
Rainbow.place_cars()
Rainbow.relative_position()
print(Rainbow.cars[7])
