from representation import Courier
from strategy import Backtracking, BruteForce, Dynamic, HeuristicByProportion, HeuristicByWeight, HeuristicRandom, HeuristicByValue

c = Courier(15,0.5)

# Overwrite default values
#c.capacity=10
#c.weights=(5,3,2,4,3)
#c.values=(3,4,2,6,1)

print(f'{c=}')
print(f'{c.values=}')
print(f'{c.weights=}')

print(f'{HeuristicRandom.get_best_value(c)=}')
print(f'{HeuristicByWeight.get_best_value(c)=}')
print(f'{HeuristicByValue.get_best_value(c)=}')
print(f'{HeuristicByProportion.get_best_value(c)=}')
print(f'{Dynamic.get_best_value(c)=}')
print(f'{BruteForce.get_best_value(c)=}')
print(f'{Backtracking.get_best_value(c)=}')
#print(f'Displaying the Dynamic programming matrix...')
#Dynamic.display_matrix(c)
