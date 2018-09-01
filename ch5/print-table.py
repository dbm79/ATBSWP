tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(data):
    colWidth = [0] * len(data)

    for i in range( len(data) ):
        # Iterate through each item in the list based on the length of the list
        
        for item in data[i]:     
            
            if len(item) > colWidth[i]:
                colWidth[i] = len(item)
    
    # print out in a table-like format
    for i in range(len(data[0])):
        for j in range(len(data)):
            print(data[j][i].rjust(max(colWidth)), end="")
        print()

print_table(tableData)
