__author__ = 'Mr.gong'

def quickSort(a):
    def Sort(start,to):
        if start>=to:
            return 0
        mid=(start+to)/2
        midindex=sorted([(a[start],start),(a[mid],mid),(a[to],to)])[1][1]
        temp=a[start]
        a[start]=a[midindex]
        a[midindex]=temp
        pivot=a[start]
        i=start+1
        j=start+1
        while j<=to:
            if a[j]<pivot:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                i+=1
            j+=1
        a[start]=a[i-1]
        a[i-1]=pivot
        leftcount=Sort(start,i-2)
        rightcount=Sort(i,to)
        return leftcount+to-start+rightcount
    return Sort(0,len(a)-1)

File=open('F://coursera/algorithm-design-analysis1/QuickSort.txt')
a=[]
for line in File:
    line=line.rstrip()
    a.append(int(line))
if __name__ == "__main__":
    import cProfile
    cProfile.run("quickSort(a)")