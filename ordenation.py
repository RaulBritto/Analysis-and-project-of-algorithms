# First project to Analysis and project of algorithms UFPB course 2016.2
# Author: Raul Britto
# Enrolment: 11111960
# Date: 01/25/17


import sys

#fuction to swap values
def swap(a,b):
	temp = a
	a = b
	b = temp
	return a,b


#function to print the array
def printList(list):
	for i in range (0, len(list)):					
		print list[i]



def selectionSort(list):
	
	for i in range(0, len(list)):
		min = i 									#store the minimum index value
		for j in range(i, len(list)):				#for the right subarray
			if(list[j] < list[min]):				#if the new valeu is smaller than old value, minimum value is the new index
				min = j			
		list[i],list[min] = list[min], list[i]  	#swap values,

	
				


def insertionSort(list):
	
	for i in range(1, len(list)):					#just the subarray i to left is ordenate, the new values are ordenate one by one
		choose = list[i]							#salve the new value to be ordenate 
		index = i 									#salve the new index to be ordenate
		while index > 0 and choose < list[index-1]: #compare the new value with the left subarray, if the new value is smaller than the left
			list[index] = list[index-1]				#swap right to left
			index -= 1								#comparate with the smaller value
		list[index] = choose						#update the correct position
	


def mergeSort(list):
	
	if len(list) > 1:
		half = len(list)/2

		leftList = list[:half]
		rightList = list[half:]

		mergeSort(leftList)
		mergeSort(rightList)

		i = 0
		j = 0
		k = 0


		while i < len(leftList) and j < len(rightList):
			if leftList[i] < rightList[j]:
				list[k] = leftList[i]
				i += 1
			else:
				list[k] = rightList[j]
				j += 1
			k += 1

		while i < len(leftList):
			list[k] = leftList[i]
			i += 1
			k += 1

		while j < len(rightList):
			list[k] = rightList[j]
			j += 1
			k += 1			

	
def quickSort(list, start, end):

	if(start < end):
		aux = qSort(list, start, end)
		quickSort(list,aux[1],aux[0]-1)
		quickSort(list,aux[0]+1, aux[2])

def qSort(list, start, end):
	pivot = list[end]	

	i = start -1

	for j in range(start,end):
		if(list[j] <= pivot):
			i += 1
			list[i],list[j] = list[j], list[i]
	list[i+1], list[end] = list[end], list[i+1]

	return i+1, start, end


def heapSort(list):
	for start in range((len(list)-1)/2, -1, -1):
		createMaxHeap(list, start, len(list)-1)

	for end in range(len(list)-1, 0, -1):
   		list[end], list[0] = list[0], list[end]
  		createMaxHeap(list, 0, end - 1)
  


def createMaxHeap(list, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and list[child] < list[child + 1]:
      child += 1
    if list[root] < list[child]:
      list[root], list[child] = list[child], list[root]
      root = child
    else:
      break




def main():
	
	list = []
	while(True):
		try:
			x = input()
			list.append(x)
			#print(x)
		except(EOFError):	
			break

	if(sys.argv[1] == '1'):
		#print 'Selection Sort'
		selectionSort(list)
		printList(list)
	elif(sys.argv[1] == '2'):
		#print 'Insertion Sort'
		insertionSort(list)
		printList(list)
	elif(sys.argv[1] == '3'):
		#print 'Merge Sort'
		mergeSort(list)
		printList(list)
	elif(sys.argv[1] == '4'):
		#print 'QuickSort'
		quickSort(list, 0, len(list)-1)
		printList(list)
	elif(sys.argv[1] == '5'):
		#print 'HeapSort'
		heapSort(list)
		printList(list)
main()