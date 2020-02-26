
# most common list

fruiteList = ["Apple", "Bananna", "Orange", "Cherry", "Blueberry"]

print(fruiteList)
print(fruiteList[1])

## negative indexes
print(fruiteList[-1])

## 2 to 4
print(fruiteList[1:4])

# list length
print(len(fruiteList))

# add items
countryFruite = ["Bananna", "Guava", "Malta", "Satkora", "Watermelon", "Betelnut"]

# adding items
fruiteList.append(countryFruite[1])
print(fruiteList)

## adding items with position
fruiteList.insert(2, countryFruite[3])
print(fruiteList)

## remove items
fruiteList.remove("Apple")
print(fruiteList)

fruiteList.pop()
print(fruiteList)
print("--Remove last index: ", fruiteList.pop(len(fruiteList)-1))
print(fruiteList)

## delete items
del fruiteList[0]
print(fruiteList)

## empty list
print("Country fruite: ", countryFruite)
print("Fruite list: " , fruiteList)

fruiteList.clear()
print("Fruite list: " , fruiteList)

### copy the list
fruiteList = countryFruite.copy()
print("Fruite list: " , fruiteList)

## join two lists
list1 = [1, 2, 3]
list2 = ["One", "Two", "Three"]
list3 = list1 + list2
print("List3: ", list3)

## make two to one
for x in list2:
    list1.append(x)

print("list1: ", list1)

# list1.extend(list2)
list1.extend(list2)
print(list1)
