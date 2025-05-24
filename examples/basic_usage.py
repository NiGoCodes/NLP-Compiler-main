"""
Example script demonstrating the usage of the NLP compiler.
"""

from nlp_compiler import NLCompiler

def main():
    # Initialize the compiler
    compiler = NLCompiler()
    
    # Example 1: Generate a prime number check function
    instruction1 = "Write a function to check if a number is prime"
    print("Example 1: Prime Number Check")
    print("Input:", instruction1)
    print("Generated Code:")
    print(compiler.compile(instruction1))
    print("\n" + "="*80 + "\n")
    
    # Example 2: Generate a function to filter even numbers
    instruction2 = "Build a function that returns a list of even numbers from a given list"
    print("Example 2: Even Numbers Filter")
    print("Input:", instruction2)
    print("Generated Code:")
    print(compiler.compile(instruction2))
    print("\n" + "="*80 + "\n")
    
    # Example 3: Generate an Employee class
    instruction3 = "Create a class Employee with attributes name and salary, and a method to display details"
    print("Example 3: Employee Class")
    print("Input:", instruction3)
    print("Generated Code:")
    print(compiler.compile(instruction3))
    print("\n" + "="*80 + "\n")
    
    # Example 4: Generate a generic function (not in predefined patterns)
    instruction4 = "Write a function to calculate the factorial of a number"
    print("Example 4: Generic Function")
    print("Input:", instruction4)
    print("Generated Code:")
    print(compiler.compile(instruction4))
    print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    main() 