"""
Code generator component that generates Python code from semantic information.
"""

from typing import List, Dict, Any, Optional
from ..semantic.analyzer import SemanticInfo
from ..parser.parser import ParseNode, NodeType
import math

class CodeGenError(Exception):
    """Exception raised when code generation fails."""
    pass

class CodeGenerator:
    """Generates Python code from semantic information."""
    
    def __init__(self):
        """Initialize the code generator with code templates."""
        self.templates = {
            'function': {
                'prime_check': self._generate_prime_check,
                'filter': self._generate_filter_function,
                'generic': self._generate_generic_function,
                'general': self._generate_general_python,
                'fibonacci': self._generate_fibonacci_check,
                'armstrong': self._generate_armstrong_check,
                'palindrome': self._generate_palindrome_check,
                'perfect': self._generate_perfect_check,
                'factorial': self._generate_factorial_function,
                'string_reverse': self._generate_string_reverse_function,
                'list_sum': self._generate_list_sum_function,
                'list_max': self._generate_list_max_function,
                'list_unique': self._generate_list_unique_function,
                'gcd': self._generate_gcd_function,
                'string_count': self._generate_count_vowels_consonants,
                'anagram_check': self._generate_check_anagrams,
                'string_clean': self._generate_remove_non_alpha,
                'string_max': self._generate_find_longest_word,
                'string_replace': self._generate_replace_spaces,
                'string_frequency': self._generate_count_char_frequency,
                'string_case': self._generate_toggle_case
            },
            'class': {
                'employee': self._generate_employee_class,
                'generic': self._generate_generic_class
            },
            'method': {
                'generic': self._generate_generic_method
            },
            'script': {
                'general': self._generate_general_script,
                'math_operations': self._generate_math_operations,
                'arithmetic': self._generate_arithmetic
            }
        }
    
    def generate(self, semantic_info: SemanticInfo) -> str:
        """
        Generate Python code from semantic information.
        
        Args:
            semantic_info (SemanticInfo): Semantic information to generate code from
            
        Returns:
            str: Generated Python code
        """
        # Check if this is a function-only request
        is_function_only = False
        if semantic_info.type == 'function':
            # Check the docstring for "function" keyword
            is_function_only = 'function' in semantic_info.docstring.lower() and 'python code' not in semantic_info.docstring.lower()
            
            # Check if this is an arithmetic operation
            if any(op in semantic_info.name for op in ['add', 'subtract', 'multiply', 'divide']):
                return self._generate_arithmetic_operation(semantic_info)
            
            # Check for specific algorithm types
            algorithm = semantic_info.implementation.get('algorithm')
            if algorithm == 'odd_even_check':
                return self._generate_odd_even_check(semantic_info)
            elif algorithm == 'palindrome':
                return self._generate_palindrome_check(semantic_info)
            elif algorithm == 'armstrong':
                return self._generate_armstrong_check(semantic_info)
            elif algorithm == 'perfect':
                return self._generate_perfect_check(semantic_info)
            elif algorithm == 'prime_check':
                return self._generate_prime_check(semantic_info)
            elif algorithm == 'fibonacci':
                return self._generate_fibonacci_check(semantic_info)
            elif algorithm == 'binary_search':
                return self._generate_binary_search_code()
            elif algorithm == 'bubble_sort':
                return self._generate_bubble_sort_code()
            elif algorithm == 'linked_list':
                return self._generate_linked_list_code()
            elif algorithm == 'binary_tree':
                return self._generate_binary_tree_code()
            elif algorithm == 'graph':
                return self._generate_graph_code()
            elif algorithm == 'dijkstra':
                return self._generate_dijkstra_code()
            elif algorithm == 'list_largest':
                return self._generate_list_largest_script(semantic_info)
            elif algorithm == 'list_smallest':
                return self._generate_list_smallest_script(semantic_info)
            elif algorithm == 'list_average':
                return self._generate_list_average_script(semantic_info)
            elif algorithm == 'list_median':
                return self._generate_list_median_script(semantic_info)
            elif algorithm == 'sqrt':
                return self._generate_sqrt_script(semantic_info)
            elif algorithm == 'square':
                return self._generate_square_script(semantic_info)
        
        # Handle different types of code generation
        if semantic_info.type == 'script':
            # For scripts, use the appropriate template based on implementation
            algorithm = semantic_info.implementation.get('algorithm', 'general')
            if algorithm in self.templates['script']:
                return self.templates['script'][algorithm](semantic_info)
            return self._generate_general_script(semantic_info)
        elif is_function_only:
            # Generate only the function definition
            return self._generate_function_only(semantic_info)
        else:
            # Generate full Python code
            return self._generate_full_code(semantic_info)
    
    def _generate_function_only(self, info: SemanticInfo) -> str:
        """Generate only the function definition without imports or main code."""
        if info.type != 'function':
            raise CodeGenError("Expected function type")
        
        # Get the algorithm type from implementation
        algorithm = info.implementation.get('algorithm', 'generic')
        
        # Generate appropriate function based on algorithm
        if algorithm == 'odd_even_check':
            return self._generate_odd_even_check(info)
        elif algorithm == 'palindrome':
            return self._generate_palindrome_check(info)
        elif algorithm == 'armstrong':
            return self._generate_armstrong_check(info)
        elif algorithm == 'perfect':
            return self._generate_perfect_check(info)
        elif algorithm == 'prime_check':
            return self._generate_prime_check(info)
        elif algorithm == 'fibonacci':
            return self._generate_fibonacci_check(info)
        elif algorithm == 'gcd':
            return self._generate_gcd_function()
        elif algorithm == 'lcm':
            return self._generate_lcm_function()
        elif algorithm == 'factorial':
            return self._generate_factorial_function()
        else:
            return self._generate_generic_function(info)
    
    def _generate_odd_even_check(self, info: SemanticInfo) -> str:
        """Generate code for checking if a number is odd or even."""
        return f'''from typing import Union

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

def check_number(number: int) -> str:
    """
    Check if a number is odd or even.
    
    Args:
        number (int): The number to check
        
    Returns:
        str: 'odd' if the number is odd, 'even' if the number is even
    """
    return "even" if number % 2 == 0 else "odd"

def check_odd_even() -> None:
    """
    Main function to check if a number is odd or even.
    """
    try:
        # Get input from user
        number = get_user_input()
        
        # Check if number is odd or even
        result = check_number(number)
        
        # Display result
        print(f"The number {{number}} is {{result}}")
            
    except Exception as e:
        print(f"Error: {{str(e)}}")

if __name__ == "__main__":
    check_odd_even()'''
    
    def _generate_full_code(self, info: SemanticInfo) -> str:
        """Generate full Python code with necessary imports and main function."""
        # Get the implementation details
        implementation = info.implementation
        
        # If there's a template, use it directly
        if 'template' in implementation:
            # Add common imports at the top
            imports = "from typing import Dict, List, Optional, Any\n\n"
            return imports + implementation['template']
            
        # Otherwise, use the algorithm-specific generation
        algorithm = implementation.get('algorithm', 'generic')
        
        if algorithm == 'string_count':
            return self._generate_string_count_script(info)
        elif algorithm == 'anagram_check':
            return self._generate_anagram_check_script(info)
        elif algorithm == 'string_clean':
            return self._generate_string_clean_script(info)
        elif algorithm == 'string_max':
            return self._generate_string_max_script(info)
        elif algorithm == 'string_replace':
            return self._generate_string_replace_script(info)
        elif algorithm == 'string_frequency':
            return self._generate_string_frequency_script(info)
        elif algorithm == 'string_case':
            return self._generate_string_case_script(info)
        # ... rest of the existing conditions ...
        
        # Default to general script generation
        return self._generate_general_script(info)

    # Add script generators for the new patterns
    def _generate_gcd_script(self, info: SemanticInfo) -> str:
        return '''def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return abs(a)

def main():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = gcd(a, b)
        print(f"GCD of {a} and {b} is: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_factorial_script(self, info: SemanticInfo) -> str:
        return '''def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    try:
        n = int(input("Enter a number: "))
        result = factorial(n)
        print(f"Factorial of {n} is: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_string_reverse_script(self, info: SemanticInfo) -> str:
        return '''def reverse_string(text: str) -> str:
    """
    Reverse a string.
    """
    return text[::-1]

def main():
    try:
        text = input("Enter a string: ")
        result = reverse_string(text)
        print(f"Reversed string: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_list_sum_script(self, info: SemanticInfo) -> str:
        return '''from typing import List

def sum_list(numbers: List[int]) -> int:
    """
    Sum all elements in a list.
    """
    return sum(numbers)

def get_list_input() -> List[int]:
    while True:
        try:
            numbers_str = input("Enter numbers (space-separated): ")
            return [int(n) for n in numbers_str.split()]
        except ValueError:
            print("Please enter valid integers separated by spaces.")





def main():
    try:
        numbers = get_list_input()
        result = find_max(numbers)
        print(f"Maximum element: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_list_unique_script(self, info: SemanticInfo) -> str:
        return '''from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from a list.
    """
    return list(dict.fromkeys(numbers))

def get_list_input() -> List[int]:
    while True:
        try:
            numbers_str = input("Enter numbers (space-separated): ")
            return [int(n) for n in numbers_str.split()]
        except ValueError:
            print("Please enter valid integers separated by spaces.")

def main():
    try:
        numbers = get_list_input()
        result = remove_duplicates(numbers)
        print(f"List after removing duplicates: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_fibonacci_check(self, info: SemanticInfo) -> str:
        """Generate code for Fibonacci number check."""
        return f'''from typing import Union
import math

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
    Check if a number is a Fibonacci number.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if the number is a Fibonacci number, False otherwise
    """
    # A number is Fibonacci if and only if one or both of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
    def is_perfect_square(num: int) -> bool:
        s = int(math.sqrt(num))
        return s * s == num
    
    return is_perfect_square(5 * number * number + 4) or is_perfect_square(5 * number * number - 4)

def is_fibonacci() -> None:
    """
    Main function to check if a number is a Fibonacci number.
    """
    try:
        # Get input from user
        number = get_user_input()
        
        # Check if number is Fibonacci
        result = check_number(number)
        
        # Display result
        print(f"The number {{number}} is {{'' if result else 'not '}}a Fibonacci number")
            
    except Exception as e:
        print(f"Error: {{str(e)}}")

if __name__ == "__main__":
    is_fibonacci()'''

    def _generate_armstrong_check(self, info: SemanticInfo) -> str:
        """Generate code for Armstrong number check."""
        return f'''from typing import Union

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
    Check if a number is an Armstrong number.
    An Armstrong number is a number that is equal to the sum of its own digits
    each raised to the power of the number of digits.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if the number is an Armstrong number, False otherwise
    """
    if number < 0:
        return False
    digits = str(number)
    return number == sum(int(digit) ** len(digits) for digit in digits)

def is_armstrong() -> None:
    """
    Main function to check if a number is an Armstrong number.
    """
    try:
        # Get input from user
        number = get_user_input()
        
        # Check if number is Armstrong
        result = check_number(number)
        
        # Display result
        print(f"The number {{number}} is {{'' if result else 'not '}}an Armstrong number")
            
    except Exception as e:
        print(f"Error: {{str(e)}}")

if __name__ == "__main__":
    is_armstrong()'''

    def _generate_palindrome_check(self, info: SemanticInfo) -> str:
        """Generate code for checking if a number is a palindrome."""
        return f'''from typing import Union

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
        print(f"The number {{number}} is {{'' if result else 'not '}}a palindrome")
            
    except Exception as e:
        print(f"Error: {{str(e)}}")

if __name__ == "__main__":
    is_palindrome()'''

    def _generate_perfect_check(self, info: SemanticInfo) -> str:
        """Generate code for perfect number check."""
        return f'''from typing import Union
import math

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
    Check if a number is a perfect number.
    A perfect number is a positive integer that is equal to the sum of its proper divisors.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if the number is a perfect number, False otherwise
    """
    if number <= 0:
        return False
    divisors_sum = 1  # 1 is always a divisor
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:  # Add the other divisor if it's different
                divisors_sum += number // i
    return divisors_sum == number

def is_perfect() -> None:
    """
    Main function to check if a number is a perfect number.
    """
    try:
        # Get input from user
        number = get_user_input()
        
        # Check if number is perfect
        result = check_number(number)
        
        # Display result
        print(f"The number {{number}} is {{'' if result else 'not '}}a perfect number")
            
    except Exception as e:
        print(f"Error: {{str(e)}}")

if __name__ == "__main__":
    is_perfect()'''

    def _generate_prime_check(self, info: SemanticInfo) -> str:
        """Generate code for prime number check."""
        return f'''from typing import Union
import math

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
    Check if a number is prime.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def is_prime() -> None:
    """
    Main function to check if a number is prime.
    """
    try:
        # Get input from user
        number = get_user_input()
        
        # Check if number is prime
        result = check_number(number)
        
        # Display result
        print(f"The number {{number}} is {{'' if result else 'not '}}prime")
            
    except Exception as e:
        print(f"Error: {{str(e)}}")

if __name__ == "__main__":
    is_prime()'''
    
    def _generate_filter_function(self, info: SemanticInfo) -> str:
        """Generate code for filtering even numbers function."""
        return f'''def {info.name}(numbers: List[int]) -> List[int]:
    """
    {info.docstring}
    
    Args:
        numbers (List[int]): List of numbers to filter
        
    Returns:
        List[int]: List containing only even numbers
    """
    return [n for n in numbers if n % 2 == 0]
'''
    
    def _generate_generic_function(self, info: SemanticInfo) -> str:
        """Generate code for generic function."""
        params = ', '.join(f"{p['name']}: {p['type']}" for p in info.parameters)
        return f'''def get_user_input(prompt: str = "Enter a number: ") -> int:
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

def {info.name}({params}) -> {info.return_type}:
    """
    {info.docstring}
    
    Args:
        {self._format_params_docstring(info.parameters)}
        
    Returns:
        {info.return_type}: Description of return value
    """
    # Get input from user
    number = get_user_input()
    
    # TODO: Implement function logic
    return True

def main():
    """Main function to demonstrate the function."""
    try:
        # Call the function
        result = {info.name}()
        
        # Display result
        print(f"Result: {{result}}")
            
    except Exception as e:
        print(f"Error: {{str(e)}}")

if __name__ == "__main__":
    main()'''
    
    def _generate_employee_class(self, info: SemanticInfo) -> str:
        """Generate code for Employee class."""
        return f'''class {info.name}:
    """
    {info.docstring}
    """
    
    def __init__(self, name: str, salary: float):
        """
        Initialize Employee.
        
        Args:
            name (str): Employee name
            salary (float): Employee salary
        """
        self.name = name
        self.salary = salary
    
    def display_details(self) -> str:
        """
        Display employee details.
        
        Returns:
            str: Formatted employee details
        """
        return f"Employee: {{self.name}}, Salary: ${{self.salary:,.2f}}"
'''
    
    def _generate_generic_class(self, info: SemanticInfo) -> str:
        """Generate code for generic class."""
        # Generate attributes
        attrs = []
        for attr in info.implementation.get('attributes', []):
            attrs.append(f"        self.{attr['name']} = {attr['name']}")
        
        # Generate methods
        methods = []
        for method in info.implementation.get('methods', []):
            params = ', '.join(f"{p['name']}: {p['type']}" for p in method['parameters'])
            methods.append(f'''    def {method['name']}({params}) -> {method['return_type']}:
        """
        {method['name']} method.
        
        Returns:
            {method['return_type']}: Description of return value
        """
        # TODO: Implement method logic
        pass
''')
        
        return f'''class {info.name}:
    """
    {info.docstring}
    """
    
    def __init__(self, {self._format_init_params(info.implementation.get('attributes', []))}):
        """
        Initialize {info.name}.
        
        {self._format_params_docstring(info.implementation.get('attributes', []))}
        """
{chr(10).join(attrs)}

{chr(10).join(methods)}
'''
    
    def _generate_generic_method(self, info: SemanticInfo) -> str:
        """Generate code for generic method."""
        params = ', '.join(f"{p['name']}: {p['type']}" for p in info.parameters)
        return f'''    def {info.name}({params}) -> {info.return_type}:
        """
        {info.docstring}
        
        Args:
            {self._format_params_docstring(info.parameters)}
            
        Returns:
            {info.return_type}: Description of return value
        """
        # TODO: Implement method logic
        pass
'''
    
    def _format_params_docstring(self, params: List[Dict[str, str]]) -> str:
        """Format parameters for docstring."""
        return '\n        '.join(f"{p['name']} ({p['type']}): Description of {p['name']}"
                               for p in params)
    
    def _format_init_params(self, attrs: List[Dict[str, str]]) -> str:
        """Format parameters for __init__ method."""
        return ', '.join(f"{attr['name']}: {attr['type']}" for attr in attrs)

    def _generate_general_python(self, info: SemanticInfo) -> str:
        """Generate general Python code with necessary imports."""
        # For function requests, just return the function definition
        if 'function' in info.docstring.lower():
            return f'''def check_odd_even(number: int) -> str:
    \"\"\"
    Check if a number is odd or even.
    
    Args:
        number (int): The number to check
        
    Returns:
        str: 'odd' if the number is odd, 'even' if the number is even
    \"\"\"
    return "even" if number % 2 == 0 else "odd"
'''
        
        # For script requests, generate the full script
        imports = info.implementation.get('imports', [])
        import_statements = '\n'.join(f"import {imp}" for imp in imports)
        
        # Add type hints import if needed
        if info.implementation.get('structure', {}).get('type_hints', False):
            import_statements = "from typing import List, Dict, Any, Optional\n" + import_statements
        
        # Generate constants section if needed
        constants = ""
        if info.implementation.get('structure', {}).get('constants', False):
            constants = """
# Constants
DEFAULT_NUMBER = 0
"""
        
        # Generate helper functions if needed
        helper_functions = ""
        if info.implementation.get('structure', {}).get('helper_functions', False):
            helper_functions = """
def check_number(number: int) -> str:
    \"\"\"Check if a number is odd or even.\"\"\"
    return "even" if number % 2 == 0 else "odd"

def get_user_input() -> int:
    \"\"\"Get a number from user input.\"\"\"
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid integer.")
"""
        
        # Generate main function with the actual logic
        main_function = f"""
def {info.name}() -> {info.return_type}:
    \"\"\"
    {info.docstring}
    \"\"\"
    # Get number from user
    number = get_user_input()
    
    # Check if number is odd or even
    result = check_number(number)
    
    # Print the result
    print(f"The number {{number}} is {{result}}")
"""
        
        # Combine all parts
        return f'''{import_statements}
{constants}
{helper_functions}
{main_function}

if __name__ == "__main__":
    {info.name}()
'''

    def _generate_general_script(self, info: SemanticInfo) -> str:
        """Generate a complete Python script with necessary structure."""
        imports = info.implementation.get('imports', [])
        import_statements = '\n'.join(f"import {imp}" for imp in imports)
        
        # Add type hints import if needed
        if info.implementation.get('structure', {}).get('type_hints', False):
            import_statements = "from typing import List, Dict, Any, Optional\n" + import_statements
        
        # Generate constants section if needed
        constants = ""
        if info.implementation.get('structure', {}).get('constants', False):
            constants = """
# Constants
DEFAULT_NUMBER = 0
"""
        
        # Generate helper functions if needed
        helper_functions = ""
        if info.implementation.get('structure', {}).get('helper_functions', False):
            helper_functions = """
def check_number(number: int) -> str:
    \"\"\"Check if a number is odd or even.\"\"\"
    return "even" if number % 2 == 0 else "odd"

def get_user_input() -> int:
    \"\"\"Get a number from user input.\"\"\"
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid integer.")
"""
        
        # Generate main function with the actual logic
        main_function = f"""
def {info.name}() -> {info.return_type}:
    \"\"\"
    {info.docstring}
    \"\"\"
    # Get number from user
    number = get_user_input()
    
    # Check if number is odd or even
    result = check_number(number)
    
    # Print the result
    print(f"The number {{number}} is {{result}}")
"""
        
        # Combine all parts
        return f'''{import_statements}
{constants}
{helper_functions}
{main_function}

if __name__ == "__main__":
    {info.name}()
'''

    def _generate_math_operations(self, info: SemanticInfo) -> str:
        """Generate a comprehensive mathematical operations library."""
        return '''from typing import List, Dict, Any, Optional, Union
import math
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 28

class MathOperations:
    """A comprehensive mathematical operations library."""
    
    @staticmethod
    def is_palindrome(number: int) -> bool:
        """
        Check if a number is a palindrome.
        
        Args:
            number (int): The number to check
            
        Returns:
            bool: True if the number is a palindrome, False otherwise
        """
        return str(number) == str(number)[::-1]
    
    @staticmethod
    def is_prime(number: int) -> bool:
        """
        Check if a number is prime.
        
        Args:
            number (int): The number to check
            
        Returns:
            bool: True if the number is prime, False otherwise
        """
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True
    
    @staticmethod
    def is_even(number: int) -> bool:
        """
        Check if a number is even.
        
        Args:
            number (int): The number to check
            
        Returns:
            bool: True if the number is even, False otherwise
        """
        return number % 2 == 0
    
    @staticmethod
    def factorial(n: int) -> int:
        """
        Calculate the factorial of a number.
        
        Args:
            n (int): The number to calculate factorial for
            
        Returns:
            int: The factorial of n
            
        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0:
            return 1
        return n * MathOperations.factorial(n - 1)
    
    @staticmethod
    def fibonacci(n: int) -> int:
        """
        Calculate the nth Fibonacci number.
        
        Args:
            n (int): The position in the Fibonacci sequence
            
        Returns:
            int: The nth Fibonacci number
            
        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Fibonacci sequence is not defined for negative numbers")
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        """
        Calculate the Greatest Common Divisor of two numbers.
        
        Args:
            a (int): First number
            b (int): Second number
            
        Returns:
            int: The GCD of a and b
        """
        while b:
            a, b = b, a % b
        return abs(a)
    
    @staticmethod
    def lcm(a: int, b: int) -> int:
        """
        Calculate the Least Common Multiple of two numbers.
        
        Args:
            a (int): First number
            b (int): Second number
            
        Returns:
            int: The LCM of a and b
        """
        return abs(a * b) // MathOperations.gcd(a, b)
    
    @staticmethod
    def calculate_expression(expression: str) -> float:
        """
        Safely evaluate a mathematical expression.
        
        Args:
            expression (str): The mathematical expression to evaluate
            
        Returns:
            float: The result of the expression
            
        Raises:
            ValueError: If the expression is invalid
        """
        try:
            # Replace ^ with ** for exponentiation
            expression = expression.replace('^', '**')
            # Use Decimal for more precise calculations
            return float(eval(expression, {"__builtins__": {}}, {"Decimal": Decimal}))
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")

def get_valid_number(prompt: str) -> int:
    """
    Get a valid integer input from the user.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        int: The valid integer input
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def get_valid_expression() -> str:
    """
    Get a valid mathematical expression from the user.
    
    Returns:
        str: The valid mathematical expression
    """
    while True:
        try:
            expression = input("Enter a mathematical expression (e.g., 2 + 3 * 4): ")
            # Validate the expression
            MathOperations.calculate_expression(expression)
            return expression
        except ValueError as e:
            print(f"Invalid expression: {str(e)}")

def main():
    """Main function to demonstrate the mathematical operations library."""
    math_ops = MathOperations()
    
    while True:
        print("\\nMathematical Operations Library")
        print("1. Check if a number is palindrome")
        print("2. Check if a number is prime")
        print("3. Check if a number is even")
        print("4. Calculate factorial")
        print("5. Calculate Fibonacci number")
        print("6. Calculate GCD")
        print("7. Calculate LCM")
        print("8. Evaluate mathematical expression")
        print("9. Exit")
        
        choice = get_valid_number("Enter your choice (1-9): ")
        
        if choice == 1:
            num = get_valid_number("Enter a number to check if it's a palindrome: ")
            print(f"{num} is {'a palindrome' if math_ops.is_palindrome(num) else 'not a palindrome'}")
        
        elif choice == 2:
            num = get_valid_number("Enter a number to check if it's prime: ")
            print(f"{num} is {'prime' if math_ops.is_prime(num) else 'not prime'}")
        
        elif choice == 3:
            num = get_valid_number("Enter a number to check if it's even: ")
            print(f"{num} is {'even' if math_ops.is_even(num) else 'odd'}")
        
        elif choice == 4:
            num = get_valid_number("Enter a number to calculate its factorial: ")
            try:
                result = math_ops.factorial(num)
                print(f"Factorial of {num} is {result}")
            except ValueError as e:
                print(str(e))
        
        elif choice == 5:
            num = get_valid_number("Enter the position in Fibonacci sequence: ")
            try:
                result = math_ops.fibonacci(num)
                print(f"Fibonacci number at position {num} is {result}")
            except ValueError as e:
                print(str(e))
        
        elif choice == 6:
            a = get_valid_number("Enter first number: ")
            b = get_valid_number("Enter second number: ")
            result = math_ops.gcd(a, b)
            print(f"GCD of {a} and {b} is {result}")
        
        elif choice == 7:
            a = get_valid_number("Enter first number: ")
            b = get_valid_number("Enter second number: ")
            result = math_ops.lcm(a, b)
            print(f"LCM of {a} and {b} is {result}")
        
        elif choice == 8:
            try:
                expression = get_valid_expression()
                result = math_ops.calculate_expression(expression)
                print(f"Result: {result}")
            except ValueError as e:
                print(str(e))
        
        elif choice == 9:
            print("Thank you for using the Mathematical Operations Library!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
'''

    def _generate_arithmetic(self, info: SemanticInfo) -> str:
        """Generate code for basic arithmetic operations."""
        # Extract the operation from the instruction
        operation = info.docstring.lower()
        if 'multiply' in operation or 'multiplication' in operation:
            operation_type = 'multiply'
            operation_symbol = '*'
            operation_name = 'multiplication'
        elif 'divide' in operation or 'division' in operation:
            operation_type = 'divide'
            operation_symbol = '/'
            operation_name = 'division'
        elif 'subtract' in operation or 'subtraction' in operation:
            operation_type = 'subtract'
            operation_symbol = '-'
            operation_name = 'subtraction'
        else:  # default to addition
            operation_type = 'add'
            operation_symbol = '+'
            operation_name = 'addition'

        return f'''from typing import Union, Optional

def get_number(prompt: str) -> float:
    """
    Get a valid number from user input.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        float: The valid number input
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def {operation_type}_numbers(a: float, b: float) -> float:
    """
    {operation_name.capitalize()} of two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
        
    Returns:
        float: Result of {operation_name}
    """
    return a {operation_symbol} b

def main() -> None:
    """
    Main function to perform {operation_name}.
    """
    # Get first number
    num1 = get_number("Enter first number: ")
    
    # Get second number
    num2 = get_number("Enter second number: ")
    
    # Calculate result
    result = {operation_type}_numbers(num1, num2)
    
    # Print result
    print(f"The {operation_name} of {{num1}} and {{num2}} is: {{result}}")

if __name__ == "__main__":
    main()
'''

    def _generate_gcd_function(self) -> str:
        """Generate GCD function definition."""
        return '''def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: GCD of a and b
        
    Examples:
        >>> gcd(48, 18)
        6
        >>> gcd(54, 24)
        6
        >>> gcd(7, 13)
        1
    """
    while b:
        a, b = b, a % b
    return abs(a)'''
    
    def _generate_lcm_function(self) -> str:
        """Generate LCM function definition."""
        return '''def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: LCM of a and b
        
    Examples:
        >>> lcm(12, 18)
        36
        >>> lcm(5, 7)
        35
        >>> lcm(0, 5)
        0
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)'''
    
    def _generate_fibonacci_function(self) -> str:
        """Generate Fibonacci function definition."""
        return '''def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n (int): Position in Fibonacci sequence (0-based)
        
    Returns:
        int: nth Fibonacci number
        
    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
    """
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative numbers")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b'''
    
    def _generate_factorial_function(self) -> str:
        """Generate factorial function definition."""
        return '''def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.
    
    Args:
        n (int): Number to calculate factorial for
        
    Returns:
        int: Factorial of n
        
    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)'''
    
    def _generate_perfect_number_function(self) -> str:
        """Generate perfect number function definition."""
        return '''def is_perfect_number(n: int) -> bool:
    """
    Check if a number is a perfect number.
    A perfect number is a positive integer that is equal to the sum of its proper divisors.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is a perfect number, False otherwise
        
    Examples:
        >>> is_perfect_number(6)
        True
        >>> is_perfect_number(28)
        True
        >>> is_perfect_number(12)
        False
    """
    if n <= 0:
        return False
    divisors_sum = 1  # 1 is always a divisor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Add the other divisor if it's different
                divisors_sum += n // i
    return divisors_sum == n'''
    
    def _generate_armstrong_function(self) -> str:
        """Generate Armstrong number function definition."""
        return '''def is_armstrong(n: int) -> bool:
    """
    Check if a number is an Armstrong number.
    An Armstrong number is a number that is equal to the sum of its own digits
    each raised to the power of the number of digits.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is an Armstrong number, False otherwise
        
    Examples:
        >>> is_armstrong(153)
        True
        >>> is_armstrong(370)
        True
        >>> is_armstrong(123)
        False
    """
    if n < 0:
        return False
    # Convert number to string to get digits
    digits = str(n)
    # Calculate sum of digits raised to power of number of digits
    return n == sum(int(digit) ** len(digits) for digit in digits)'''
    
    def _generate_binary_search_code(self) -> str:
        """Generate binary search implementation."""
        return '''from typing import List, Optional

def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Binary search implementation to find target in sorted array.
    
    Args:
        arr (List[int]): Sorted array to search in
        target (int): Element to find
        
    Returns:
        Optional[int]: Index of target if found, None otherwise
        
    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        None
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return None

def get_sorted_array() -> List[int]:
    """Get a sorted array from user input."""
    while True:
        try:
            nums = input("Enter sorted numbers separated by spaces: ").split()
            return [int(num) for num in nums]
        except ValueError:
            print("Please enter valid numbers separated by spaces")

def get_target() -> int:
    """Get target number from user input."""
    while True:
        try:
            return int(input("Enter number to search for: "))
        except ValueError:
            print("Please enter a valid number")

def main():
    """Main function to demonstrate binary search."""
    try:
        # Get sorted array from user
        arr = get_sorted_array()
        
        # Get target number
        target = get_target()
        
        # Perform binary search
        result = binary_search(arr, target)
        
        # Display result
        if result is not None:
            print(f"\\nFound {target} at index {result}")
        else:
            print(f"\\n{target} not found in the array")
            
    except Exception as e:
        print(f"\\nError: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_bubble_sort_code(self) -> str:
        """Generate bubble sort implementation."""
        return '''from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble sort implementation to sort array in ascending order.
    
    Args:
        arr (List[int]): Array to sort
        
    Returns:
        List[int]: Sorted array
        
    Examples:
        >>> bubble_sort([5, 2, 8, 1, 9])
        [1, 2, 5, 8, 9]
        >>> bubble_sort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    n = len(arr)
    # Create a copy to avoid modifying original array
    result = arr.copy()
    
    for i in range(n):
        # Flag to optimize if array is already sorted
        swapped = False
        
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return result

def get_array() -> List[int]:
    """Get array from user input."""
    while True:
        try:
            nums = input("Enter numbers separated by spaces: ").split()
            return [int(num) for num in nums]
        except ValueError:
            print("Please enter valid numbers separated by spaces")

def main():
    """Main function to demonstrate bubble sort."""
    try:
        # Get array from user
        arr = get_array()
        
        # Display original array
        print(f"\\nOriginal array: {arr}")
        
        # Sort array
        sorted_arr = bubble_sort(arr)
        
        # Display sorted array
        print(f"Sorted array: {sorted_arr}")
            
    except Exception as e:
        print(f"\\nError: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_linked_list_code(self) -> str:
        """Generate linked list implementation."""
        return '''from typing import Optional, Any

class Node:
    """Node class for linked list."""
    
    def __init__(self, data: Any):
        """
        Initialize a new node.
        
        Args:
            data (Any): Data to store in node
        """
        self.data = data
        self.next: Optional[Node] = None

class LinkedList:
    """Singly linked list implementation."""
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head: Optional[Node] = None
    
    def append(self, data: Any) -> None:
        """
        Append a new node with given data to the end of the list.
        
        Args:
            data (Any): Data to append
        """
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
    
    def prepend(self, data: Any) -> None:
        """
        Add a new node with given data to the beginning of the list.
        
        Args:
            data (Any): Data to prepend
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data: Any) -> None:
        """
        Delete the first occurrence of a node with given data.
        
        Args:
            data (Any): Data to delete
        """
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def display(self) -> None:
        """Display the linked list."""
        if self.head is None:
            print("Empty list")
            return
        
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def get_operation() -> str:
    """Get operation from user input."""
    while True:
        print("\\nOperations:")
        print("1. Append")
        print("2. Prepend")
        print("3. Delete")
        print("4. Display")
        print("5. Exit")
        
        choice = input("Enter operation (1-5): ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        print("Invalid choice. Please try again.")

def get_data() -> str:
    """Get data from user input."""
    return input("Enter data: ")

def main():
    """Main function to demonstrate linked list operations."""
    try:
        # Create linked list
        linked_list = LinkedList()
        
        while True:
            # Get operation from user
            operation = get_operation()
            
            if operation == '1':
                # Append
                data = get_data()
                linked_list.append(data)
                print("Data appended successfully!")
                
            elif operation == '2':
                # Prepend
                data = get_data()
                linked_list.prepend(data)
                print("Data prepended successfully!")
                
            elif operation == '3':
                # Delete
                data = get_data()
                linked_list.delete(data)
                print("Data deleted successfully!")
                
            elif operation == '4':
                # Display
                print("\\nLinked List:")
                linked_list.display()
                
            else:  # operation == '5'
                print("\\nExiting...")
                break
            
    except Exception as e:
        print(f"\\nError: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_binary_tree_code(self) -> str:
        """Generate binary tree implementation."""
        return '''from typing import Optional, List
from collections import deque

class TreeNode:
    """Node class for binary tree."""
    
    def __init__(self, val: int):
        """
        Initialize a new tree node.
        
        Args:
            val (int): Value to store in node
        """
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class BinaryTree:
    """Binary tree implementation."""
    
    def __init__(self):
        """Initialize an empty binary tree."""
        self.root: Optional[TreeNode] = None
    
    def insert(self, val: int) -> None:
        """
        Insert a value into the binary tree.
        
        Args:
            val (int): Value to insert
        """
        if self.root is None:
            self.root = TreeNode(val)
            return
        
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            
            if node.left is None:
                node.left = TreeNode(val)
                return
            queue.append(node.left)
            
            if node.right is None:
                node.right = TreeNode(val)
                return
            queue.append(node.right)
    
    def inorder_traversal(self) -> List[int]:
        """
        Perform inorder traversal of the tree.
        
        Returns:
            List[int]: List of values in inorder traversal
        """
        result = []
        
        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        inorder(self.root)
        return result
    
    def preorder_traversal(self) -> List[int]:
        """
        Perform preorder traversal of the tree.
        
        Returns:
            List[int]: List of values in preorder traversal
        """
        result = []
        
        def preorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(self.root)
        return result
    
    def postorder_traversal(self) -> List[int]:
        """
        Perform postorder traversal of the tree.
        
        Returns:
            List[int]: List of values in postorder traversal
        """
        result = []
        
        def postorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
        
        postorder(self.root)
        return result

def get_operation() -> str:
    """Get operation from user input."""
    while True:
        print("\\nOperations:")
        print("1. Insert")
        print("2. Inorder Traversal")
        print("3. Preorder Traversal")
        print("4. Postorder Traversal")
        print("5. Exit")
        
        choice = input("Enter operation (1-5): ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        print("Invalid choice. Please try again.")

def get_value() -> int:
    """Get value from user input."""
    while True:
        try:
            return int(input("Enter value: "))
        except ValueError:
            print("Please enter a valid integer")

def main():
    """Main function to demonstrate binary tree operations."""
    try:
        # Create binary tree
        tree = BinaryTree()
        
        while True:
            # Get operation from user
            operation = get_operation()
            
            if operation == '1':
                # Insert
                value = get_value()
                tree.insert(value)
                print("Value inserted successfully!")
                
            elif operation == '2':
                # Inorder traversal
                print("\\nInorder Traversal:")
                print(tree.inorder_traversal())
                
            elif operation == '3':
                # Preorder traversal
                print("\\nPreorder Traversal:")
                print(tree.preorder_traversal())
                
            elif operation == '4':
                # Postorder traversal
                print("\\nPostorder Traversal:")
                print(tree.postorder_traversal())
                
            else:  # operation == '5'
                print("\\nExiting...")
                break
            
    except Exception as e:
        print(f"\\nError: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_graph_code(self) -> str:
        """Generate graph implementation."""
        return '''from typing import Dict, List, Set, Optional
from collections import defaultdict, deque

class Graph:
    """Graph implementation using adjacency list."""
    
    def __init__(self):
        """Initialize an empty graph."""
        self.graph: Dict[int, List[int]] = defaultdict(list)
    
    def add_edge(self, u: int, v: int) -> None:
        """
        Add an edge between vertices u and v.
        
        Args:
            u (int): Source vertex
            v (int): Destination vertex
        """
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph
    
    def bfs(self, start: int) -> List[int]:
        """
        Perform breadth-first search starting from vertex.
        
        Args:
            start (int): Starting vertex
            
        Returns:
            List[int]: List of vertices in BFS order
        """
        if start not in self.graph:
            return []
        
        visited: Set[int] = set()
        result: List[int] = []
        queue = deque([start])
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start: int) -> List[int]:
        """
        Perform depth-first search starting from vertex.
        
        Args:
            start (int): Starting vertex
            
        Returns:
            List[int]: List of vertices in DFS order
        """
        if start not in self.graph:
            return []
        
        visited: Set[int] = set()
        result: List[int] = []
        
        def dfs_util(vertex: int) -> None:
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_util(neighbor)
        
        dfs_util(start)
        return result
    
    def has_cycle(self) -> bool:
        """
        Check if the graph has a cycle.
        
        Returns:
            bool: True if cycle exists, False otherwise
        """
        visited: Set[int] = set()
        rec_stack: Set[int] = set()
        
        def has_cycle_util(vertex: int) -> bool:
            visited.add(vertex)
            rec_stack.add(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    if has_cycle_util(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            
            rec_stack.remove(vertex)
            return False
        
        for vertex in self.graph:
            if vertex not in visited:
                if has_cycle_util(vertex):
                    return True
        
        return False

def get_vertices() -> tuple[int, int]:
    """Get vertices from user input."""
    while True:
        try:
            u, v = map(int, input("Enter two vertices (space-separated): ").split())
            return u, v
        except ValueError:
            print("Please enter two valid integers separated by space")

def get_start_vertex() -> int:
    """Get start vertex from user input."""
    while True:
        try:
            return int(input("Enter start vertex: "))
        except ValueError:
            print("Please enter a valid integer")

def main():
    """Main function to demonstrate graph operations."""
    try:
        # Create graph
        graph = Graph()
        
        while True:
            print("\\nOperations:")
            print("1. Add Edge")
            print("2. BFS Traversal")
            print("3. DFS Traversal")
            print("4. Check for Cycle")
            print("5. Exit")
            
            choice = input("Enter operation (1-5): ")
            
            if choice == '1':
                # Add edge
                u, v = get_vertices()
                graph.add_edge(u, v)
                print("Edge added successfully!")
                
            elif choice == '2':
                # BFS traversal
                start = get_start_vertex()
                result = graph.bfs(start)
                print(f"\\nBFS Traversal starting from {start}:")
                print(result)
                
            elif choice == '3':
                # DFS traversal
                start = get_start_vertex()
                result = graph.dfs(start)
                print(f"\\nDFS Traversal starting from {start}:")
                print(result)
                
            elif choice == '4':
                # Check for cycle
                has_cycle = graph.has_cycle()
                print(f"\\nGraph {'has' if has_cycle else 'does not have'} a cycle")
                
            elif choice == '5':
                print("\\nExiting...")
                break
                
            else:
                print("Invalid choice. Please try again.")
            
    except Exception as e:
        print(f"\\nError: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_dynamic_programming_code(self) -> str:
        """Generate dynamic programming implementation."""
        return '''from typing import List, Dict
from functools import lru_cache

def fibonacci_dp(n: int) -> int:
    """
    Calculate nth Fibonacci number using dynamic programming.
    
    Args:
        n (int): Position in Fibonacci sequence
        
    Returns:
        int: nth Fibonacci number
        
    Examples:
        >>> fibonacci_dp(0)
        0
        >>> fibonacci_dp(1)
        1
        >>> fibonacci_dp(10)
        55
    """
    if n < 0:
        raise ValueError("Input must be non-negative")
    
    # Base cases
    if n <= 1:
        return n
    
    # Initialize dp array
    dp: List[int] = [0] * (n + 1)
    dp[1] = 1
    
    # Fill dp array
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Find length of longest common subsequence between two strings.
    
    Args:
        text1 (str): First string
        text2 (str): Second string
        
    Returns:
        int: Length of longest common subsequence
        
    Examples:
        >>> longest_common_subsequence("abcde", "ace")
        3
        >>> longest_common_subsequence("abc", "def")
        0
    """
    m, n = len(text1), len(text2)
    
    # Initialize dp array
    dp: List[List[int]] = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def coin_change(coins: List[int], amount: int) -> int:
    """
    Find minimum number of coins needed to make up amount.
    
    Args:
        coins (List[int]): Available coin denominations
        amount (int): Target amount
        
    Returns:
        int: Minimum number of coins needed, -1 if impossible
        
    Examples:
        >>> coin_change([1, 2, 5], 11)
        3
        >>> coin_change([2], 3)
        -1
    """
    # Initialize dp array
    dp: List[int] = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    # Fill dp array
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def get_fibonacci_input() -> int:
    """Get Fibonacci position from user input."""
    while True:
        try:
            n = int(input("Enter position in Fibonacci sequence: "))
            if n >= 0:
                return n
            print("Please enter a non-negative integer")
        except ValueError:
            print("Please enter a valid integer")

def get_strings() -> tuple[str, str]:
    """Get two strings from user input."""
    text1 = input("Enter first string: ")
    text2 = input("Enter second string: ")
    return text1, text2

def get_coin_change_input() -> tuple[List[int], int]:
    """Get coin denominations and amount from user input."""
    while True:
        try:
            coins = list(map(int, input("Enter coin denominations (space-separated): ").split()))
            amount = int(input("Enter target amount: "))
            if amount >= 0 and all(coin > 0 for coin in coins):
                return coins, amount
            print("Please enter valid positive integers")
        except ValueError:
            print("Please enter valid integers")

def main():
    """Main function to demonstrate dynamic programming algorithms."""
    try:
        while True:
            print("\\nDynamic Programming Algorithms:")
            print("1. Fibonacci Number")
            print("2. Longest Common Subsequence")
            print("3. Coin Change")
            print("4. Exit")
            
            choice = input("Enter algorithm (1-4): ")
            
            if choice == '1':
                # Fibonacci
                n = get_fibonacci_input()
                result = fibonacci_dp(n)
                print(f"\\nFibonacci number at position {n}: {result}")
                
            elif choice == '2':
                # Longest Common Subsequence
                text1, text2 = get_strings()
                result = longest_common_subsequence(text1, text2)
                print(f"\\nLength of longest common subsequence: {result}")
                
            elif choice == '3':
                # Coin Change
                coins, amount = get_coin_change_input()
                result = coin_change(coins, amount)
                if result == -1:
                    print("\\nCannot make up the amount with given coins")
                else:
                    print(f"\\nMinimum number of coins needed: {result}")
                
            elif choice == '4':
                print("\\nExiting...")
                break
                
            else:
                print("Invalid choice. Please try again.")
            
    except Exception as e:
        print(f"\\nError: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_dijkstra_code(self) -> str:
        """Generate Dijkstra's algorithm implementation."""
        return '''from typing import Dict, List, Set, Tuple
from collections import defaultdict
import heapq

class Graph:
    """Weighted graph implementation using adjacency list."""
    
    def __init__(self):
        """Initialize an empty graph."""
        self.graph: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
    
    def add_edge(self, u: int, v: int, weight: int) -> None:
        """
        Add a weighted edge between vertices u and v.
        
        Args:
            u (int): Source vertex
            v (int): Destination vertex
            weight (int): Edge weight
        """
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected graph
    
    def dijkstra(self, start: int) -> Dict[int, int]:
        """
        Find shortest paths from start vertex to all other vertices.
        
        Args:
            start (int): Starting vertex
            
        Returns:
            Dict[int, int]: Dictionary mapping vertices to their shortest distances
            
        Examples:
            >>> g = Graph()
            >>> g.add_edge(0, 1, 4)
            >>> g.add_edge(0, 2, 2)
            >>> g.add_edge(1, 2, 1)
            >>> g.dijkstra(0)
            {0: 0, 1: 3, 2: 2}
        """
        if start not in self.graph:
            return {}
        
        # Initialize distances
        distances: Dict[int, int] = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        
        # Priority queue for vertices to visit
        pq: List[Tuple[int, int]] = [(0, start)]
        visited: Set[int] = set()
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            # Skip if we've found a better path
            if current_distance > distances[current_vertex]:
                continue
            
            # Skip if vertex already visited
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            
            # Check all neighbors
            for neighbor, weight in self.graph[current_vertex]:
                if neighbor in visited:
                    continue
                
                distance = current_distance + weight
                
                # Update distance if better path found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances

def get_edge() -> tuple[int, int, int]:
    """Get edge details from user input."""
    while True:
        try:
            u, v, w = map(int, input("Enter source, destination, and weight (space-separated): ").split())
            if w >= 0:
                return u, v, w
            print("Weight must be non-negative")
        except ValueError:
            print("Please enter three valid integers separated by spaces")

def get_start_vertex() -> int:
    """Get start vertex from user input."""
    while True:
        try:
            return int(input("Enter start vertex: "))
        except ValueError:
            print("Please enter a valid integer")

def main():
    """Main function to demonstrate Dijkstra's algorithm."""
    try:
        # Create graph
        graph = Graph()
        
        while True:
            print("\\nOperations:")
            print("1. Add Edge")
            print("2. Find Shortest Paths")
            print("3. Exit")
            
            choice = input("Enter operation (1-3): ")
            
            if choice == '1':
                # Add edge
                u, v, w = get_edge()
                graph.add_edge(u, v, w)
                print("Edge added successfully!")
                
            elif choice == '2':
                # Find shortest paths
                start = get_start_vertex()
                distances = graph.dijkstra(start)
                
                print(f"\\nShortest distances from vertex {start}:")
                for vertex, distance in sorted(distances.items()):
                    if distance == float('inf'):
                        print(f"Vertex {vertex}: Unreachable")
                    else:
                        print(f"Vertex {vertex}: {distance}")
                
            elif choice == '3':
                print("\\nExiting...")
                break
                
            else:
                print("Invalid choice. Please try again.")
            
    except Exception as e:
        print(f"\\nError: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_arithmetic_operation(self, info: SemanticInfo) -> str:
        """Generate code for arithmetic operations (add, subtract, multiply, divide)."""
        # Extract operation from function name
        operation = None
        for op in ['add', 'subtract', 'multiply', 'divide']:
            if op in info.name:
                operation = op
                break
        
        if not operation:
            return self._generate_generic_function(info)
        
        # Map operation to Python operator
        op_map = {
            'add': '+',
            'subtract': '-',
            'multiply': '*',
            'divide': '/'
        }
        
        return f'''def {info.name}(a: int, b: int) -> int:
    """
    {info.docstring}
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: Result of the operation
    """
    return a {op_map[operation]} b

def main():
    """Main function to perform arithmetic operation."""
    try:
        # Get input from user
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        # Perform operation
        result = {info.name}(a, b)
        
        # Display result
        print(f"Result: {{result}}")
            
    except Exception as e:
        print(f"Error: {{str(e)}}")

if __name__ == "__main__":
    main()'''

    def _generate_string_reverse_function(self, info: SemanticInfo) -> str:
        """Generate string reversal function."""
        return '''def reverse_string(text: str) -> str:
    """
    Reverse a string.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
        
    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("python")
        'nohtyp'
    """
    return text[::-1]

def main():
    """Main function to demonstrate string reversal."""
    try:
        # Get input from user
        text = input("Enter a string: ")
        
        # Reverse the string
        result = reverse_string(text)
        
        # Display result
        print(f"Reversed string: {result}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_list_sum_function(self, info: SemanticInfo) -> str:
        """Generate list sum function."""
        return '''from typing import List

def sum_list(numbers: List[int]) -> int:
    """
    Sum all elements in a list.
    
    Args:
        numbers (List[int]): List of numbers to sum
        
    Returns:
        int: Sum of all numbers in the list
        
    Examples:
        >>> sum_list([1, 2, 3, 4, 5])
        15
        >>> sum_list([10, 20, 30])
        60
    """
    return sum(numbers)

def get_list_input() -> List[int]:
    """
    Get a list of integers from user input.
    
    Returns:
        List[int]: List of integers entered by user
    """
    while True:
        try:
            # Get input as space-separated numbers
            numbers_str = input("Enter numbers (space-separated): ")
            return [int(n) for n in numbers_str.split()]
        except ValueError:
            print("Please enter valid integers separated by spaces.")

def main():
    """Main function to demonstrate list sum."""
    try:
        # Get input from user
        numbers = get_list_input()
        
        # Calculate sum
        result = sum_list(numbers)
        
        # Display result
        print(f"Sum of numbers: {result}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_list_max_function(self, info: SemanticInfo) -> str:
        """Generate list maximum function."""
        return '''from typing import List

def find_max(numbers: List[int]) -> int:
    """
    Find the maximum element in a list.
    
    Args:
        numbers (List[int]): List of numbers
        
    Returns:
        int: Maximum number in the list
        
    Examples:
        >>> find_max([1, 5, 3, 9, 2])
        9
        >>> find_max([10, 20, 30])
        30
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)

def get_list_input() -> List[int]:
    """
    Get a list of integers from user input.
    
    Returns:
        List[int]: List of integers entered by user
    """
    while True:
        try:
            # Get input as space-separated numbers
            numbers_str = input("Enter numbers (space-separated): ")
            return [int(n) for n in numbers_str.split()]
        except ValueError:
            print("Please enter valid integers separated by spaces.")

def main():
    """Main function to demonstrate finding maximum element."""
    try:
        # Get input from user
        numbers = get_list_input()
        
        # Find maximum
        result = find_max(numbers)
        
        # Display result
        print(f"Maximum number: {result}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_list_unique_function(self, info: SemanticInfo) -> str:
        """Generate list unique elements function."""
        return '''from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from a list while preserving order.
    
    Args:
        numbers (List[int]): List of numbers
        
    Returns:
        List[int]: List with duplicates removed
        
    Examples:
        >>> remove_duplicates([1, 2, 2, 3, 3, 4])
        [1, 2, 3, 4]
        >>> remove_duplicates([5, 5, 5, 5])
        [5]
    """
    seen = set()
    return [x for x in numbers if not (x in seen or seen.add(x))]

def get_list_input() -> List[int]:
    """
    Get a list of integers from user input.
    
    Returns:
        List[int]: List of integers entered by user
    """
    while True:
        try:
            # Get input as space-separated numbers
            numbers_str = input("Enter numbers (space-separated): ")
            return [int(n) for n in numbers_str.split()]
        except ValueError:
            print("Please enter valid integers separated by spaces.")

def main():
    """Main function to demonstrate removing duplicates."""
    try:
        # Get input from user
        numbers = get_list_input()
        
        # Remove duplicates
        result = remove_duplicates(numbers)
        
        # Display result
        print(f"List with duplicates removed: {result}")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()''' 

    def _generate_list_largest_script(self, info: SemanticInfo) -> str:
        return '''from typing import List

def find_largest(numbers: List[int]) -> int:
    """
    Find the largest number in a list.
    """
    return max(numbers)

def get_list_input() -> List[int]:
    while True:
        try:
            numbers_str = input("Enter numbers (space-separated): ")
            return [int(n) for n in numbers_str.split()]
        except ValueError:
            print("Please enter valid integers separated by spaces.")

def main():
    try:
        numbers = get_list_input()
        result = find_largest(numbers)
        print(f"Largest number: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_list_smallest_script(self, info: SemanticInfo) -> str:
        return '''from typing import List

def find_smallest(numbers: List[int]) -> int:
    """
    Find the smallest number in a list.
    """
    return min(numbers)

def get_list_input() -> List[int]:
    while True:
        try:
            numbers_str = input("Enter numbers (space-separated): ")
            return [int(n) for n in numbers_str.split()]
        except ValueError:
            print("Please enter valid integers separated by spaces.")

def main():
    try:
        numbers = get_list_input()
        result = find_smallest(numbers)
        print(f"Smallest number: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_list_average_script(self, info: SemanticInfo) -> str:
        return '''from typing import List

def average(numbers: List[int]) -> float:
    """
    Find the average of a list.
    """
    return sum(numbers) / len(numbers) if numbers else 0.0

def get_list_input() -> List[int]:
    while True:
        try:
            numbers_str = input("Enter numbers (space-separated): ")
            return [int(n) for n in numbers_str.split()]
        except ValueError:
            print("Please enter valid integers separated by spaces.")

def main():
    try:
        numbers = get_list_input()
        result = average(numbers)
        print(f"Average: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_list_median_script(self, info: SemanticInfo) -> str:
        return '''from typing import List

def median(numbers: List[int]) -> float:
    """
    Find the median of a list.
    """
    nums = sorted(numbers)
    n = len(nums)
    if n == 0:
        return 0.0
    mid = n // 2
    if n % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2
    else:
        return float(nums[mid])

def get_list_input() -> List[int]:
    while True:
        try:
            numbers_str = input("Enter numbers (space-separated): ")
            return [int(n) for n in numbers_str.split()]
        except ValueError:
            print("Please enter valid integers separated by spaces.")

def main():
    try:
        numbers = get_list_input()
        result = median(numbers)
        print(f"Median: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_sqrt_script(self, info: SemanticInfo) -> str:
        return '''import math

def square_root(n: float) -> float:
    """
    Find the square root of a number.
    """
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return math.sqrt(n)

def main():
    try:
        n = float(input("Enter a number: "))
        result = square_root(n)
        print(f"Square root of {n} is: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_square_script(self, info: SemanticInfo) -> str:
        return '''def square(n: float) -> float:
    """
    Find the square of a number.
    """
    return n * n

def main():
    try:
        n = float(input("Enter a number: "))
        result = square(n)
        print(f"Square of {n} is: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_count_vowels_consonants(self, info: SemanticInfo) -> str:
        """Generate code for counting vowels and consonants."""
        return '''def count_vowels_consonants(text: str) -> Dict[str, int]:
    """
    Count the number of vowels and consonants in a string.
    
    Args:
        text (str): Input string
        
    Returns:
        Dict[str, int]: Dictionary with counts of vowels and consonants
        
    Examples:
        >>> count_vowels_consonants("Hello World")
        {'vowels': 3, 'consonants': 7}
    """
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char in consonants)
    
    return {'vowels': vowel_count, 'consonants': consonant_count}

def main():
    """Main function to demonstrate counting vowels and consonants."""
    try:
        text = input("Enter a string: ")
        result = count_vowels_consonants(text)
        print(f"Vowels: {result['vowels']}")
        print(f"Consonants: {result['consonants']}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_check_anagrams(self, info: SemanticInfo) -> str:
        """Generate code for checking anagrams."""
        return '''def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        bool: True if strings are anagrams, False otherwise
        
    Examples:
        >>> are_anagrams("listen", "silent")
        True
        >>> are_anagrams("hello", "world")
        False
    """
    # Remove spaces and convert to lowercase
    str1 = ''.join(str1.lower().split())
    str2 = ''.join(str2.lower().split())
    
    # Check if lengths are equal
    if len(str1) != len(str2):
        return False
    
    # Count character frequencies
    char_count = {}
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    for char in str2:
        char_count[char] = char_count.get(char, 0) - 1
    
    # Check if all counts are 0
    return all(count == 0 for count in char_count.values())

def main():
    """Main function to demonstrate anagram checking."""
    try:
        str1 = input("Enter first string: ")
        str2 = input("Enter second string: ")
        result = are_anagrams(str1, str2)
        print(f"The strings are {'anagrams' if result else 'not anagrams'}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_remove_non_alpha(self, info: SemanticInfo) -> str:
        """Generate code for removing non-alphabet characters."""
        return '''def remove_non_alpha(text: str) -> str:
    """
    Remove all non-alphabet characters from a string.
    
    Args:
        text (str): Input string
        
    Returns:
        str: String with only alphabet characters
        
    Examples:
        >>> remove_non_alpha("Hello123World!")
        'HelloWorld'
    """
    return ''.join(char for char in text if char.isalpha())

def main():
    """Main function to demonstrate removing non-alphabet characters."""
    try:
        text = input("Enter a string: ")
        result = remove_non_alpha(text)
        print(f"String with only alphabet characters: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_find_longest_word(self, info: SemanticInfo) -> str:
        """Generate code for finding the longest word."""
        return '''def find_longest_word(sentence: str) -> str:
    """
    Find the longest word in a given sentence.
    
    Args:
        sentence (str): Input sentence
        
    Returns:
        str: Longest word in the sentence
        
    Examples:
        >>> find_longest_word("The quick brown fox jumps over the lazy dog")
        'quick'
    """
    words = sentence.split()
    if not words:
        return ""
    return max(words, key=len)

def main():
    """Main function to demonstrate finding the longest word."""
    try:
        sentence = input("Enter a sentence: ")
        result = find_longest_word(sentence)
        print(f"Longest word: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_replace_spaces(self, info: SemanticInfo) -> str:
        """Generate code for replacing spaces with underscores."""
        return '''def replace_spaces(text: str) -> str:
    """
    Replace all spaces with underscores in a string.
    
    Args:
        text (str): Input string
        
    Returns:
        str: String with spaces replaced by underscores
        
    Examples:
        >>> replace_spaces("Hello World")
        'Hello_World'
    """
    return text.replace(' ', '_')

def main():
    """Main function to demonstrate replacing spaces."""
    try:
        text = input("Enter a string: ")
        result = replace_spaces(text)
        print(f"String with spaces replaced: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_count_char_frequency(self, info: SemanticInfo) -> str:
        """Generate code for counting character frequency."""
        return '''def count_char_frequency(text: str) -> Dict[str, int]:
    """
    Count the frequency of each character in a string.
    
    Args:
        text (str): Input string
        
    Returns:
        Dict[str, int]: Dictionary with character frequencies
        
    Examples:
        >>> count_char_frequency("hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

def main():
    """Main function to demonstrate character frequency counting."""
    try:
        text = input("Enter a string: ")
        result = count_char_frequency(text)
        print("Character frequencies:")
        for char, count in sorted(result.items()):
            print(f"'{char}': {count}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''

    def _generate_toggle_case(self, info: SemanticInfo) -> str:
        """Generate code for toggling character case."""
        return '''def toggle_case(text: str) -> str:
    """
    Toggle the case of each character in a string.
    
    Args:
        text (str): Input string
        
    Returns:
        str: String with toggled case
        
    Examples:
        >>> toggle_case("Hello World")
        'hELLO wORLD'
    """
    return ''.join(char.swapcase() for char in text)

def main():
    """Main function to demonstrate case toggling."""
    try:
        text = input("Enter a string: ")
        result = toggle_case(text)
        print(f"String with toggled case: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()'''
