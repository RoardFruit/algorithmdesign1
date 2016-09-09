__author__ = 'Mr.gong'

def minCut(graphNodes):
    import random
    for i in range(len(graphNodes)-2):
        node1=random.choice(graphNodes.keys())
        node2=random.choice(graphNodes[node1])
        for node in graphNodes[node2]:
            nodeindex=graphNodes[node].index(node2)
            if node is node1:
                graphNodes[node].pop(nodeindex)
            else:
                graphNodes[node][nodeindex]=node1
                graphNodes[node1].append(node)
        graphNodes.pop(node2)
    return len(graphNodes.values()[0])

File=open('F://coursera/algorithm-design-analysis1/kargerMinCut.txt')
a={}
for line in File:
    line=line.rstrip()
    nums=[int(num) for num in line.split()]
    a[nums[0]]=nums[1:]

def findminCut(graphNodes,maxIter):
    min=None
    import copy
    for i in range(maxIter):
        graphcopy=copy.deepcopy(graphNodes)
        cur=minCut(graphcopy)
        if min is None or cur<min:
            min=cur
    return min

print findminCut(a,2000)