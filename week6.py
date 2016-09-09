__author__ = 'Mr.gong'
def twoSum(nums):
    h = set()
    for num in nums:
        h.add(num)
    count=0
    for target in range(-10000,10001):
        for num in h:
            if target-num in h and target-num!=num:
                count+=1
                break
    print count

File=open('F://coursera/algorithm-design-analysis1/algo1-programming_prob-2sum.txt')
a=[]
for line in File:
    line=line.rstrip()
    a.append(int(line))
print 'load done'
twoSum(a)

import heapq
class maxHeap(object):
    def __init__(self):
        self.heap=[]
    def insert(self,x):
        heapq.heappush(self.heap,-x)
    def extractMax(self):
        m=heapq.heappop(self.heap)
        return -m
    def head(self):
        return self.heap[0]

def median(streams):
    res=[]
    maxheap=maxHeap()
    minheap=[]
    maxnum=0
    minnum=0
    for num in streams:
        if maxnum==minnum==0:
            maxheap.insert(num)
            maxnum+=1
        elif minnum==0:
            m=maxheap.head()
            if num>=m:
                heapq.heappush(minheap,num)
            else:
                maxheap.extractMax()
                heapq.heappush(minheap,m)
                maxheap.insert(num)
                minnum+=1
        else:
            m=maxheap.head()
            n=minheap[0]
            if num<m:
                if maxnum>minnum:
                    maxheap.extractMax()
                    heapq.heappush(minheap,m)
                    maxheap.insert(num)
                    minnum+=1
                else:
                    maxheap.insert(num)
                    maxnum+=1
            elif num>n:
                if maxnum<minnum:
                    heapq.heappop(minheap)
                    maxheap.insert(n)
                    heapq.heappush(minheap,num)
                    maxnum+=1
                else:
                    heapq.heappush(minheap,num)
                    minnum+=1
            else:
                if maxnum<=minnum:
                    maxheap.insert(num)
                else:
                    heapq.heappush(minheap,num)
        if maxnum>=minnum:
            res.append(maxheap.head())
        else:
            res.append(minheap[0])
    print res

