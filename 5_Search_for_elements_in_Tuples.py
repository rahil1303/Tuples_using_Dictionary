print('b' in newTuple)

### Using Linear Search
def searchTuple(Tuplle,element):
    for i in Tuplle:
        if i == element:
            return Tuplle.index(i)
        
    return "element does not exist"
searchTuple(newTuple,"b")
### TIME COMPLEXITY IS O(N) SPACE COMPLEXITY IS O(1)
