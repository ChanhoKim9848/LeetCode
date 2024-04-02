class Solution(object):
    def largestPerimeter(self, nums):
        A = sorted(nums)[::-1]
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0
    

print(Solution.largestPerimeter(Solution,[1,2,1,10]))