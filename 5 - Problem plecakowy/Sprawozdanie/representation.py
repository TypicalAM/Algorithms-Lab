import random
class Courier:
    def __init__(self, size: int, capacity_modifier: float) -> None:
        '''Create an instance and generate key values'''
        self.size = size

        self.weights = self.generate_weights()
        self.capacity = self.generate_capacity(capacity_modifier)
        self.values = self.generate_values()

    def generate_capacity(self, modifier: float) -> int:
        return round(sum(self.weights) * modifier)

    def generate_weights(self) -> tuple:
        '''Generates the weights of the items'''
        return tuple(random.randint(15,1000) for _ in range(self.size))

    def generate_values(self) -> tuple:
        '''Generates the values of the items'''
        return tuple(random.randint(150,15000) for _ in range(self.size))

    def __repr__(self) -> str:
        '''Print the str representation of the instance'''
        size = self.size
        capacity = self.capacity
        return f'Courier({size=}, {capacity=})'
