# Given a matrix of integers A of size N x M and an integer B. 
# Write an efficient algorithm that searches for integer B in matrix A.

# This matrix A has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row >= the last integer of the previous row.

# Return 1 if B is present in A, else return 0.



class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        n = len(A)
        m = len(A[0])

        # First identify row in which we have the element
        start = 0
        end = n-1
        row = -1

        while start<=end:
            mid = start + (end-start)//2
            if A[mid][0] == B:
                return 1
            elif A[mid][0] >B:
                end = mid-1
            else:
                row = mid
                start = mid + 1

        if row == -1:
            return 0

        
        start = 0
        end = m-1

        while start<=end:
            mid = start + (end-start)//2
            if A[row][mid] == B:
                return 1
            elif A[row][mid] >B:
                end = mid-1
            else:
                start = mid + 1

        return 0





if __name__ == "__main__":

    # Declare array A
    arr = [[1,1,1],
           [2,3,4],
           [4,5,6]]


    # Search for element
    element = 2


    sol = Solution()
    element_present = sol.searchMatrix(arr,element)
    print(element_present)
















































