grafo = {'a':{'b':1,'c':4},'b':{'c':1, 'd':3},'c':{'d':1},'d':{}}  

def dijkstra(grafo,start):

    nodes = grafo  
    absoluteD = {}      #Contiene il numero minimo di costo per raggiungere un certo nodo 
    predecessors = {}     
    iDistance = 100000      #Inizialmente tutti i nodi hano una distanza infinita dal nodo 0
    


    for node in nodes:      #Inizializzo tutti i nodi ad un numero molto grande, che non deve essere superato dalla somma di tutti i pesi
        absoluteD[node] = iDistance
    absoluteD[start] = 0 

    while nodes:       #Il ciclo continua fin quando nel grafo ci saranno nodi             
        minNode = None              
        for node in nodes:      #Mi serve cercare il nodo minimo per poi proseguire cercando i suoi successivi
            if minNode is None:
                minNode = node
            elif absoluteD[node] < absoluteD[minNode]:      
                minNode = node

        for childNode, weight in grafo[minNode].items():                # Faccio un ciclo per ogni elmento di ogni blocco della dello shot_path
            if weight + absoluteD[minNode] < absoluteD[childNode]:      # controllo per vedere se il peso + l'etichetta nel mio nodo sono minori di quelli sucessivi(figli) 
                absoluteD[childNode] = weight + absoluteD[minNode]      # se vero, rietichetto il nodo figlio con un valore minore
                predecessors[childNode] = minNode                       # contengo la predecessori di ogni nodo
        
        nodes.pop(minNode)    # mi permette di uscire dal while
    
    print("Label min: ")
    print(absoluteD)
    print("Predecessors: ")
    print(predecessors)
    
    input("Press any key to stop! ")


if __name__ == "__main__":
    dijkstra(grafo, 'a')