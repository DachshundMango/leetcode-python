class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)):
            if (nums1[i] == 0) and (len(nums2) > 0):
                nums1[i] = nums2.pop()

        plus = 0
    
        for num in nums1:
            if num < plus:
                plus = num

        if plus < 0:
            for i in range(len(nums1)):
                nums1[i] = nums1[i] - plus

        k = nums1[0]

        for i in range(len(nums1)):
            if nums1[i] > k:
                k = nums1[i]

        counting_sort = [0] * (k + 1)

        for i in range(len(nums1)):
            counting_sort[nums1[i]] += 1

        for i in range(1, len(counting_sort)):
            counting_sort[i] = counting_sort[i] + counting_sort[i-1]

        copy_nums1 = [0] * len(nums1)

        for i in range(len(nums1)):
            idx = counting_sort[nums1[len(nums1) - 1 - i]] - 1
            copy_nums1[idx] = nums1[len(nums1) - 1 - i]
            counting_sort[nums1[len(nums1) - 1 - i]] -= 1

        for i in range(len(nums1)):
            nums1[i] = copy_nums1[i] + plus



        
        
