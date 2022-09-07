# Given a sorted array of integers A(0 based index) of size N 
# Find the starting and the ending position of a given integer B in array A.

# Return an array of size 2
# The first element = starting position of B in A and the second element = ending position of B in A, 
# If B is not found in A return [-1, -1].



import math

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers


    # Binary Search to index of first occurence of B in A
    def bs_left(self,A,B,n):
        start = 0
        end = n-1
        out = -1

        while(start<=end):
            mid = math.floor(start + (end-start)/2)

            if A[mid] == B:
                out = mid
                end = mid-1
            
            elif A[mid]<B:
                start = mid+1

            else:
                end = mid-1
        return out

    # Binary Search to index of last occurence of B in A
    def bs_right(self,A,B,n):
        start = 0
        end = n-1
        out = -1

        while(start<=end):
            mid = math.floor(start + (end-start)/2)
            if A[mid] == B:
                out = mid
                start = mid+1
            
            elif A[mid]<B:
                start = mid+1

            else:
                end = mid-1
        return out
            

    def searchRange(self, A, B):
        n = len(A)
        ans = []
        ans.append(self.bs_left(A,B,n))
        ans.append(self.bs_right(A,B,n))
        return ans




if __name__ == "__main__":

    # Declare array A
    arr = [1,1,1]

    # Declare element whose range is searched
    element = 5

    
    sol = Solution()
    element_range = sol.searchRange(arr,element)
    print(element_range)
















































