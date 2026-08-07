class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        startingPixelColor = image[sr][sc]
        if startingPixelColor == color:
            return image

        def dfs(sr, sc):
            #Check out of bounds
            if sr >= len(image) or sr < 0 or sc >= len(image[0]) or sc < 0:
                return 
            
            if image[sr][sc] != startingPixelColor:
                return
            else:
                image[sr][sc] = color
            
            dfs(sr + 1, sc)
            dfs(sr - 1, sc)
            dfs(sr, sc+1)
            dfs(sr, sc-1)

        dfs(sr, sc)
        return image