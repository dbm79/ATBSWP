def toString(someList):
    ''' This takes a list and returns a string '''
    someList.insert(-1, 'and')

    return ', '.join(str(x) for x in someList)
    
sampleList1 = ['apples', 'bananas', 'tofu', 'cats',]
sampleList2 = [ 2, 3, 5, 10, 4,]

print(toString(sampleList1))
print(toString(sampleList2))