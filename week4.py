__author__ = 'Mr.gong'

def SCC(graph,regraph):
    n=len(graph)
    def SCCfirst():
        isVisited=[False]*n
        res=[]
        def DFS(node):
            stack=[node]
            isVisited[node]=True
            while len(stack)>0:
                for neighborNode in regraph[node]:
                    if not isVisited[neighborNode]:
                        stack.append(node)
                        isVisited[neighborNode]=True
                        node=neighborNode
                        break
                else:
                    res.append(node)
                    node=stack.pop()
        for i in range(n):
            if not isVisited[i]:
                DFS(i)
        return res
    def SCCsecond(finishTime):
        isVisited=[False]*n
        belong=[0]*n
        def DFS(node,leader):
            stack=[node]
            isVisited[node]=True
            while len(stack)>0:
                for neighborNode in graph[node]:
                    if not isVisited[neighborNode]:
                        stack.append(node)
                        isVisited[neighborNode]=True
                        node=neighborNode
                        break
                else:
                    belong[node]=leader
                    node=stack.pop()
        while len(finishTime)>0:
            node=finishTime.pop()
            if not isVisited[node]:
                DFS(node,node)
        return belong
    finishTime=SCCfirst()
    belong=SCCsecond(finishTime)
    nodeCluster={}
    for i in belong:
        nodeCluster[i]=nodeCluster.get(i,0)+1
    return sorted(nodeCluster.values(),reverse=True)[:5]

File=open('F://coursera/algorithm-design-analysis1/SCC.txt')
graph=[[] for _ in range(875714)]
regraph=[[] for _ in range(875714)]
for line in File:
    line=line.rstrip()
    line=[int(i)-1 for i in line.split()]
    graph[line[0]].append(line[1])
    regraph[line[1]].append(line[0])
import sys
sys.setrecursionlimit(100000)
print 'loading done'
print SCC(graph,regraph)
#if __name__ == "__main__":
#    import cProfile
#    cProfile.run("SCC(graph,regraph)")

