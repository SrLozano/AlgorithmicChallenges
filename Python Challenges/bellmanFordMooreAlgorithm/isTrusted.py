import math

def IsTrusted(node, trustGraph, pretrustedPeers, trustThreshold):

    # I'm going to use what I have learnt in heuristic and optimization at University.
    # Bellman-Ford-Moore Algorithm

    veryBigNumber = math.inf
    N = len(trustGraph)

    distances = []  # We store the distantes every
    previous = []  # In order to build the paths

    for i in range(0, N):  # We fill the lists so we can detect the main node 
        if i == node:
            distances.append(0)
            previous.append(-1)
        else:
            distances.append(veryBigNumber)
            previous.append(-1)

    for current in range(0, N):
        for i in range(0, N):
            if trustGraph[current][i] != 0:  # If it is an adjacent node
                if distances[current] + trustGraph[current][i] < distances[i]:
                    # We update the lists with the path information gathered
                    distances[i] = distances[current] + trustGraph[node][i]
                    previous[i] = current

    # Now we select only the nodes that have been trusted
    distances_trusted = []

    for element in pretrustedPeers:
        distances_trusted.append(distances[element])

    # Final comprobation
    if min(distances_trusted) <= trustThreshold:
        return True
    else:
        return False

# The result for number 1 must be: false
matrix1 = [[0, 2, 3],
           [2, 0, 2],
           [3, 2, 2]]
node1 = 0
pretrustedPeers1 = [2]
trustThreshold1 = 1

# The result for number 2 must be: true
matrix2 = [[0, 2, 0],
           [2, 0, 2],
           [0, 2, 0]]
node2 = 0
pretrustedPeers2 = [2]
trustThreshold2 = 10

# The result for number 3 must be: false
matrix3 = [[0, 2, 0],
           [2, 0, 2],
           [0, 2, 0]]
node3 = 0
pretrustedPeers3 = [2]
trustThreshold3 = 1


while(1):
    print("Welcome to my implemantation of the Bellman-Ford-Moore Algorithm")
    a = input("Enter the set of test you would like to test ")
    if len(a) != 0:
        if a == str(1):
            result = IsTrusted(node1, matrix1, pretrustedPeers1, trustThreshold1)
        elif a == str(2):
            result = IsTrusted(node2, matrix2, pretrustedPeers2, trustThreshold2)
        elif a == str(3):
            result = IsTrusted(node3, matrix3, pretrustedPeers3, trustThreshold3)
        else:
            print("Problems ocurred")
            result = False
        print("Can you trust the node? " + str(result))
        print("")
    else:
        print("The number can not be empty")


     