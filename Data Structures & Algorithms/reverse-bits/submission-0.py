class Solution:
    def reverseBits(self, n: int) -> int:
        
        # 10010
        # 01001
        decimal_result = 0
        for i in range(32):
            bit = (n >> i) & 1
            decimal_result += (bit << (31 - i))

        return decimal_result
