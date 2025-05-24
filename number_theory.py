from typing import List, Optional, Union
import math

def is_fibonacci(n: int) -> bool:
    """
    Check if a number is a Fibonacci number.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is a Fibonacci number, False otherwise
        
    Examples:
        >>> is_fibonacci(5)
        True
        >>> is_fibonacci(7)
        False
    """
    # A number is Fibonacci if and only if one or both of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

def is_perfect_square(n: int) -> bool:
    """Check if a number is a perfect square."""
    s = int(math.sqrt(n))
    return s * s == n

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n: int) -> bool:
    """
    Check if a number is an Armstrong number.
    An Armstrong number is a number that is equal to the sum of its own digits
    each raised to the power of the number of digits.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is an Armstrong number, False otherwise
    """
    if n < 0:
        return False
    digits = str(n)
    return n == sum(int(digit) ** len(digits) for digit in digits)

def is_palindrome(n: int) -> bool:
    """
    Check if a number is a palindrome.
    A palindrome number reads the same forwards and backwards.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is a palindrome, False otherwise
    """
    if n < 0:
        return False
    return str(n) == str(n)[::-1]

def is_perfect_number(n: int) -> bool:
    """
    Check if a number is a perfect number.
    A perfect number is a positive integer that is equal to the sum of its proper divisors.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is a perfect number, False otherwise
    """
    if n <= 0:
        return False
    divisors_sum = 1  # 1 is always a divisor
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Add the other divisor if it's different
                divisors_sum += n // i
    return divisors_sum == n

def get_user_input(prompt: str) -> int:
    """
    Get a valid integer from user input.
    
    Args:
        prompt (str): Input prompt
        
    Returns:
        int: Valid integer entered by user
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer")

def main():
    """Main function to demonstrate number theory functions."""
    print("Number Theory Functions")
    print("1. Check if a number is Fibonacci")
    print("2. Check if a number is Prime")
    print("3. Check if a number is Armstrong")
    print("4. Check if a number is Palindrome")
    print("5. Check if a number is Perfect")
    print("6. Exit")
    
    while True:
        try:
            choice = get_user_input("\nEnter your choice (1-6): ")
            
            if choice == 1:
                num = get_user_input("Enter a number to check if it's Fibonacci: ")
                result = is_fibonacci(num)
                print(f"{num} is {'a Fibonacci number' if result else 'not a Fibonacci number'}")
            
            elif choice == 2:
                num = get_user_input("Enter a number to check if it's prime: ")
                result = is_prime(num)
                print(f"{num} is {'prime' if result else 'not prime'}")
            
            elif choice == 3:
                num = get_user_input("Enter a number to check if it's Armstrong: ")
                result = is_armstrong(num)
                print(f"{num} is {'an Armstrong number' if result else 'not an Armstrong number'}")
            
            elif choice == 4:
                num = get_user_input("Enter a number to check if it's palindrome: ")
                result = is_palindrome(num)
                print(f"{num} is {'a palindrome' if result else 'not a palindrome'}")
            
            elif choice == 5:
                num = get_user_input("Enter a number to check if it's perfect: ")
                result = is_perfect_number(num)
                print(f"{num} is {'a perfect number' if result else 'not a perfect number'}")
            
            elif choice == 6:
                print("Thank you for using Number Theory Functions!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 