from itertools import product
from itertools import permutations

print(['Alice', 'Bob', 'Charlie']  + [0, 1, 2, 3, 4])       #Rule of Sum

for p in product(['a', 'b', 'c'], ['x', 'y']):              #Rule of Product
  print("".join(p))
  
for p in product("ab", repeat=3):                           #Tuples
  print("".join(p))

for p in permutations("abcd", 2):                           #Permutations
  print("".join(p))
