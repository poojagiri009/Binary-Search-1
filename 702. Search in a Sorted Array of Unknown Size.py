# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:


#TC-> O(log n) SC-> O(1)
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        low = 0
        high = 1
        while reader.get(high) < target:
            low = high
            high = high * 2
        return self.binarySearch(reader,target,low,high)

    def binarySearch(self, reader: 'ArrayReader', target: int, low:int, high:int)-> int:
        while low <= high:
            mid = low + (high-low)//2
            if reader.get(mid) == target:
                return mid
            elif target > reader.get(mid):
                low = mid + 1
            else:
                high = mid - 1
        return -1
        