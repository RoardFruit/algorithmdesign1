__author__ = 'Mr.gong'
def  dijkstra(graph):
    numVertices=len(graph)
    solvedSet=set([0])
    shortLength=[1000000]*numVertices
    shortLength[0]=0
    while len(solvedSet)<numVertices:
        shortl,nextVertices=min([(shortLength[s]+v,t) for s in solvedSet for t,v in graph[s] if t not in solvedSet])
        solvedSet.add(nextVertices)
        shortLength[nextVertices]=shortl
    res=[]
    for i  in [7,37,59,82,99,115,133,165,188,197]:
        res.append(shortLength[i-1])
    print res

def  dijkstraheap(graph):
    numVertices=len(graph)
    solvedSet=set([0])
    shortLength=[1000000]*numVertices
    shortLength[0]=0
    import heapq
    heap=[]
    for t,v in graph[0]:
        heapq.heappush(heap,(v,t))
    while len(solvedSet)<numVertices:
        shortl,nextVertices=heapq.heappop(heap)
        if nextVertices not in solvedSet:
            solvedSet.add(nextVertices)
            shortLength[nextVertices]=shortl
            for t,v in graph[nextVertices]:
                if t not in solvedSet:
                    heapq.heappush(heap,(shortl+v,t))
    res=[]
    for i  in [7,37,59,82,99,115,133,165,188,197]:
        res.append(shortLength[i-1])
    print res

File=open('F://coursera/algorithm-design-analysis1/dijkstraData.txt')
graph=[]
for line in File:
    line=line.rstrip()
    graph.append([[int(i.split(',')[0])-1,int(i.split(',')[1])] for i in line.split()[1:]])
dijkstra(graph)
dijkstraheap(graph)
if __name__ == "__main__":
    import cProfile
    cProfile.run("dijkstra(graph)")
    cProfile.run("dijkstraheap(graph)")
