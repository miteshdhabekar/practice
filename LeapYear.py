#User function Template for python3

class Solution:
    def checkYear (self, n):
        # code here
        
        # A year is a leap year if:
        # 1. It is divisible by 400
        # 2. It is divisible by 4 but NOT by 100
        
        if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
            return 1
        else:
            return 0