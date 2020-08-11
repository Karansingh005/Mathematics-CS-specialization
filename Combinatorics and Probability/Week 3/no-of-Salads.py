# Here T=`tomato', B=`bell pepper', L=`lettuce', E=`eggplant'. You can run this code and observe the result.

from itertools import combinations_with_replacement
for c in combinations_with_replacement("TBLE", 7):
    print("".join(c))
