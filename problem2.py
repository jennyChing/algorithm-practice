from sys import argv

def quicksort(array, p, r):
	count = 0
	if r - p <=1:
		return 0
	else:
		array[p],  array[r-1]=array[r-1], array[p]
		split = partition(array, p, r)
		count = r - p - 1
		lc = quicksort(array, p, split)
		rc = quicksort(array, split+1, r)
		return count + lc + rc
def partition(array, p ,r):
	pivot = array[p]
	i = p + 1
	for j in range(p+1, r):
		if array < pivot:
			array[i], array[j] = array[j], array[i]
			i = i+1
	array[i-1], array[p] = array[p], array[i-1]
	return i-1

array = []
for line in open("/Users/jennyching/documents/QuickSort.txt","r").readlines():
	array.append(int(line))
print len(array)
print quicksort(array,0,len(array))
