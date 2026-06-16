'''
#Data Analysis: This is te process inspecting, cleaning, transfroming, and modeling data to discover useful insights.
Types of DA
------------
1.Descriptive Analysis
-----------------------
-->Summarizing data
2.Diagnostic Analysis
---------------------
-->understanding causes
3.Predictive Analysis
---------------------
-->Forecasting future outcomes
4.Prescriptive Analysis
-----------------------
-->Suggesting actions based on data

Why DA?
-------
--To improve decision making
--detects trends & pattern


NumPy (Numerical Python):
--This python library for numerical computing.It provides support for multi-dimensional arrays, and linear algebra operation, making if essentails for DA.

using numpy in DA
-----------------
--->improved performance
--->simplifies complex operations
--->easy data manipulation
'''

# one-dimentional array
import numpy as np
arr=np.array([1,2,3,4])
print(arr)

#2-dimentional array
import numpy as np
arr=np.array([[2,3,4],[3,4,5]])
print(arr)

#3-dimentional array
import numpy as np
arr=np.array([[3,4,5],[6,7,8],[2,3,8]])
print(arr)


#program
import numpy as np
arr=np.array([[2,3,4],[5,6,7]])
print(arr)
print(arr.shape)
reshaped=arr.reshape(3,2)
print(reshaped)


#
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr+2)

#matrix multiplication
import numpy as np
A = np.array([[1, 2],[3, 4]])
B = np.array([[5, 6],[7, 8]])
C = np.dot(A, B)
print(C)

##
import numpy as np
arr=np.array([10,20,30])
nrm_copy=arr.view()
arr[0]=100
print(nrm_copy)
print(arr)

##
import numpy as np
arr=np.array([10,20,30])
copy_deep=arr.copy()
arr[1]=200
print(copy_deep)
print(arr)

'''
Pandas:the pandas is a powerful data manipulation and analysis library.
-->where it provides data structure like series and dataframe for efficient data handling.
methods for Series:
--------------------
mean(),sum(),max(),min(),apply(),map()
'''
import pandas as pd
any=pd.Series([2999,15999,52999,4999,1999],
              index=["earbuds","smartphone","lap","watch","footware"])
print(any)

#Dataframe
data={"Product":["Earbuds","Smartphone","Lap","Watch","Footware"],
      "Brand":["Noise","OnePlus","HP","Bolt","Nike"],
      "Price":[1599,15999,53999,1999,3999],
      "stock":[50,15,25,40,70]}
dip=pd.DataFrame(data)
print(dip)

