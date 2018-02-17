# Heap sort
# python3.6.3
# ksnt

# The Result
# $ python heap_sort.py 
# Enter the elements to sort: 100 1 12 188 89 992 99 29
# Buit a heap.
# Initial sequence:  [992, 188, 100, 29, 89, 12, 99, 1]
# Sorted sequence:  [1, 12, 29, 89, 99, 100, 188, 992]

class MaxHeap:
      def __init__(self):
               self.arr=[]
               self.size=len(self.arr)
 
      def maxheap(self,idx):
              largest = idx
              left    = 2 * idx + 1
              right   = 2 * idx + 2
 
              if left < self.size and self.arr[left] > self.arr[largest]:
                       largest=left
              if right < self.size and self.arr[right] > self.arr[largest]:
                       largest=right
              if not largest==idx:
                         self.arr[largest],self.arr[idx]=self.arr[idx],self.arr[largest]
                         self.maxheap(largest)
 
      def buildheap(self,array):
               self.size=len(array)
               self.arr=array
               i=(self.size-2)//2
               while i>=0:
                     self.maxheap(i)
                     i = i - 1
               print("Buit a heap.")
 
def heapSort(heap):
       while heap.size >1:
               heap.arr[0],heap.arr[heap.size-1]=heap.arr[heap.size-1],heap.arr[0]
               heap.size-=1
               heap.maxheap(0)
 
seq=list(map(int,input("Enter the elements to sort: ").split()))
heap=MaxHeap()
heap.buildheap(seq)
print("Initial sequence: ",seq)   
heapSort(heap)
print("Sorted sequence: ",seq) 