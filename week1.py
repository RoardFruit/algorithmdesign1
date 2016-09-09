__author__ = 'Mr.gong'

def inversionsCount(a):
    def merge(src,dst,start,mid,to):
        i=start
        j=mid+1
        count=0
        k=start
        while i<=mid and j<=to:
            if src[i]<=src[j]:
                dst[k]=src[i]
                i+=1
                k+=1
            else:
                dst[k]=src[j]
                count+=mid-i+1
                j+=1
                k+=1
        if i==mid+1 and j<to+1:
            dst[k:to+1]=src[j:to+1]
        elif j==to+1 and i<mid+1:
            dst[k:to+1]=src[i:mid+1]
        return count

    def inversions(src,dst,start,to):
        if start==to:
            return 0
        else:
            mid=(start+to)/2
            lcount=inversions(dst,src,start,mid)
            rcount=inversions(dst,src,mid+1,to)
            mcount=merge(src,dst,start,mid,to)
            return lcount+rcount+mcount

    import copy
    b=copy.copy(a)
    import time
    start = time.clock()
    count=inversions(b,a,0,len(a)-1)
    end = time.clock()
    print start,end,end-start
    return count

File=open('F://coursera/algorithm-design-analysis1/IntegerArray.txt')
a=[]
for line in File:
    line=line.rstrip()
    a.append(int(line))
if __name__ == "__main__":
    import cProfile
    cProfile.run("inversionsCount(a)")
