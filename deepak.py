from typing import Union

def get_user_input() -> int:
    """
    Get a valid integer from user input.
    
    Returns:
        int: The number entered by the user
    """
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid integer.")

def check_number(number: int) -> bool:
    """
    Check if a number is a palindrome.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    # Convert number to string for easy comparison
    num_str = str(number)
    return num_str == num_str[::-1]

def is_palindrome() -> None:
    """
    Main function to check if a number is a palindrome.
    """
    try:
        # Get input from user
        number = get_user_input()
        
        # Check if number is palindrome
        result = check_number(number)
        
        # Display result
        print(f"The number {number} is {'' if result else 'not '}a palindrome")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    is_palindrome()
