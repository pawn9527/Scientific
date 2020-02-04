#!/usr/bin/env python
# coding:utf8
"""
作者:pawn
邮箱:pawn9537@gmail.com
日期:2020/2/2
时间:14:33
"""
import numpy as np
import copy


class Program:
    
    # 冒泡排序, 空间复杂度 O(1), 时间复杂度 O(n^2)
    def bubble_sort(self, array):
        n = len(array)
        for i in range(n):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array
    
    # 插入排序 空间复杂度是O(1), 时间复杂度 O(n^2)
    def insertion_sort(self, array):
        n = len(array)
        for i in range(1, n):
            current = array[i]
            j = i - 1
            while j >= 0 and current < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = current
        return array
    
    # 快速排序 时间复杂度 O(n^2) 空间复杂度 O(log n)
    def quick_sort(self, array, low, high):
        def partition(array, low, high):
            i = low - 1
            pivot = array[high]
            for j in range(low, high):
                if array[j] <= pivot:
                    i = i + 1
                    array[i], array[j] = array[j], array[i]
            array[i + 1], array[high] = array[high], array[i + 1]
            return i + 1
        
        if low < high:
            pi = partition(array, low, high)
            self.quick_sort(array, low, pi - 1)
            self.quick_sort(array, pi + 1, high)
        return array
    
    def binary_search(self, array, left, right, x):
        if right >= left:
            mid = int(left + (right - left) / 2)
            if array[mid] == x:
                return mid
            elif array[mid] > x:
                return self.binary_search(array, left, mid - 1, x)
            else:
                return self.binary_search(array, mid + 1, right, x)
        else:
            return -1
    
    def reverse_32int(self, number):
        if number >= 0:
            result = int(str(number)[::-1])
        else:
            result = -int(str(number)[:0:-1])
        if -2 ** 31 < result < 2 ** 31 - 1:
            return result
        return result
    
    def is_power_of_2(self, number):
        if number < 1:
            return False
        while number > 1:
            if number % 2:
                return False
            number = number / 2
        return True
    
    def is_power_of_2_by_bit(self, number):
        """
        如果该数是2的乘方,则该数的二进制表示仅包含一个1, 那么该数与他的减一的数相与, 一定为0
        :param number: 输入检测数字
        :return:
        """
        if number < 1:
            return False
        if number & (number - 1):
            return False
        else:
            return True
    
    def merge_orderly_list(self, list1, list2):
        """
        利用双指针来解题
        :param list1:
        :param list2:
        :return:
        """
        i = j = 0
        result = []
        while i <= len(list1) - 1 and j <= len(list2) - 1:
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
            # else:
            #     result.append(list1[i])
            #     result.append(list1[j])
            #     j += 1
            #     i += 1
        return result + list1[i:] + list2[j:]


if __name__ == '__main__':
    array = np.random.randint(100, size=100)
    program = Program()
    # array = program.bubble_sort(array)
    # array = program.insertion_sort(array)
    # array = program.quick_sort(array, 0, len(array) - 1)
    # print(array)
    # array = program.binary_search(array, 0, len(array) - 1, 99)
    # array = program.reverse_32int(-1010)
    array = program.merge_orderly_list([1, 2, 3, 1000], [0, 2, 3, 555])
    print(array)
