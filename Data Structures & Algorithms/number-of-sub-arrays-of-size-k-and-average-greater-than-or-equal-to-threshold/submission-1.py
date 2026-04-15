class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #Constraints
        # Window = size k
        # Average must be greater than or equal to threshold

        # 2 7 3 5 5 5 8

        # 2 2 2 2 5 5 5 8

        # running_sum = 8
        # window = 2 2 2 2

        running_sum = 0
        sub_arrays = 0

        L = 0

        for R in range(len(arr)):
            running_sum += arr[R]
            if R - L + 1 == k:
                if running_sum / k >= threshold:
                    sub_arrays += 1
            if R - L + 1 > k:
                running_sum -= arr[L]
                L += 1
                if running_sum / k >= threshold:
                    sub_arrays += 1
            
        return sub_arrays
        








        
        