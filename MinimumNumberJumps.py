# https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1/?page=1&category[]=Dynamic%20Programming&sortBy=submissions

#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        if (n <= 1):
            return 0
            
        if (arr[0] == 0):
            return -1
            
        alcanceMax = arr[0]
        passos = arr[0]
        pulos = 1
        
        for i in range(1, n):
            if (i == n - 1):
                return pulos
                
            alcanceMax = max(alcanceMax, i + arr[i])
            
            passos -= 1
            
            if (passos == 0):
                pulos += 1
                
                if (i >= alcanceMax):
                    return -1
                
                passos = alcanceMax - i
        return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr,n)
        print(ans)
# } Driver Code Ends