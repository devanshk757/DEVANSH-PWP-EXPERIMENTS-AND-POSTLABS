# import numpy as np  
# list1 = [2, 4, 6, 8]   
# array1 = np.array(list1)   
# print(array1)


# import numpy as np
# array1 = np.array([10, 9, 6, 7])
# print(array1)



# import numpy as np
# array1 = np.zeros(4)
# print(array1)



# import numpy as np
# array1 = np.arange(5)
# print("Using np.arange(5):", array1)
# array2 = np.arange(1, 9, 2)
# print("Using np.arange(1, 9, 2):",array2)



# import numpy as np
# array1 = np.random.rand(5)
# print(array1)





# import numpy as np
# arr1=np.array([10,20,30])
# print("My 1D array:\n",arr1)








# arr2 = np.array([[10,20,30],[40,50,60]])
# print("My 2D numpy array:\n", arr2)




# arr= np.arange(0, 20, 3)
# print ("A sequential array with steps of 3:\n", arr)









# arr= np.linspace(0, 3, 5)
# print ("A sequential array with 5 values between 0 and 5:\n", arr)




# arr = np.ones((2,3))
# print("numpy array:\n", arr)
# print("Type:", type(arr))






# import numpy as np
# int_array = np.array([-3, -1, 0, 1])
# float_array = np.array([0.1, 0.2, 0.3])
# complex_array = np.array([1+2j, 2+3j, 3+4j])
# print(int_array.dtype) 
# print(float_array.dtype)  
# print(complex_array.dtype) 










# import numpy as np
# array1 = np.array([1, 3, 7], dtype='int8')
# array2 = np.array([2, 4, 6], dtype='uint16')
# array3 = np.array([1.2, 2.3, 3.4], dtype='float32')
# array4 = np.array([1+2j, 2+3j, 3+4j], dtype='complex64')
# print(array1, array1.dtype)
# print(array2, array2.dtype)
# print(array3, array3.dtype)
# print(array4, array4.dtype)












# import numpy as np
# int_array = np.array([1, 3, 5, 7])
# float_array = int_array.astype('float')
# print(int_array, int_array.dtype)
# print(float_array, float_array.dtype)










# import numpy as np
# array1 = np.array([[2, 4, 6],
#                   [1, 3, 5]])
# print(array1.ndim)








# array1 = np.array([[1, 2, 3],
#                  [6, 7, 8]])
# print(array1.size)








# import numpy as np
# array1 = np.array([[1, 2, 3],
#                 [6, 7, 8]])
# print(array1.shape)








# import numpy as np
# array1 = np.array([6, 7, 8])
# print(array1.dtype)









# import numpy as np
# array1 = np.array([6, 7, 8, 10, 13])
# array2 = np.array([6, 7, 8, 10, 13], dtype=np.int32)
# print(array1.itemsize)  
# print(array2.itemsize)  











# import numpy as np
# array1 = np.array([6, 7, 8])
# array2 = np.array([[1, 2, 3],
#                    	    [6, 7, 8]])
# print("\nData of array1 is: ",array1.data)
# print("Data of array2 is: ",array2.data)









# import numpy as np
# p = [[1, 0], [0, 1]]
# q = [[1, 2], [3, 4]]
# print("Original matrices:")
# print(p)
# print(q)
# result1 = np.dot(p, q)
# print("Result of the matrix multiplication:")
# print(result1)









# import numpy as np
# from numpy import linalg as LA
# a = np.array([[1, 0], [1, 2]])
# print("Original 2-d array")
# print(a)
# print("Determinant of the said 2-D array:")
# print(np.linalg.det(a))










#post lab
#1
# import numpy as np
# matrix = np.arange(2, 11).reshape(3, 3)
# print("3x3 Matrix with values from 2 to 10:")
# print(matrix)



#2
# import numpy as np
# arr = np.array([1, 9, 7, 12, 10])
# reversed_arr = arr[::-1]
# print("Original array:", arr)
# print("Reversed array:", reversed_arr)






# #3
# import numpy as np
# arr1 = np.array([1, 2, 3, 4, 5])
# arr2 = np.array([4, 5, 6, 7, 8])
# common_values = np.intersect1d(arr1, arr2)
# print("Array 1:", arr1)
# print("Array 2:", arr2)
# print("Common values:", common_values)







# #4
# import numpy as np
# arr = np.array([1, 2, 3])
# repeated_arr = np.repeat(arr, 3)
# print("Original array:", arr)
# print("Repeated array:", repeated_arr)




# #5
# import numpy as np
# arr = np.array([10, 20, 30, 40, 50, 60, 70])
# print("Memory size (bytes):", arr.nbytes)





#6
# import numpy as np
# zeros_arr = np.zeros((3, 3))
# ones_arr = np.ones((3, 3))
# print("Array of Zeros:\n", zeros_arr)
# print("Array of Ones:\n", ones_arr)





#7
import numpy as np
arr = np.array([13, 55, 19, 30, 45, 39, 88, 100, 10, 25, 70, 18, 12])
thirteenth_element = arr[12]
print("Array:", arr)
print("12th element:", thirteenth_element)
