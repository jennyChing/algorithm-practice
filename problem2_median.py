def median_elemet (a,b,c):
	if ( a <= b and b <= c )or(c <= b and b <= a ) :
		return True 

def quicksort(A,begin,end) :
	count = 0
	if end - begin <= 1:
		return 0
	else :
		med = begin +  (end - begin + 1)/2 - 1
		
		if median_elemet(A[begin],A[med],A[end-1]) :
			A[begin], A[med] = A[med] , A[begin]
		elif median_elemet(A[begin],A[end-1],A[med]) :
			A[begin], A[end-1] =  A[end-1], A[begin]	
		
		split = partition(A,begin,end)
		count = end - begin - 1
		lc = quicksort(A,begin,split)				
		rc = quicksort(A,split+1,end)
		return count + lc + rc
	

def partition(A,begin,end) :
	pivot = A[begin]
	i = begin + 1

	for j in range(begin+1,end) :
		if A[j] < pivot :					
			A[i], A[j] = A[j], A[i]
			i = i + 1			
			
	A[i-1], A[begin] = A[begin], A[i-1]
	return i-1
	
#use any array like below to sort
A = [ ]
for line in open("/Users/jennyching/documents/Algorithm-Khanacademy/QuickSort.txt",'r').readlines():	
	A.append(int(line))

print len(A)
print quicksort(A,0,len(A))