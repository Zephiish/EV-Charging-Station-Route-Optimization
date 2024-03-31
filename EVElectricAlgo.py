import heapq

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self, from_node, to_node, weight):
        self.adj_list.setdefault(from_node, []).append((to_node, weight))
        self.adj_list.setdefault(to_node, []).append((from_node, weight))  

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.adj_list}
    distances[start] = 0
    prioQ = [(0, start)]
    
    while prioQ:
        currentDistance, currentNode = heapq.heappop(prioQ)
        
        if currentDistance > distances[currentNode]:
            continue
        
        for neighbor, weight in graph.adj_list[currentNode]:
            distance = currentDistance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(prioQ, (distance, neighbor))
    
    return distances

def recRoute(distances, chargeStations):
    nearStation = min(chargeStations, key=lambda station: distances[station])
    return nearStation

def pathCheck(distances, chargeStations):
    minDistance = float('inf')
    recStation = None
    
    for station in chargeStations:
        if distances[station] < minDistance:
            minDistance = distances[station]
            recStation = station
    
    return recStation

# Create the graph
graph = Graph()
edges = [
        ('a', 'b',6), ('a', 'f',5), #a
        ('b', 'c',5), ('b', 'g',6), #b
        ('c', 'd',7), ('c', 'h',5), #c
        ('d', 'e',7), ('d','i',8),  #d
        ('e','i',6), ('e','n',15),  #e
        ('f','g',8), ('f','j',7),   #f
        ('g','h',9), ('g','k',8),   #g
        ('h','i',12),               #h
        ('i','m',10),               #i
        ('j','k',5),('j','o',7),    #j
        ('k','l',7),                #k
        ('l','m',7), ('l','p',7),   #l
        ('m','n',9),                #m
        ('n','r',7),                #n
        ('o','p',13),('o','s',9),   #o
        ('p','q',8), ('p','u',11),  #p
        ('q','r',9),                #q
        ('r','w',10),               #r
        ('s','t',9),                #s
        ('t','u',8),                #t
        ('u','v',8),                #U  
        ('v','w',5)                 #V
        
        ]

for edge in edges:
    graph.add_edge(*edge)

# Define charging stations
chargeStations = ['h', 'k', 'q', 't']

# Find shortest paths from node ' ' to all nodes
def getInput():
    while True:
        startNode = input("Enter the node you would like to start at: ").lower()
        if startNode in graph.adj_list:
            return startNode
        else:
            print("Invalid node. Please enter a valid node.")

# Input and find shortest paths
startNode = getInput()
distances = dijkstra(graph, startNode)

# Recommend route to the nearest charging station
nearStation = recRoute(distances, chargeStations)
print(f"The nearest charging station from node {startNode} is {nearStation}.")

# Analyze paths and recommend the most efficient route
recStation = pathCheck(distances, chargeStations)
print(f"The most efficient route to a charging station from node {startNode} is {recStation}.")

# Output the shortest distances to all nodes
print("Shortest distances to all nodes:")
for node, distance in distances.items():
    print(f"Node {node}: {distance}")

