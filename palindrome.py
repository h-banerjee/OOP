def isPalindrome(x: int) -> bool:
    # Negative numbers and numbers ending with 0 (but not 0 itself) cannot be palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    # For odd-length numbers, discard the middle digit by dividing reversed_half by 10
    return x == reversed_half or x == reversed_half // 10

# Example Usage
print(isPalindrome(121))   # Output: True
print(isPalindrome(-121))  # Output: False
print(isPalindrome(10))    # Output: False
