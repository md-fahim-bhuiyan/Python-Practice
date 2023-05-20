setA = {1, 2, 3, 5, 'Fahim', "Farhan", "Alve"}
setB = set([10, 20.4, 30.4, "Bangladesh", "India", "Pakistan"])

print("SetA Type=", type(setA))
print("SetB Type=", type(setB))

setA.add(9)
setA.update(['Shakib', 'Ovi', 'Riaz'])
print("Update SetA Type=", setA)

set1 = {1, 2, 3}
set2 = {2, 3, 4}

union_set = set1 | set2  # Union of two sets
intersection_set = set1 & set2  # Intersection of two sets
difference_set = set1 - set2  # Set difference of set1 and set2
symmetric_difference_set = set1 ^ set2  # Symmetric difference of set1 and set2

print('\n')
print('Union Set= ', union_set)
print('Intersection Set= ', intersection_set)
print('Difference Set= ', difference_set)
print('Symmetric Difference Set= ', symmetric_difference_set)

