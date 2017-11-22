
import sys
sys.path.append('..')
from graphs import Graph
from basic import Queue

def bfs(g, start, end):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
                if nbr == end:
                    print nbr.getDistance()
                    #print nbr.getPred()
                    return end
            currentVert.setColor('black')
    return "end point not found"

def traverse(y):
    x = y
    while (x.getPred()):
        print (x.getId())
        x = x.getPred()
    print(x.getPred())


def buildGraph(wordFile):
    d = {}
    g = Graph()
    with open(wordFile) as wfile:
        for line in wfile:
            word = line.strip()
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if d.get(bucket, False):
                    d[bucket].append(word)
                else:
                    d[bucket] = []
                    d[bucket].append(word)

    #return d

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

g = buildGraph('four_letter_words.txt')
end = bfs(g, g.getVertex('fool'), g.getVertex('sage'))
traverse(end)
#print repr(len(result.getVertices()))
#print "_ope=> ", result["_ope"]
#print "p_pe=> ", result["p_pe"]
#print "po_e=> ", result["po_e"]
#print "pop_=> ", result["pop_"]
#print "l_ke=> ", result["l_ke"]

