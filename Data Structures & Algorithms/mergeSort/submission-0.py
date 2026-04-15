# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mainSort(pairs, 0, len(pairs) - 1)
        return pairs

    def mainSort(self, arr: List[Pair], startIndex: int, endIndex: int) -> None:
        if startIndex >= endIndex:
            return
        
        middleIndex = (startIndex + endIndex) // 2

        self.mainSort(arr, startIndex, middleIndex)
        self.mainSort(arr, middleIndex + 1, endIndex)

        self.merge(arr, startIndex, middleIndex, endIndex)

    def merge(self, arr: List[Pair], startIndex: int, middleIndex: int, endIndex: int) -> None:
        leftSubArray = arr[startIndex:middleIndex + 1]
        rightSubArray = arr[middleIndex + 1:endIndex + 1]

        leftPointer = 0
        rightPointer = 0
        mainPointer = startIndex

        while leftPointer < len(leftSubArray) and rightPointer < len(rightSubArray):
            if leftSubArray[leftPointer].key <= rightSubArray[rightPointer].key:
                arr[mainPointer] = leftSubArray[leftPointer]
                leftPointer += 1
            else:
                arr[mainPointer] = rightSubArray[rightPointer]
                rightPointer += 1
            mainPointer += 1

        while leftPointer < len(leftSubArray):
            arr[mainPointer] = leftSubArray[leftPointer]
            leftPointer += 1
            mainPointer += 1
        
        while rightPointer < len(rightSubArray):
            arr[mainPointer] = rightSubArray[rightPointer]
            rightPointer += 1
            mainPointer += 1

        
        
