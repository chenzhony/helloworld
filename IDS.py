# Iterative Deepening Search(IDS)
# take the initial node and goal node, variable moveNum is to calculate the number of move
# nextNode function as parameter go in IDS function
# IDS is composed of a loop of Iterative Deepening and Depth-first search(DFS) function
# path is the shortes path from initial node to goal
def IDS (initial,nextNode,goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]],moveNum=0):    
    def DFS (path,iterNum): 
        nonlocal moveNum            #nonlocal variable calculate the number of move function 
        if path[-1] == goal:
            return path
        if iterNum == 0:            #determine the depth of currentnode
            return
        for subNodes in nextNode(path[-1]):
            moveNum += 1            
            if subNodes not in path:
                next_path = DFS(path + [subNodes], iterNum - 1)
                if next_path:       #Determine whether to return to the previous node to expand another subnode
                    return next_path
                
                
                
    #execute from here !!!!!!!!!!!          
    #Iterative Deepening increase one depth each time          
    import itertools
    for iterNum in itertools.count():
        path = DFS([initial],iterNum)
        if path:        #if path exist, get goal
            return path,moveNum
        
        
# expand node  
def nextNode(currentNode):  
    
    #get tile 0 position to every node
    def getIndex(currentNode):
        for i,j in enumerate(currentNode):
            for k,l in enumerate(j):
                if l == 0:
                    return i,k
                
    #move tiles and copy wrap the data of tile
    #using deepcopy to copy new variable not just copy pointer
    def copyNode(x1,y1):
        import copy
        grid = copy.deepcopy(currentNode)
        grid [x1][y1], grid[x][y] = grid[x][y],grid[x1][y1]
        return grid
    
    #Execute from here !!!!!!!!!!!! 
    subNode = []
    x,y = getIndex(currentNode)

    #check which direction can move
    if x > 0:
        subNode.append(copyNode(x-1,y))  
    if x < 2:
        subNode.append(copyNode(x+1,y))
    if y > 0:
        subNode.append(copyNode(x,y-1))
    if y < 2:
        subNode.append(copyNode(x,y+1))
    return subNode

def main():
    list1 = [[[0,7,1],[4,3,2],[8,6,5]],
             [[5,6,0],[1,3,8],[4,7,2]],
             [[3,5,6],[1,2,7],[0,8,4]],
             [[7,3,5],[4,0,2],[8,1,6]],
             [[6,4,8],[7,1,3],[0,2,5]],
             [[3,2,0],[6,1,8],[4,7,5]],
             [[0,1,8],[3,6,7],[5,4,2]],
             [[6,4,1],[7,3,2],[0,5,8]],
             [[0,7,1],[5,4,8],[6,2,3]],
             [[5,4,0],[2,3,1],[8,7,6]],
             [[8,6,7],[2,5,4],[3,0,1]]
             ]
    for list2 in list1:
        import timeit
        start = timeit.default_timer()
        path,moveNum = IDS(list2,nextNode)
        print("the number of moves:",len(path)-1)
        print("the number of calls function",moveNum)
        stop = timeit.default_timer()
        print('Time: ', stop - start)  

if __name__ == "__main__":
    main()


