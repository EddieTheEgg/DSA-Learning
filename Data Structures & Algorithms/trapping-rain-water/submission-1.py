class Solution:
    def trap(self, height: List[int]) -> int:
        #We want the total area which is the max between the
        #entire array length (not between two specific columns lol)

        #This means we should start right and left pointer and move 
        # accordingly


        #Start left pointer at 0, and right pointer at len(height) - 1
        #Compare if left or right pointer is greater
        #We take the min (leftpointer, rightpointer) height, 
        # whichever is less we increment or decrement
        # Now we update the max of whichever pointer moved
        # To see how much water it can hold on its own 
        # so like leftMax = max(leftMax, height[i]). 

        #If height[i] is less than leftMax or rightMax, that means
        # we can trap water since nearby column is greater than current index
        # and we know the max water collection is the leftMax - height[i] where i
        # is the index of the column that could have water.

        # we know the max height of water can be that leftMax or rightMax

        L = 0
        R = len(height) - 1

        #We need to keep track of our tallest columns known
        # at each iteration, like shortening the "bowl" more and more
        leftMax = height[L]
        rightMax = height[R]

        trapped_water = 0

        while L < R:
            # Right column is always taller than left column,
            # so we can possibly trap water closest to left side
            if leftMax < rightMax:
                L += 1
                #Two situations, either a new taller or equal column, or space for water
                leftMax = max(leftMax, height[L])
                trapped_water += leftMax - height[L]
            else:
                #if both maxHeights are the same on each pointer, just iterate right down as well
                R -= 1
                rightMax = max(rightMax, height[R])
                trapped_water += rightMax - height[R]

        return trapped_water

                


            





