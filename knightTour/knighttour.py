import sys
sys.path.append('..')
from graphs import Graph
from basic import Queue

def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositons = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
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


def legalCoord(x,bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return Falsei
