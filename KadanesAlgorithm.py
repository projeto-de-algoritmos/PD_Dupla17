# https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1/?page=1&category[]=Dynamic%20Programming&sortBy=submissions

#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        maiorPoss = arr[0]
        maximoVez = 0
        
        for i in range(0, N):
            maximoVez = maximoVez + arr[i]
            if maximoVez < 0:
                maximoVez = 0
                
            elif (maiorPoss < maximoVez):
                maiorPoss = maximoVez
                
            if (maximoVez == 0 and arr[i] > maiorPoss):
                maiorPoss = arr[i]
                
        return maiorPoss

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends