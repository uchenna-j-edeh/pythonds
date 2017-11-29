import sys
sys.path.append('..')
from graphs import Graph
from basic import Queue

def allMoves(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genAllMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            #import pdb; pdb.set_trace()
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    #            import pdb; pdb.set_trace()
    return ktGraph

def posToNodeId(row, column, board_size):
    return (row * board_size) + column

def genLegalMoves(x,y,bdSize):
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                                       ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX,bdSize) and \
                         legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves


def genAllMoves(x,y,bdSize):
    newMoves = []
    moveOffsets = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX,bdSize) and \
                 legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False

def knightTour(n, path, u, limit):
    """
    n represents the current dept in the search tree
    path represets a list of vertices visited thus far
    u represents the vertice in the graph we wish to explore
    limit os the number of nodes in the path
    """
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, nbrList[i], limit)
            i = i + 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
        print 'n=> ', n
        print 'path=> ', path
    return path 

def dfs(start):
    start.setColor('gray')
    print "Visted => ", start.getId()
    for nbr in start.getConnections():
        if nbr.getColor() == 'white':                
            dfs(nbr)

g = knightGraph(8) 
#g = allMoves(3)
path = []
limit = 6
print 'vertices=> ', g.getVertices()
#print 'edges=> ', g.iterkeys()

#trace = knightTour(0, path, g.getVertex(4), 63)

#g2 =  g.getVertex(2)
#for g in g2.getConnections():
#    print "=" * 10
#    print g.getId()
#    print "=" * 10

#for p in trace:
#    print p.getId()
    #print p.getConnections()

print "Number of Nodes visited is => ", dfs( g.getVertex(0))
    

