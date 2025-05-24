"""
Semantic analyzer component that interprets the meaning of instructions.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from ..parser.parser import ParseNode, NodeType

@dataclass
class SemanticInfo:
    """Semantic information extracted from parse tree."""
    type: str  # Type of code to generate (function, class, method)
    name: str  # Name of the function/class/method
    parameters: List[Dict[str, str]]  # Parameters with types
    return_type: str  # Return type
    implementation: Dict[str, Any]  # Implementation details
    docstring: str  # Documentation string

class SemanticAnalyzer:
    """Analyzes semantic meaning of parsed instructions."""
    
    def __init__(self):
        """Initialize the semantic analyzer with common patterns."""
        self.context = {}  # Additional context for analysis
        self.implementation_patterns = {
            'odd_even': {
                'type': 'function',
                'name': 'check_odd_even',
                'parameters': [{'name': 'number', 'type': 'int'}],
                'return_type': 'str',
                'implementation': {
                    'algorithm': 'odd_even_check',
                    'complexity': 'O(1)'
                },
                'keywords': ['odd', 'even', 'check if number is odd', 'check if number is even']
            },
            'prime': {
                'type': 'function',
                'name': 'is_prime',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'bool',
                'implementation': {
                    'algorithm': 'prime_check',
                    'complexity': 'O(sqrt(n))'
                },
                'keywords': ['prime', 'primality']
            },
            'fibonacci': {
                'type': 'function',
                'name': 'is_fibonacci',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'bool',
                'implementation': {
                    'algorithm': 'fibonacci',
                    'complexity': 'O(1)'
                },
                'keywords': ['fibonacci', 'fib']
            },
            'armstrong': {
                'type': 'function',
                'name': 'is_armstrong',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'bool',
                'implementation': {
                    'algorithm': 'armstrong',
                    'complexity': 'O(d)'  # d is number of digits
                },
                'keywords': ['armstrong', 'narcissistic']
            },
            'palindrome': {
                'type': 'function',
                'name': 'is_palindrome',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'bool',
                'implementation': {
                    'algorithm': 'palindrome',
                    'complexity': 'O(d)'  # d is number of digits
                },
                'keywords': ['palindrome', 'palindromic']
            },
            'perfect': {
                'type': 'function',
                'name': 'is_perfect_number',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'bool',
                'implementation': {
                    'algorithm': 'perfect',
                    'complexity': 'O(sqrt(n))'
                },
                'keywords': ['perfect number', 'perfect']
            },
            'binary_search': {
                'type': 'function',
                'name': 'binary_search',
                'parameters': [
                    {'name': 'arr', 'type': 'List[int]'},
                    {'name': 'target', 'type': 'int'}
                ],
                'return_type': 'int',
                'implementation': {
                    'algorithm': 'binary_search',
                    'complexity': 'O(log n)'
                },
                'keywords': ['binary search', 'binary', 'search']
            },
            'bubble_sort': {
                'type': 'function',
                'name': 'bubble_sort',
                'parameters': [{'name': 'arr', 'type': 'List[int]'}],
                'return_type': 'List[int]',
                'implementation': {
                    'algorithm': 'bubble_sort',
                    'complexity': 'O(n^2)'
                },
                'keywords': ['bubble sort', 'sort']
            },
            'linked_list': {
                'type': 'class',
                'name': 'LinkedList',
                'parameters': [],
                'return_type': 'None',
                'implementation': {
                    'algorithm': 'linked_list',
                    'complexity': 'O(1) for insert/delete at head'
                },
                'keywords': ['linked list', 'linkedlist']
            },
            'binary_tree': {
                'type': 'class',
                'name': 'BinaryTree',
                'parameters': [],
                'return_type': 'None',
                'implementation': {
                    'algorithm': 'binary_tree',
                    'complexity': 'O(log n) for balanced tree'
                },
                'keywords': ['binary tree', 'tree']
            },
            'graph': {
                'type': 'class',
                'name': 'Graph',
                'parameters': [],
                'return_type': 'None',
                'implementation': {
                    'algorithm': 'graph',
                    'complexity': 'O(V + E) for traversal'
                },
                'keywords': ['graph', 'adjacency list', 'adjacency matrix']
            },
            'dijkstra': {
                'type': 'function',
                'name': 'dijkstra',
                'parameters': [
                    {'name': 'graph', 'type': 'Dict[int, List[Tuple[int, int]]]'},
                    {'name': 'start', 'type': 'int'}
                ],
                'return_type': 'Dict[int, int]',
                'implementation': {
                    'algorithm': 'dijkstra',
                    'complexity': 'O((V + E)log V)'
                },
                'keywords': ['dijkstra', 'shortest path', 'dijkstra algorithm']
            },
            'factorial': {
                'type': 'function',
                'name': 'factorial',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'int',
                'implementation': {
                    'algorithm': 'factorial',
                    'complexity': 'O(n)'
                },
                'keywords': ['factorial', 'calculate factorial']
            },
            'string_reverse': {
                'type': 'function',
                'name': 'reverse_string',
                'parameters': [{'name': 'text', 'type': 'str'}],
                'return_type': 'str',
                'implementation': {
                    'algorithm': 'string_reverse',
                    'complexity': 'O(n)'
                },
                'keywords': ['reverse string', 'reverse a string']
            },
            'list_sum': {
                'type': 'function',
                'name': 'sum_list',
                'parameters': [{'name': 'numbers', 'type': 'List[int]'}],
                'return_type': 'int',
                'implementation': {
                    'algorithm': 'list_sum',
                    'complexity': 'O(n)'
                },
                'keywords': ['sum list', 'sum elements', 'sum all elements']
            },
            'list_max': {
                'type': 'function',
                'name': 'find_max',
                'parameters': [{'name': 'numbers', 'type': 'List[int]'}],
                'return_type': 'int',
                'implementation': {
                    'algorithm': 'list_max',
                    'complexity': 'O(n)'
                },
                'keywords': ['find maximum', 'find max', 'maximum element']
            },
            'list_unique': {
                'type': 'function',
                'name': 'remove_duplicates',
                'parameters': [{'name': 'numbers', 'type': 'List[int]'}],
                'return_type': 'List[int]',
                'implementation': {
                    'algorithm': 'list_unique',
                    'complexity': 'O(n)'
                },
                'keywords': ['remove duplicates', 'unique elements']
            },
            'gcd': {
                'type': 'function',
                'name': 'gcd',
                'parameters': [
                    {'name': 'a', 'type': 'int'},
                    {'name': 'b', 'type': 'int'}
                ],
                'return_type': 'int',
                'implementation': {
                    'algorithm': 'gcd',
                    'complexity': 'O(log(min(a,b)))'
                },
                'keywords': ['greatest common divisor', 'gcd', 'highest common factor']
            },
            'list_largest': {
                'type': 'function',
                'name': 'find_largest',
                'parameters': [{'name': 'numbers', 'type': 'List[int]'}],
                'return_type': 'int',
                'implementation': {
                    'algorithm': 'list_largest',
                    'complexity': 'O(n)'
                },
                'keywords': ['largest number', 'find largest', 'maximum in list', 'largest in list']
            },
            'list_smallest': {
                'type': 'function',
                'name': 'find_smallest',
                'parameters': [{'name': 'numbers', 'type': 'List[int]'}],
                'return_type': 'int',
                'implementation': {
                    'algorithm': 'list_smallest',
                    'complexity': 'O(n)'
                },
                'keywords': ['smallest number', 'find smallest', 'minimum in list', 'smallest in list']
            },
            'list_average': {
                'type': 'function',
                'name': 'average',
                'parameters': [{'name': 'numbers', 'type': 'List[int]'}],
                'return_type': 'float',
                'implementation': {
                    'algorithm': 'list_average',
                    'complexity': 'O(n)'
                },
                'keywords': ['average', 'mean', 'average of a list', 'find average']
            },
            'list_median': {
                'type': 'function',
                'name': 'median',
                'parameters': [{'name': 'numbers', 'type': 'List[int]'}],
                'return_type': 'float',
                'implementation': {
                    'algorithm': 'list_median',
                    'complexity': 'O(n log n)'
                },
                'keywords': ['median', 'find median', 'median of a list']
            },
            'sqrt': {
                'type': 'function',
                'name': 'square_root',
                'parameters': [{'name': 'n', 'type': 'float'}],
                'return_type': 'float',
                'implementation': {
                    'algorithm': 'sqrt',
                    'complexity': 'O(1)'
                },
                'keywords': ['square root', 'sqrt', 'find square root']
            },
            'square': {
                'type': 'function',
                'name': 'square',
                'parameters': [{'name': 'n', 'type': 'float'}],
                'return_type': 'float',
                'implementation': {
                    'algorithm': 'square',
                    'complexity': 'O(1)'
                },
                'keywords': ['square', 'find square', 'square of a number']
            },
            'count_vowels_consonants': {
                'type': 'function',
                'name': 'count_vowels_consonants',
                'parameters': [{'name': 'text', 'type': 'str'}],
                'return_type': 'Dict[str, int]',
                'implementation': {
                    'algorithm': 'string_count',
                    'complexity': 'O(n)',
                    'template': '''from typing import Dict

def count_vowels_consonants(text: str) -> Dict[str, int]:
    """
    Count the number of vowels and consonants in a string.
    
    Args:
        text (str): Input string
        
    Returns:
        Dict[str, int]: Dictionary containing count of vowels and consonants
    """
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char in consonants)
    
    return {'vowels': vowel_count, 'consonants': consonant_count}

def main():
    try:
        text = input("Enter a string: ")
        result = count_vowels_consonants(text)
        print(f"Vowels: {result['vowels']}")
        print(f"Consonants: {result['consonants']}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['count vowels', 'count consonants', 'vowels and consonants']
            },
            'check_anagrams': {
                'type': 'function',
                'name': 'are_anagrams',
                'parameters': [
                    {'name': 'str1', 'type': 'str'},
                    {'name': 'str2', 'type': 'str'}
                ],
                'return_type': 'bool',
                'implementation': {
                    'algorithm': 'anagram_check',
                    'complexity': 'O(n)',
                    'template': '''from typing import Dict

def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        bool: True if strings are anagrams, False otherwise
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
    
    # Compare with second string
    for char in str2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    return True

def main():
    try:
        str1 = input("Enter first string: ")
        str2 = input("Enter second string: ")
        result = are_anagrams(str1, str2)
        print(f"Are anagrams: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['anagram', 'check anagrams', 'are anagrams']
            },
            'remove_non_alpha': {
                'type': 'function',
                'name': 'remove_non_alpha',
                'parameters': [{'name': 'text', 'type': 'str'}],
                'return_type': 'str',
                'implementation': {
                    'algorithm': 'string_clean',
                    'complexity': 'O(n)',
                    'template': '''
def remove_non_alpha(text: str) -> str:
    """
    Remove all non-alphabet characters from a string.
    
    Args:
        text (str): Input string
        
    Returns:
        str: String containing only alphabetic characters
    """
    return ''.join(char for char in text if char.isalpha())

def main():
    try:
        text = input("Enter a string: ")
        result = remove_non_alpha(text)
        print(f"String with only alphabets: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['remove non alphabet', 'remove non alpha', 'only alphabet']
            },
            'find_longest_word': {
                'type': 'function',
                'name': 'find_longest_word',
                'parameters': [{'name': 'sentence', 'type': 'str'}],
                'return_type': 'str',
                'implementation': {
                    'algorithm': 'string_max',
                    'complexity': 'O(n)',
                    'template': '''
def find_longest_word(sentence: str) -> str:
    """
    Find the longest word in a given sentence.
    
    Args:
        sentence (str): Input sentence
        
    Returns:
        str: Longest word in the sentence
    """
    words = sentence.split()
    if not words:
        return ""
    return max(words, key=len)

def main():
    try:
        sentence = input("Enter a sentence: ")
        result = find_longest_word(sentence)
        print(f"Longest word: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['longest word', 'find longest', 'maximum length word']
            },
            'replace_spaces': {
                'type': 'function',
                'name': 'replace_spaces',
                'parameters': [{'name': 'text', 'type': 'str'}],
                'return_type': 'str',
                'implementation': {
                    'algorithm': 'string_replace',
                    'complexity': 'O(n)',
                    'template': '''
def replace_spaces(text: str) -> str:
    """
    Replace all spaces with underscores in a string.
    
    Args:
        text (str): Input string
        
    Returns:
        str: String with spaces replaced by underscores
    """
    return text.replace(' ', '_')

def main():
    try:
        text = input("Enter a string: ")
        result = replace_spaces(text)
        print(f"String with spaces replaced: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['replace spaces', 'space to underscore', 'spaces with underscore']
            },
            'count_char_frequency': {
                'type': 'function',
                'name': 'count_char_frequency',
                'parameters': [{'name': 'text', 'type': 'str'}],
                'return_type': 'Dict[str, int]',
                'implementation': {
                    'algorithm': 'string_frequency',
                    'complexity': 'O(n)',
                    'template': '''from typing import Dict

def count_char_frequency(text: str) -> Dict[str, int]:
    """
    Count the frequency of each character in a string.
    
    Args:
        text (str): Input string
        
    Returns:
        Dict[str, int]: Dictionary containing character frequencies
    """
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

def main():
    try:
        text = input("Enter a string: ")
        result = count_char_frequency(text)
        print("Character frequencies:")
        for char, freq in result.items():
            print(f"'{char}': {freq}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['character frequency', 'count characters', 'frequency of characters']
            },
            'toggle_case': {
                'type': 'function',
                'name': 'toggle_case',
                'parameters': [{'name': 'text', 'type': 'str'}],
                'return_type': 'str',
                'implementation': {
                    'algorithm': 'string_case',
                    'complexity': 'O(n)',
                    'template': '''
def toggle_case(text: str) -> str:
    """
    Toggle the case of each character in a string.
    
    Args:
        text (str): Input string
        
    Returns:
        str: String with toggled case
    """
    return ''.join(char.swapcase() for char in text)

def main():
    try:
        text = input("Enter a string: ")
        result = toggle_case(text)
        print(f"String with toggled case: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['toggle case', 'switch case', 'change case']
            },
            'count_even_odd': {
                'type': 'function',
                'name': 'count_even_odd',
                'parameters': [{'name': 'numbers', 'type': 'List[int]'}],
                'return_type': 'Dict[str, int]',
                'implementation': {
                    'algorithm': 'list_even_odd_count',
                    'complexity': 'O(n)',
                    'template': '''from typing import List, Dict

def count_even_odd(numbers: List[int]) -> Dict[str, int]:
    """
    Count the number of even and odd numbers in a list.
    """
    even = sum(1 for n in numbers if n % 2 == 0)
    odd = sum(1 for n in numbers if n % 2 != 0)
    return {'even': even, 'odd': odd}

def main():
    try:
        numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
        result = count_even_odd(numbers)
        print(f"Even: {result['even']}")
        print(f"Odd: {result['odd']}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['even and odd', 'count even', 'count odd', 'even numbers', 'odd numbers']
            },
            'merge_sorted_lists': {
                'type': 'function',
                'name': 'merge_sorted_lists',
                'parameters': [
                    {'name': 'list1', 'type': 'List[int]'},
                    {'name': 'list2', 'type': 'List[int]'}
                ],
                'return_type': 'List[int]',
                'implementation': {
                    'algorithm': 'merge_sorted_lists',
                    'complexity': 'O(n+m)',
                    'template': '''from typing import List

def merge_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
    """
    Merge two sorted lists into a single sorted list.
    """
    i, j = 0, 0
    merged = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

def main():
    try:
        list1 = list(map(int, input("Enter first sorted list (space-separated): ").split()))
        list2 = list(map(int, input("Enter second sorted list (space-separated): ").split()))
        result = merge_sorted_lists(list1, list2)
        print(f"Merged list: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['merge sorted lists', 'merge lists', 'combine sorted lists']
            },
            'remove_element': {
                'type': 'function',
                'name': 'remove_element',
                'parameters': [
                    {'name': 'numbers', 'type': 'List[int]'},
                    {'name': 'element', 'type': 'int'}
                ],
                'return_type': 'List[int]',
                'implementation': {
                    'algorithm': 'remove_element',
                    'complexity': 'O(n)',
                    'template': '''from typing import List

def remove_element(numbers: List[int], element: int) -> List[int]:
    """
    Remove all occurrences of a specific element from a list.
    """
    return [n for n in numbers if n != element]

def main():
    try:
        numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
        element = int(input("Enter element to remove: "))
        result = remove_element(numbers, element)
        print(f"List after removal: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['remove element', 'remove all occurrences', 'delete element']
            },
            'split_list_halves': {
                'type': 'function',
                'name': 'split_list_halves',
                'parameters': [{'name': 'numbers', 'type': 'List[int]'}],
                'return_type': 'Tuple[List[int], List[int]]',
                'implementation': {
                    'algorithm': 'split_list_halves',
                    'complexity': 'O(n)',
                    'template': '''from typing import List, Tuple

def split_list_halves(numbers: List[int]) -> Tuple[List[int], List[int]]:
    """
    Split a list into two halves.
    """
    mid = len(numbers) // 2
    return numbers[:mid], numbers[mid:]

def main():
    try:
        numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
        first, second = split_list_halves(numbers)
        print(f"First half: {first}")
        print(f"Second half: {second}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['split list', 'two halves', 'divide list']
            },
            'max_min_difference': {
                'type': 'function',
                'name': 'max_min_difference',
                'parameters': [{'name': 'numbers', 'type': 'List[int]'}],
                'return_type': 'int',
                'implementation': {
                    'algorithm': 'max_min_difference',
                    'complexity': 'O(n)',
                    'template': '''from typing import List

def max_min_difference(numbers: List[int]) -> int:
    """
    Find the difference between the maximum and minimum elements in a list.
    """
    return max(numbers) - min(numbers) if numbers else 0

def main():
    try:
        numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
        result = max_min_difference(numbers)
        print(f"Difference: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['difference between maximum and minimum', 'max min difference', 'range of list']
            },
            'element_frequency': {
                'type': 'function',
                'name': 'element_frequency',
                'parameters': [{'name': 'numbers', 'type': 'List[int]'}],
                'return_type': 'Dict[int, int]',
                'implementation': {
                    'algorithm': 'element_frequency',
                    'complexity': 'O(n)',
                    'template': '''from typing import List, Dict

def element_frequency(numbers: List[int]) -> Dict[int, int]:
    """
    Count the frequency of each element in a list.
    """
    freq = {}
    for n in numbers:
        freq[n] = freq.get(n, 0) + 1
    return freq

def main():
    try:
        numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
        result = element_frequency(numbers)
        print("Element frequencies:")
        for k, v in result.items():
            print(f"{k}: {v}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['frequency of each element', 'element frequency', 'count frequency in list']
            },
            'common_unique_elements': {
                'type': 'function',
                'name': 'common_unique_elements',
                'parameters': [
                    {'name': 'list1', 'type': 'List[int]'},
                    {'name': 'list2', 'type': 'List[int]'}
                ],
                'return_type': 'List[int]',
                'implementation': {
                    'algorithm': 'common_unique_elements',
                    'complexity': 'O(n+m)',
                    'template': '''from typing import List

def common_unique_elements(list1: List[int], list2: List[int]) -> List[int]:
    """
    Find all unique elements common to two lists.
    """
    return list(set(list1) & set(list2))

def main():
    try:
        list1 = list(map(int, input("Enter first list (space-separated): ").split()))
        list2 = list(map(int, input("Enter second list (space-separated): ").split()))
        result = common_unique_elements(list1, list2)
        print(f"Common unique elements: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['unique elements common', 'common elements', 'intersection of lists']
            },
            'shuffle_list': {
                'type': 'function',
                'name': 'shuffle_list',
                'parameters': [{'name': 'numbers', 'type': 'List[int]'}],
                'return_type': 'List[int]',
                'implementation': {
                    'algorithm': 'shuffle_list',
                    'complexity': 'O(n)',
                    'template': '''from typing import List
import random

def shuffle_list(numbers: List[int]) -> List[int]:
    """
    Shuffle the elements of a list randomly.
    """
    shuffled = numbers[:]
    random.shuffle(shuffled)
    return shuffled

def main():
    try:
        numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
        result = shuffle_list(numbers)
        print(f"Shuffled list: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['shuffle list', 'randomly shuffle', 'random order']
            },
            'lcm': {
                'type': 'function',
                'name': 'lcm',
                'parameters': [
                    {'name': 'a', 'type': 'int'},
                    {'name': 'b', 'type': 'int'}
                ],
                'return_type': 'int',
                'implementation': {
                    'algorithm': 'lcm',
                    'complexity': 'O(log(min(a,b)))',
                    'template': '''from typing import List

def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.
    """
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers.
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def main():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = lcm(a, b)
        print(f"LCM of {a} and {b} is: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['lcm', 'least common multiple', 'find lcm']
            },
            'decimal_to_binary': {
                'type': 'function',
                'name': 'decimal_to_binary',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'str',
                'implementation': {
                    'algorithm': 'decimal_to_binary',
                    'complexity': 'O(log n)',
                    'template': '''def decimal_to_binary(n: int) -> str:
    """
    Convert a decimal number to binary.
    """
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return binary

def main():
    try:
        n = int(input("Enter a decimal number: "))
        result = decimal_to_binary(n)
        print(f"Binary representation: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['decimal to binary', 'convert decimal', 'binary conversion']
            },
            'sum_of_digits': {
                'type': 'function',
                'name': 'sum_of_digits',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'int',
                'implementation': {
                    'algorithm': 'sum_of_digits',
                    'complexity': 'O(log n)',
                    'template': '''def sum_of_digits(n: int) -> int:
    """
    Find the sum of digits of a number.
    """
    return sum(int(digit) for digit in str(abs(n)))

def main():
    try:
        n = int(input("Enter a number: "))
        result = sum_of_digits(n)
        print(f"Sum of digits: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['sum of digits', 'digit sum', 'sum digits']
            },
            'find_factors': {
                'type': 'function',
                'name': 'find_factors',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'List[int]',
                'implementation': {
                    'algorithm': 'find_factors',
                    'complexity': 'O(sqrt(n))',
                    'template': '''from typing import List

def find_factors(n: int) -> List[int]:
    """
    Find all factors of a given number.
    """
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

def main():
    try:
        n = int(input("Enter a number: "))
        result = find_factors(n)
        print(f"Factors: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['factors', 'find factors', 'all factors']
            },
            'strong_number': {
                'type': 'function',
                'name': 'is_strong_number',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'bool',
                'implementation': {
                    'algorithm': 'strong_number',
                    'complexity': 'O(log n)',
                    'template': '''def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

def is_strong_number(n: int) -> bool:
    """
    Check if a number is a strong number.
    A strong number is a number whose sum of the factorial of digits is equal to the number itself.
    """
    return n == sum(factorial(int(digit)) for digit in str(n))

def main():
    try:
        n = int(input("Enter a number: "))
        result = is_strong_number(n)
        print(f"Is strong number: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['strong number', 'check strong number', 'is strong number']
            },
            'reverse_digits': {
                'type': 'function',
                'name': 'reverse_digits',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'int',
                'implementation': {
                    'algorithm': 'reverse_digits',
                    'complexity': 'O(log n)',
                    'template': '''def reverse_digits(n: int) -> int:
    """
    Reverse the digits of a number.
    """
    return int(str(abs(n))[::-1]) * (1 if n >= 0 else -1)

def main():
    try:
        n = int(input("Enter a number: "))
        result = reverse_digits(n)
        print(f"Reversed number: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['reverse digits', 'reverse number', 'reverse a number']
            },
            'first_n_primes': {
                'type': 'function',
                'name': 'first_n_primes',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'List[int]',
                'implementation': {
                    'algorithm': 'first_n_primes',
                    'complexity': 'O(n * sqrt(n))',
                    'template': '''from typing import List

def is_prime(num: int) -> bool:
    """
    Check if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n: int) -> List[int]:
    """
    Print the first n prime numbers.
    """
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def main():
    try:
        n = int(input("Enter the number of primes to generate: "))
        result = first_n_primes(n)
        print(f"First {n} prime numbers: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['first n prime numbers', 'generate primes', 'print primes']
            },
            'first_n_fibonacci': {
                'type': 'function',
                'name': 'first_n_fibonacci',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'List[int]',
                'implementation': {
                    'algorithm': 'first_n_fibonacci',
                    'complexity': 'O(n)',
                    'template': '''from typing import List

def first_n_fibonacci(n: int) -> List[int]:
    """
    Generate the first n Fibonacci numbers.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def main():
    try:
        n = int(input("Enter the number of Fibonacci numbers to generate: "))
        result = first_n_fibonacci(n)
        print(f"First {n} Fibonacci numbers: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['first n fibonacci numbers', 'generate fibonacci', 'print fibonacci']
            },
            'multiplication_table': {
                'type': 'function',
                'name': 'multiplication_table',
                'parameters': [{'name': 'n', 'type': 'int'}],
                'return_type': 'None',
                'implementation': {
                    'algorithm': 'multiplication_table',
                    'complexity': 'O(n)',
                    'template': '''def multiplication_table(n: int) -> None:
    """
    Generate a multiplication table for a given number.
    """
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def main():
    try:
        n = int(input("Enter a number: "))
        multiplication_table(n)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
'''
                },
                'keywords': ['multiplication table', 'generate table', 'print table']
            }
        }
    
    def set_context(self, context: Dict[str, Any]):
        """
        Set additional context for semantic analysis.
        
        Args:
            context (Dict[str, Any]): Additional context information
        """
        self.context = context
    
    def analyze(self, parse_tree: ParseNode) -> SemanticInfo:
        """
        Analyze parse tree and extract semantic information.
        
        Args:
            parse_tree (ParseNode): Parse tree to analyze
            
        Returns:
            SemanticInfo: Semantic information extracted from parse tree
        """
        # Extract purpose from parse tree
        purpose = self._extract_purpose(parse_tree)
        
        # DEBUG: Log the purpose string
        print(f"[DEBUG] Purpose for semantic analysis: '{purpose}'")
        
        # Match purpose against known patterns
        implementation = self._match_implementation_pattern(purpose)
        if implementation:
            return SemanticInfo(
                type=implementation['type'],
                name=implementation['name'],
                parameters=implementation['parameters'],
                return_type=implementation['return_type'],
                implementation=implementation['implementation'],
                docstring=self._generate_docstring(purpose)
            )
        
        # If no pattern matches, use generic function template
        return SemanticInfo(
            type='function',
            name='generated_function',
            parameters=[{'name': 'n', 'type': 'int'}],
            return_type='bool',
            implementation={'algorithm': 'generic'},
            docstring=self._generate_docstring(purpose)
        )
    
    def _extract_purpose(self, node: ParseNode) -> str:
        """Extract purpose from parse tree node."""
        if node.type == NodeType.FUNCTION:
            return ' '.join(token.text for token in node.tokens)
        return ''
    
    def _match_implementation_pattern(self, purpose: str) -> Optional[Dict[str, Any]]:
        """Match purpose against known implementation patterns."""
        purpose = purpose.lower()
        # String manipulation patterns
        if any(keyword in purpose for keyword in ['vowel', 'consonant']) and 'count' in purpose:
            return self.implementation_patterns['count_vowels_consonants']
        if 'anagram' in purpose:
            return self.implementation_patterns['check_anagrams']
        if ('non' in purpose and 'alphabet' in purpose) or ('non' in purpose and 'alpha' in purpose):
            return self.implementation_patterns['remove_non_alpha']
        if 'longest word' in purpose:
            return self.implementation_patterns['find_longest_word']
        if 'replace' in purpose and 'space' in purpose:
            return self.implementation_patterns['replace_spaces']
        if 'frequency' in purpose and 'character' in purpose:
            return self.implementation_patterns['count_char_frequency']
        if 'toggle' in purpose and 'case' in purpose:
            return self.implementation_patterns['toggle_case']
        # List manipulation patterns
        if ('even' in purpose and 'odd' in purpose and 'count' in purpose) or ('count' in purpose and 'even' in purpose) or ('count' in purpose and 'odd' in purpose):
            return self.implementation_patterns['count_even_odd']
        if 'merge' in purpose and 'sorted' in purpose and 'list' in purpose:
            return self.implementation_patterns['merge_sorted_lists']
        if ('remove' in purpose and 'element' in purpose) or ('remove' in purpose and 'occurrences' in purpose):
            return self.implementation_patterns['remove_element']
        if ('split' in purpose and 'list' in purpose and 'half' in purpose) or ('divide' in purpose and 'list' in purpose):
            return self.implementation_patterns['split_list_halves']
        if ('difference' in purpose and 'maximum' in purpose and 'minimum' in purpose) or ('max' in purpose and 'min' in purpose and 'difference' in purpose):
            return self.implementation_patterns['max_min_difference']
        if ('frequency' in purpose and 'element' in purpose) or ('count' in purpose and 'frequency' in purpose and 'list' in purpose):
            return self.implementation_patterns['element_frequency']
        if ('unique' in purpose and 'common' in purpose and 'list' in purpose) or ('common' in purpose and 'elements' in purpose and 'list' in purpose):
            return self.implementation_patterns['common_unique_elements']
        if ('shuffle' in purpose and 'list' in purpose) or ('random' in purpose and 'order' in purpose):
            return self.implementation_patterns['shuffle_list']
        # Number-based patterns
        if 'lcm' in purpose or 'least common multiple' in purpose:
            return self.implementation_patterns['lcm']
        if 'decimal to binary' in purpose or 'convert decimal' in purpose:
            return self.implementation_patterns['decimal_to_binary']
        if 'sum of digits' in purpose or 'digit sum' in purpose:
            return self.implementation_patterns['sum_of_digits']
        if 'factors' in purpose or 'find factors' in purpose:
            return self.implementation_patterns['find_factors']
        if 'strong number' in purpose or 'check strong number' in purpose:
            return self.implementation_patterns['strong_number']
        if 'reverse digits' in purpose or 'reverse number' in purpose:
            return self.implementation_patterns['reverse_digits']
        if 'first n prime numbers' in purpose or 'generate primes' in purpose:
            return self.implementation_patterns['first_n_primes']
        if 'first n fibonacci numbers' in purpose or 'generate fibonacci' in purpose:
            return self.implementation_patterns['first_n_fibonacci']
        if 'multiplication table' in purpose or 'generate table' in purpose:
            return self.implementation_patterns['multiplication_table']
        # Existing checks for other patterns
        operations = {'add', 'subtract', 'multiply', 'divide'}
        for op in operations:
            if op in purpose:
                return {
                    'type': 'function',
                    'name': f"{op}_numbers",
                    'parameters': [
                        {'name': 'a', 'type': 'int'},
                        {'name': 'b', 'type': 'int'}
                    ],
                    'return_type': 'int',
                    'implementation': {
                        'algorithm': 'arithmetic',
                        'operation': op
                    }
                }
        if 'binary search' in purpose:
            return self.implementation_patterns['binary_search']
        elif 'bubble sort' in purpose:
            return self.implementation_patterns['bubble_sort']
        elif 'linked list' in purpose:
            return self.implementation_patterns['linked_list']
        elif 'binary tree' in purpose:
            return self.implementation_patterns['binary_tree']
        elif 'graph' in purpose:
            return self.implementation_patterns['graph']
        elif 'dijkstra' in purpose:
            return self.implementation_patterns['dijkstra']
        for pattern in self.implementation_patterns.values():
            if any(keyword in purpose for keyword in pattern['keywords']):
                return pattern
        return None
    
    def _generate_docstring(self, purpose: str) -> str:
        """Generate docstring from purpose."""
        return f"Generated from instruction: {purpose}"

class SemanticError(Exception):
    """Exception raised when semantic analysis fails."""
    pass 