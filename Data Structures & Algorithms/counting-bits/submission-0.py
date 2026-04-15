class Solution:
    def countBits(self, n: int) -> List[int]:

        if n == 0:
            return [0]

        curr_number = 0
        output = []

        while curr_number <= n:
            decimal_num = curr_number
            count_ones = 0
            while decimal_num:
                decimal_num &= (decimal_num-1)
                count_ones += 1
            
            output.append(count_ones)
            curr_number += 1
        
        return output

