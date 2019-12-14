class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        cur = left        
        left = cur - k if cur - k >= 0 else 0
        right = cur + k if cur + k < len(arr) else len(arr) - 1
        while right - left + 1 > k:
            left_diff = abs(arr[left] - x)
            right_diff = abs(arr[right] - x)
            if left_diff > right_diff:
                left += 1
            else:
                right -= 1
        return arr[left : right+1]