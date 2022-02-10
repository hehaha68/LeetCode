# -*- coding: utf-8 -*-
""" 
@Time    : 2022/2/10 20:26
@Author  : 和泳毅
@FileName: 25. K 个一组翻转链表.py
@SoftWare: PyCharm
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1 or not head:
            return head
        List = [0] * k
        node, new_head = head, head
        for i in range(k-1):
            if new_head.next:
                new_head = new_head.next
            else:
                return head
        head = new_head

        temp = None
        while node:
            for i in range(k):
                List[i] = node
                if node.next:
                    node = node.next
                else:
                    if temp:
                        temp.next = List[0]
                    if i == k-1:
                        List[0].next = None
                        node = None
                        break
                    return head
            if temp:
                temp.next = List[k-1]
            temp = List[0]
            for i in range(k-1,0,-1):
                List[i].next = List[i-1]
        return head