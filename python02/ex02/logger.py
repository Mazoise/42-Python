import time
from random import randint
import os


def log(func):

    def wrapper(*args, **kwargs):
        timee = time.time()
        res = func(*args, **kwargs)
        timee = time.time() - timee
        fd = open("machine.log", "a")
        print("(" + os.environ["USER"] + ")Running:",
              str.ljust(" ".join(map(str.capitalize,
                        func.__name__.split('_'))), 18),
              "[ exec-time = ", end="", file=fd)
        if timee >= 1:
            print("%.3f s ]" % (timee), file=fd)
        else:
            timee *= 1000
            print("%.3f ms ]" % (timee), file=fd)
        return res
    return wrapper


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
