class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        len1, len2 = len(nums1), len(nums2)
        num1Pointer = num2Pointer = 0
        median1 = median2 = 0

        for count in range((len1 + len2) // 2 + 1):
            median2 = median1
            if num1Pointer < len1 and num2Pointer < len2:
                if nums1[num1Pointer] > nums2[num2Pointer]:
                    median1 = nums2[num2Pointer]
                    num2Pointer += 1
                else:
                    median1 = nums1[num1Pointer]
                    num1Pointer += 1
            elif num1Pointer < len1:
                median1 = nums1[num1Pointer]
                num1Pointer += 1
            else:
                median1 = nums2[num2Pointer]
                num2Pointer += 1

        if (len1 + len2) % 2 == 1:
            return float(median1)
        else:
            return (median1 + median2) / 2.0
