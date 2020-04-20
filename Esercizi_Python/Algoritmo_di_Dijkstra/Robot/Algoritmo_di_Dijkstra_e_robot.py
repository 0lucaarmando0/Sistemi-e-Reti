def initializeFloor(dim):
    floor = []
    for r in range(0, dim):
        row = []
        for c in range(0, dim): row.append(True)
        floor.append(row)
    return floor


def createFloor():
    dim = int(input("Insert the size of the floor: \n"))
    return initializeFloor(dim)


def stampFloor(flo):
    for r in range(0, len(flo)):
        print(" ")
        for c in range(0, len(flo)): print(flo[r][c], end=' ')


def createNodes(flo):
    nodes = 1
    for r in range(0, len(flo)):
        for c in range(0, len(flo)):
            if flo[r][c]:
                flo[r][c] = nodes
                nodes += 1


def createDic(flo):
    dict = {}
    x = 1  
    nodes = 1
    for r in range(0, len(flo)):
        for c in range(0, len(flo)):
            links = []
            if flo[r][c] != False:
                if r - x >= 0:
                    if (flo[r - x][c] != False): links.append(flo[r - x][c])
                if c - x >= 0:
                    if (flo[r][c - x] != False): links.append(flo[r][c - x])
                if c + x < len(flo):
                    if (flo[r][c + x] != False): links.append(flo[r][c + x])
                if r + x < len(flo):
                    if ([r + x][c] != False): links.append(flo[r + x][c])
                dict[nodes] = links
                nodes += 1
    return dict


def stampDict(dict):
    print("\n{")
    for key, val in dict.items(): print(f"\t{key}: {val},")
    print("}")


def occupiedCells(flo):
    while True:
        pos = input("Enter -1 to stop or insert the coordinates of the cell occupied (Put the row before and then "
                    f"the column from 1 to {len(flo)}): ")
        if pos != "-1": flo[int(pos.split(".")[0]) - 1][int(pos.split(".")[1]) - 1] = False
        else:
            if pos == "-1": break
    createNodes(flo)
    return createDic(flo)


def main():
    p = createFloor()
    stampFloor(p)
    dict = occupiedCells(p)
    stampFloor(p)
    stampDict(dict)


if __name__ == '__main__':
    main()