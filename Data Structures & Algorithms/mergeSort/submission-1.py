# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mainMerge(pairs, 0, len(pairs)-1)

    def mainMerge(self, arr, startIndex, endIndex):
        if (endIndex-startIndex +1 <= 1):
            return arr

        middleIndex = startIndex + (endIndex - startIndex) // 2

        self.mainMerge(arr, startIndex, middleIndex)
        self.mainMerge(arr, middleIndex+1, endIndex)

        self.merge(arr, startIndex, middleIndex, endIndex)

        return arr

    def merge (self, arr, startIndex, middleIndex, endIndex):
        leftSubArray = arr[startIndex: middleIndex+1]
        rightSubArray = arr[middleIndex+1: endIndex+1]

        left = 0
        right = 0
        mainArrPointer = startIndex

        while left < len(leftSubArray) and right < len(rightSubArray):
            if leftSubArray[left].key <= rightSubArray[right].key:
                arr[mainArrPointer] = leftSubArray[left]
                left += 1
            else:
                arr[mainArrPointer] = rightSubArray[right]
                right += 1
            mainArrPointer += 1

        while left < len(leftSubArray):
            arr[mainArrPointer] = leftSubArray[left]
            left += 1
            mainArrPointer += 1
        
        while right < len(rightSubArray):
            arr[mainArrPointer] = rightSubArray[right]
            right += 1
            mainArrPointer += 1




