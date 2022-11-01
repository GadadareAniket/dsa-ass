#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
def pairs(arr,n,sum):
  for i in range (0,n):
    for j in range (i+1,n):
      if (arr[i] + arr[j] ==sum):
        print("(",arr[i],",",arr[j],")")

arr = [1,7,-1,5,3,2,4]
n=len(arr)
sum=6
pairs(arr,n,sum)