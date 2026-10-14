class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        maxL = height[0]
        maxR = height[-1]

        total = 0

        while l < r:
            if maxL <= maxR:
                l += 1
                total += max(0, maxL - height[l])
                maxL = max(maxL, height[l])
            else:
                r -= 1
                total += max(0, maxR - height[r])
                maxR = max(maxR, height[r])
        return total
        
        
        
        '''
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        minLR = [0] * n

        total = 0

        maxLeft[0] = height[0]
        for i in range(1, n):
            maxLeft[i] = max(height[i], maxLeft[i-1])
        
        maxRight[-1] = height[-1]
        for i in range(-1, -n, -1):
            maxRight[i] = max(height[i], maxRight[i+1])

        for i in range(n):
            minLR[i] = min(maxLeft[i], maxRight[i])
        
        for i in range(n):
            if height[i] <= minLR[i]:
                total += minLR[i] - height[i]
        
        return total
        '''