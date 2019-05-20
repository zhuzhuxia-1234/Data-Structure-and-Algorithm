# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:06:22 2019

@author: zhuxibing
"""
#图解 冒泡，选择，插入排序算法：https://www.cnblogs.com/chengxiao/p/6103002.html
# 1.冒泡排序 算法步骤
#1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
#2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。

def bubble_sort(array):
    for i in range(1,len(array)):
        for j in range(0,len(array)-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

# 2.选择排序 算法步骤
#1.首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
#2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
#3.重复第二步，直到所有元素均排序完毕。
    
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
    return arr
            
# 3.插入排序 算法步骤
#1.将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。
#2.从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）

def insert_sort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    return arr

# 4.归并排序
## 图解归并排序算法： https://www.cnblogs.com/chengxiao/p/6194356.html
def merge_sort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0));
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0));
    while right:
        result.append(right.pop(0));
    return result


#5.希尔排序 
## 图解希尔排序算法：https://www.cnblogs.com/chengxiao/p/6104371.html
def shell_sort(arr):
    import math
    gap=1
    while(gap < len(arr)/3):
        gap = gap*3+1
    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j] > temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr

#6.快速排序
# 图解快速排序算法：https://www.cnblogs.com/MOBIN/p/4681369.html
def partition(arr,low,high): 
    i = ( low-1 )         # 最小元素索引
    pivot = arr[high]     
    for j in range(low , high):   
        # 当前元素小于或等于 pivot 
        if   arr[j] <= pivot:          
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return i+1
  
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

array=[2,4,1,5,7,3,10,8]
print(bubble_sort(array))
print(selection_sort(array))
print(insert_sort(array))
print(merge_sort(array))
print(shell_sort(array))
quickSort(array,0,len(array)-1)
print(array)