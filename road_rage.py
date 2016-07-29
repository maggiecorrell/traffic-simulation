import random
import numpy as np


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
        self.speeds = []
        self.positions = []

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
    def is_able_to_move(self, road):
        front = self.position + self.length
        if front > road.length:
            front = front % road.length
        if self.speed + front >= self.car_in_front.position:
            return False
        else:
            return True

    """ Call accelerate() or decelerate() """
    def change_speed(self, road):
        if random.random() < self.slow_percentage:
            self.decelerate()
        elif not self.is_able_to_move(road):
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

    def drive(self, road):
        self.change_speed(road)
        self.speeds.append(self.speed)
        self.move_car(road)
        self.positions.append(self.position)


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
        for idx, car in enumerate(self.cars):
            try:
                self.cars[idx].add_relative_car(self.cars[idx + 1])
            except IndexError:
                self.cars[idx].add_relative_car(self.cars[0])


class Simulation:
    def __init__(self, road_length=1000, time=60, number_of_cars=30, runs=1):
        self.road_length = road_length
        self.seconds = time
        self.number_of_cars = number_of_cars
        self.runs = runs
        self.speeds = []
        self.positions = []

    def get_mean(self):
        return np.mean(self.speeds)

    def get_stdev(self):
        return np.std(self.speeds)

    def run_simulation(self):
        road = Road()
        road.place_cars()
        road.relative_position()
        for _ in range(self.runs):
            for unit in range(self.seconds):
                for car in road.cars:
                    car.drive(road)
            for car in road.cars:
                self.speeds.append(car.speeds)
                self.positions.append(car.positions)

        self.speeds = np.array(self.speeds)
        self.positions = np.array(self.positions)
        mean = self.get_mean()
        stdev = self.get_stdev()
        speed_limit = int(round(mean + stdev))
        return self.speeds, self.positions, mean, stdev, speed_limit


def main():
    simulate = Simulation(1000, 60, 30, 10)
    speeds, positions, mean, stdev, speed_limit = simulate.run_simulation()
    return speeds, positions, mean, stdev, speed_limit

if __name__ == '__main__':
    main()
