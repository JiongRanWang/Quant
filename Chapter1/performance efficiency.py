import itertools
items = [1,2,3]

for item in itertools.permutations(items):
    print(item)

for item in itertools.combinations(items,2):
    print(item)

for item in itertools.combinations_with_replacement(items,2):
    print(item)

ab = ['a', 'b']
cd = ['c', 'd']
for item in itertools.product(ab,cd):
    print(item)

#笛卡尔积求最优属于有限参数范围内求最优的问题