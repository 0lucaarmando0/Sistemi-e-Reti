def CreateMatrix():  
    dim = int(input("Insert the lenght of the matrix: \n"))

    mat = []

    for i in range(0, l):
       line = []

        for j in range(0, l):
            line.append(-1)
      
       mat.append(line) 
    
    return matrix

def fillTabel(m): 

    nodes = int(input("Insert the numeber of nodes: \n"))

    for i in range(0, nodes):
        coordx = int(input(f"Insert the x coordinate of the {i}  node : \n"))
        coordy = int(input(f"Insert the y cordinate of the {i}  node : \n"))

        m[coordx][coordy] = i 
    
    return m



def findNext(m):
    neighbors = []
    for i in range(len(m)):
        for k in range(len(m)):
            near = []
            if(m[i][k] > 0 ):
                if(m[i][k-1] > 0):
                    near.append(m[i][k-1])
                if(m[i][k+1] > 0 ):
                    near.append[m[i][k+1]]
                if(m[i+1][k] > 0):
                    near.append(m[i+1][k])
                if(m[i-1][k] > 0):
                    near.append(m[i-1][k])
            
            neighbors.append(near)
    
    return neighbors
    

            
            
                    
            
        


if __name__ == "__main__":
    matrix=matrixBorn()
    print(trovoVicini(fillTabel(matrix)))
    