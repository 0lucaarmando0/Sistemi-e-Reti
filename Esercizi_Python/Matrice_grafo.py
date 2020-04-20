
def matrix():

    matrix=[[0 for i in range(nodes)] for j in range(nodes)]

    for i in range(1, nodes):
        list_=input(f"Insert nearby nodes to {i}: ").split(',')
        #health=input(f"Insert the healty: ").split(",")
        int_list=[int(i) for i in list_]
        #int_health=[int(i)for i in health]
        for a in int_list:
            if(i==a):
                matrix[i][a]=0
            else:
                matrix[i][a]=1 #health[i]
        
        print("matrix: ")
        for i in range(nodes):
            for j in range(nodes):
                print(matrix[i][j], end=" ")
            print()

dict_matrix={}

for i in range(nodes):
    app_list=[]
    for j in range(nodes):
        if matrix == 1:
            app_list.append(str(j))

    dict_matrix[i]=app_list

print(dict_matrix)


def main():



if __name__ == "__main__":
        main()