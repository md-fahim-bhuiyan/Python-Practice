listA = [1, 2, 3, 4, 5, 6, "BD"]

print("List :", listA)
print("Length: ", len(listA))

print(type(listA[6]))

# Int Number Input
inputList = input("Enter a list of elements(int), separated by spaces: ")


splitList = inputList.split()




newList = [int(num) for num in splitList]
print("Your Input List: ", newList)

# All data input on String
inputAllList = input("Enter a list of elements, separated by spaces: ").split()
print("Length: ", len(inputAllList))
print(inputAllList)


