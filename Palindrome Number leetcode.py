class Solution:
    def isPalindrome(self,x: int) -> bool:
    # Check for negative numbers
        if x < 0:
            return False
    
    # Convert the number to a list of digits
        numbers = [int(digit) for digit in str(x)]
    
    # Reverse the list of digits
        reversed_numbers = numbers[::-1]
    
    # Compare original and reversed numbers
        return numbers == reversed_numbers

        
