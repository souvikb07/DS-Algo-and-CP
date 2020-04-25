# # Implementing a Dynamic Array
# import ctypes
# class DynamicArray:
#     def __init__(self):
#         self._n = 0 # Count Actual element
#         self._capacity = 1 # capacity of array
#         self._A = self._make_array(self._capacity) # Array with capacity A

#     def __len__(self):
#         " Return number of elements"
#         return self._n

#     def __getitem__(self,k):
#         "Get Item at index k "
#         if not 0 <= k < self._n:
#             raise IndexError('invalid index')
#         return self._A[k]

#     def append(self, obj):
#         "Add object at end of array"
#         if self._n == self._capacity:
#             self.resize = (2 * self._capacity)
#         self._A[self.n] = obj
#         self._n += 1
    
#     def _resize(self, c):
#         "Resize internal array to capacity c"
#         B = self._make_array(c)
#         for k in self._n:
#             B[k] = self._A[k]
#         self._A = B
#         self._capacity = c
    
#     def _make_array(self, c):
#         "make low level array with capacity c"
#         return (c * ctypes.py_object)( )



l_0 = ['a','b','c']
l_1 = ['q','e','r','t']
l_2 = ['a','d','g','g','h']
final_list = ['s']
for i in range(1,3):
    final_list.append((globals()['l_%s' % i]))
final_list.pop(0) 
print(final_list)