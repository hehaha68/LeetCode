# -*- coding: utf-8 -*-
""" 
@Time    : 2022/2/8 20:25
@Author  : 和泳毅
@FileName: 4. 寻找两个正序数组的中位数.py
@SoftWare: PyCharm
"""


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        m = (l1 + l2) // 2
        if l1 == 0:
            if l2 % 2 == 1:
                return nums2[l2 // 2]
            else:
                return (nums2[l2 // 2 - 1] + nums2[l2 // 2]) / 2
        elif l2 == 0:
            if l1 % 2 == 1:
                return nums1[l1 // 2]
            else:
                return (nums1[l1 // 2 - 1] + nums1[l1 // 2]) / 2
        elif (l1 + l2) % 2 == 1:
            return self.median(nums1, nums2, m + 1)
        else:
            return (self.median(nums1, nums2, m) + self.median(nums1, nums2, m + 1)) / 2

    def median(self, nums1, nums2, m):
        l1, l2 = len(nums1), len(nums2)
        while l1 != 0 and l2 != 0 and m > 1:
            q = m // 2
            if q > min(l1, l2):
                q = min(l1, l2)
            if nums1[q - 1] <= nums2[q - 1]:
                nums1 = nums1[q:]
            else:
                nums2 = nums2[q:]
            m -= q
            l1, l2 = len(nums1), len(nums2)
        if l1 == 0:
            return nums2[m - 1]
        elif l2 == 0:
            return nums1[m - 1]
        else:
            return min(nums1[0], nums2[0])