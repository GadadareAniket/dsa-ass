#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverseArray(A):
  print( A[::-1])
     
A = [1, 2, 3, 4, 5, 6]
print("Given array",A)
print("Reversed array is")
reverseArray(A)