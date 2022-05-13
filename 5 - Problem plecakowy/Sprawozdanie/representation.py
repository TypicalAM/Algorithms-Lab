import random
class Courier:
    def __init__(self, size: int) -> None:
        '''Create an instance and generate key values'''
        self.size = size
        self.capacity = 350 * self.size # Arbitrary choice
        self.weights = self.generate_weights()
        self.values = self.generate_values()

    def generate_weights(self) -> tuple:
        '''Generates the weights of the items'''
        weights = tuple(random.randint(15,1000) for _ in range(self.size))
        if sum(weights) <= self.capacity:
            weights = self.generate_weights()
        return weights

    def generate_values(self) -> tuple:
        '''Generates the values of the items'''
        return tuple(random.randint(150,15000) for _ in range(self.size))

    def __repr__(self) -> str:
        '''Print the str representation of the instance'''
        size = self.size
        capacity = self.capacity
        return f'Courier({size=}, {capacity=})'
