newTuple = ("a","b","c","d","e","f")
newTuple1 = ("g","h","i","j","k","l")
print(newTuple)
print(newTuple1)

### by using concatenation operator
print(newTuple + newTuple1)

### Now we cannot multiply the tuples but we can mutiply individual numbers to the tuples
print(newTuple*2)

### Search for a element in Tuple
print("a" in newTuple)

### Count Method in Tuple
print(newTuple.count("a"))

### Access Tuple using Index
print(newTuple.index("b"))

### Find llength of tuple
print(len(newTuple))

### Find Maximum in Tuple
print(max(newTuple))

### Find Minimum in tuple
print(min(newTuple))
