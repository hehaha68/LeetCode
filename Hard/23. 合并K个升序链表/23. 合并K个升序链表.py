# -*- coding: utf-8 -*-
""" 
@Time    : 2022/2/10 17:21
@Author  : 和泳毅
@FileName: 23. 合并K个升序链表.py
@SoftWare: PyCharm
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 暴力解法
# class Solution:
#     def mergeKLists(self, lists):
#         all = []
#         for elem in lists:
#             if not elem:
#                 continue
#             while elem.next:
#                 all.append(elem.val)
#                 elem = elem.next
#             all.append(elem.val)
#         all.sort()
#         result = ListNode()
#         node = result
#         for elem in all:
#             node.next = ListNode(val=elem)
#             node = node.next
#         return result.next

# 根据有序规律结合优先队列解法
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        priority_queue = []
        for list_node in lists:
            if list_node:
                heapq.heappush(priority_queue, (list_node.val, list_node.next))

        result = ListNode()
        node = result
        while priority_queue:
            node_val, node_next = heapq.heappop(priority_queue)
            node.next = ListNode(node_val)
            node = node.next
            if node_next:
                heapq.heappush(priority_queue, (node_next.val, node_next.next))
        return result.next
