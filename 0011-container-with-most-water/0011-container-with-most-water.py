class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        volume = min(height[i],height[j]) * j
        while(i < j):
            if height[i] < height[j]:
                i += 1
            else: j-= 1
            volume = max(volume,min(height[i],height[j]) * (j-i))
        return volume
