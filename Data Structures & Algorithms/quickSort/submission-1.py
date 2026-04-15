# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        pairs = self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs

    def quickSortHelper(self, arr, startIndex, endIndex):
        if (endIndex-startIndex + 1 <=1):
            return arr
        
        pivot = arr[endIndex].key
        swapPointer = startIndex

        for i in range(startIndex, endIndex+1):
            if(arr[i].key < pivot):
                temp = arr[i]
                arr[i] = arr[swapPointer]
                arr[swapPointer] = temp
                swapPointer += 1
        
        temp = arr[endIndex]
        arr[endIndex] = arr[swapPointer]
        arr[swapPointer] = temp

        self.quickSortHelper(arr, startIndex, swapPointer-1)
        self.quickSortHelper(arr, swapPointer+1, endIndex)

        return arr
        

        