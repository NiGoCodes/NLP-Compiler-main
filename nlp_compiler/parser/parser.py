"""
Parser component that handles syntax analysis and builds a parse tree.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum
from ..lexer.tokenizer import Token

class NodeType(Enum):
    """Types of nodes in the parse tree."""
    FUNCTION = "function"
    CLASS = "class"
    METHOD = "method"
    ATTRIBUTE = "attribute"
    PARAMETER = "parameter"
    RETURN = "return"
    CONDITION = "condition"
    LOOP = "loop"
    OPERATION = "operation"
    ROOT = "root"

@dataclass
class ParseNode:
    """Node in the parse tree."""
    type: NodeType
    tokens: List[Token]
    children: List['ParseNode']
    metadata: Dict[str, Any]

class Parser:
    """Handles syntax analysis and builds a parse tree."""
    
    def __init__(self):
        """Initialize the parser with grammar rules."""
        # Define patterns for different types of instructions
        # '*' matches any sequence of tokens
        # '?' matches an optional token (like articles)
        self.patterns = {
            'function': [
                # Basic function patterns with flexible structure
                ['write', '*', 'python', '*', 'code', '*', '*'],  # Write [a] python [code] [to/for] [operation]
                ['create', '*', 'python', '*', 'code', '*', '*'],  # Create [a] python [code] [to/for] [operation]
                ['build', '*', 'python', '*', 'code', '*', '*'],  # Build [a] python [code] [to/for] [operation]
                
                # Function with return value patterns
                ['write', '?', 'function', 'that', 'returns', '*'],  # Write (a) function that returns X
                ['create', '?', 'function', 'that', 'returns', '*'],  # Create (a) function that returns X
                ['build', '?', 'function', 'that', 'returns', '*'],  # Build (a) function that returns X
                ['write', '?', 'function', 'to', 'return', '*'],  # Write (a) function to return X
                ['create', '?', 'function', 'to', 'return', '*'],  # Create (a) function to return X
                ['build', '?', 'function', 'to', 'return', '*'],  # Build (a) function to return X
                
                # Function with specific purpose patterns
                ['write', '?', 'function', 'for', 'checking', '*'],  # Write (a) function for checking X
                ['create', '?', 'function', 'for', 'checking', '*'],  # Create (a) function for checking X
                ['build', '?', 'function', 'for', 'checking', '*'],  # Build (a) function for checking X
                
                # Simple function patterns
                ['write', 'function', 'to', '*'],  # Write function to do X
                ['create', 'function', 'to', '*'],  # Create function to do X
                ['build', 'function', 'to', '*'],  # Build function to do X
                
                # Specific patterns for common operations
                ['write', '?', 'python', '?', 'code', 'to', 'check', 'if', 'a', 'number', 'is', 'palindrome'],  # Write (a) python (code) to check if a number is palindrome
                ['create', '?', 'python', '?', 'code', 'to', 'check', 'if', 'a', 'number', 'is', 'palindrome'],  # Create (a) python (code) to check if a number is palindrome
                ['build', '?', 'python', '?', 'code', 'to', 'check', 'if', 'a', 'number', 'is', 'palindrome'],  # Build (a) python (code) to check if a number is palindrome
                ['write', '?', 'python', '?', 'code', 'for', 'checking', 'if', 'a', 'number', 'is', 'palindrome'],  # Write (a) python (code) for checking if a number is palindrome
                ['create', '?', 'python', '?', 'code', 'for', 'checking', 'if', 'a', 'number', 'is', 'palindrome'],  # Create (a) python (code) for checking if a number is palindrome
                ['build', '?', 'python', '?', 'code', 'for', 'checking', 'if', 'a', 'number', 'is', 'palindrome'],  # Build (a) python (code) for checking if a number is palindrome
            ],
            'class': [
                ['create', '?', 'class', '*', 'with', '*'],  # Create (a) class X with Y
                ['define', '?', 'class', '*', 'with', '*'],  # Define (a) class X with Y
                ['make', '?', 'class', '*', 'with', '*'],  # Make (a) class X with Y
                ['write', '?', 'class', '*', 'with', '*'],  # Write (a) class X with Y
            ],
            'method': [
                ['add', '?', 'method', '*', 'to', '*'],  # Add (a) method X to Y
                ['create', '?', 'method', '*', 'for', '*'],  # Create (a) method X for Y
                ['define', '?', 'method', '*', 'for', '*'],  # Define (a) method X for Y
                ['write', '?', 'method', '*', 'for', '*'],  # Write (a) method X for Y
            ]
        }
        
        # Articles and other words to skip in pattern matching
        self.skip_words = {'a', 'an', 'the', 'some', 'any', 'from', 'given'}
        
        # Common prompt variations and their corrections
        self.prompt_variations = {
            'write python code': 'write a python code to',
            'write python': 'write a python code to',
            'create python': 'create a python code to',
            'build python': 'build a python code to',
            'write code': 'write a python code to',
            'create code': 'create a python code to',
            'build code': 'build a python code to',
        }
    
    def parse(self, tokens: List[Token]) -> ParseNode:
        """
        Parse tokens into a parse tree.
        
        Args:
            tokens (List[Token]): List of tokens from lexical analysis
            
        Returns:
            ParseNode: Root node of the parse tree
            
        Raises:
            ParseError: If the input cannot be parsed
        """
        root = ParseNode(NodeType.ROOT, tokens, [], {})
        
        # Filter out articles and other skip words
        filtered_tokens = [t for t in tokens if t.text.lower() not in self.skip_words]
        
        # Try to identify the instruction type
        instruction_type = self._identify_instruction_type(filtered_tokens)
        
        # If instruction type not found, try to fix common prompt variations
        if not instruction_type:
            fixed_tokens = self._fix_common_prompt_variations(tokens)
            if fixed_tokens:
                filtered_tokens = [t for t in fixed_tokens if t.text.lower() not in self.skip_words]
                instruction_type = self._identify_instruction_type(filtered_tokens)
                if instruction_type:
                    tokens = fixed_tokens
                else:
                    self._suggest_prompt_fixes(tokens)
        
        if not instruction_type:
            raise ParseError("Could not identify instruction type")
        
        # Create appropriate node based on instruction type
        if instruction_type == 'function':
            node = self._parse_function(tokens)
        elif instruction_type == 'class':
            node = self._parse_class(tokens)
        elif instruction_type == 'method':
            node = self._parse_method(tokens)
        else:
            raise ParseError(f"Unsupported instruction type: {instruction_type}")
        
        root.children.append(node)
        return root
    
    def _fix_common_prompt_variations(self, tokens: List[Token]) -> Optional[List[Token]]:
        """
        Try to fix common prompt variations.
        
        Args:
            tokens (List[Token]): List of tokens
            
        Returns:
            Optional[List[Token]]: Fixed tokens if a variation was found, None otherwise
        """
        # Convert tokens to lowercase string for matching
        token_text = ' '.join(t.text.lower() for t in tokens)
        
        # Check for common variations
        for variation, correction in self.prompt_variations.items():
            if variation in token_text:
                # Replace the variation with the correction
                corrected_text = token_text.replace(variation, correction)
                # Create new tokens from the corrected text
                return [Token(text=word, pos='', lemma='', tag='', dep='', is_keyword=False) 
                       for word in corrected_text.split()]
        
        return None
    
    def _suggest_prompt_fixes(self, tokens: List[Token]):
        """
        Suggest fixes for the prompt.
        
        Args:
            tokens (List[Token]): List of tokens
        """
        token_text = ' '.join(t.text.lower() for t in tokens)
        
        # Check for missing 'to' after 'code'
        if 'code' in token_text and 'to' not in token_text:
            raise ParseError("Please add 'to' after 'code' in your instruction. For example: 'Write a python code to divide two numbers'")
        
        # Check for missing 'python code'
        if 'write' in token_text and 'python' not in token_text and 'code' not in token_text:
            raise ParseError("Please specify 'python code' in your instruction. For example: 'Write a python code to divide two numbers'")
        
        # Check for missing operation
        if 'numbers' in token_text and not any(op in token_text for op in ['add', 'subtract', 'multiply', 'divide']):
            raise ParseError("Please specify the operation (add, subtract, multiply, or divide) in your instruction. For example: 'Write a python code to divide two numbers'")
        
        # Generic error message
        raise ParseError("Please use a complete instruction. For example: 'Write a python code to divide two numbers'")
    
    def _match_pattern(self, token_texts: List[str], pattern: List[str]) -> bool:
        """
        Check if token texts match a pattern with improved flexibility.
        
        Args:
            token_texts (List[str]): List of token texts
            pattern (List[str]): Pattern to match against
            
        Returns:
            bool: True if pattern matches
        """
        if len(token_texts) < len(pattern):
            return False
        
        pattern_idx = 0
        text_idx = 0
        
        while pattern_idx < len(pattern) and text_idx < len(token_texts):
            if pattern[pattern_idx] == '*':
                # '*' matches any sequence of tokens until the next pattern element
                if pattern_idx == len(pattern) - 1:
                    return True
                next_pattern = pattern[pattern_idx + 1]
                while text_idx < len(token_texts):
                    if token_texts[text_idx] == next_pattern:
                        pattern_idx += 1
                        break
                    text_idx += 1
                if text_idx == len(token_texts):
                    return False
            elif pattern[pattern_idx] == '?':
                # '?' matches an optional token
                pattern_idx += 1
                continue
            elif pattern[pattern_idx] == token_texts[text_idx]:
                pattern_idx += 1
                text_idx += 1
            else:
                # Skip articles and other skip words
                if token_texts[text_idx] in self.skip_words:
                    text_idx += 1
                    continue
                return False
        
        # Check if we've matched all pattern elements
        return pattern_idx == len(pattern) or (pattern_idx == len(pattern) - 1 and pattern[-1] == '*')
    
    def _identify_instruction_type(self, tokens: List[Token]) -> Optional[str]:
        """
        Identify the type of instruction from tokens with improved pattern matching.
        
        Args:
            tokens (List[Token]): List of tokens
            
        Returns:
            Optional[str]: Type of instruction or None if not recognized
        """
        token_texts = [t.text.lower() for t in tokens]
        
        # First, try exact pattern matching
        for instr_type, patterns in self.patterns.items():
            for pattern in patterns:
                if self._match_pattern(token_texts, pattern):
                    return instr_type
        
        # If no exact match, try flexible matching
        for instr_type, patterns in self.patterns.items():
            for pattern in patterns:
                # Check if all non-wildcard pattern elements are present in the tokens
                pattern_elements = [p for p in pattern if p not in ['*', '?']]
                if pattern_elements and all(any(p == t for t in token_texts) for p in pattern_elements):
                    return instr_type
        
        return None
    
    def _parse_function(self, tokens: List[Token]) -> ParseNode:
        """
        Parse function definition tokens.
        
        Args:
            tokens (List[Token]): List of tokens
            
        Returns:
            ParseNode: Function node
        """
        # Extract function name and purpose
        name = self._extract_function_name(tokens)
        purpose = self._extract_function_purpose(tokens)
        
        return ParseNode(
            type=NodeType.FUNCTION,
            tokens=tokens,
            children=[],
            metadata={
                'name': name,
                'purpose': purpose,
                'parameters': self._extract_parameters(tokens),
                'return_type': self._infer_return_type(tokens)
            }
        )
    
    def _parse_class(self, tokens: List[Token]) -> ParseNode:
        """
        Parse class definition tokens.
        
        Args:
            tokens (List[Token]): List of tokens
            
        Returns:
            ParseNode: Class node
        """
        # Extract class name and attributes
        name = self._extract_class_name(tokens)
        attributes = self._extract_attributes(tokens)
        
        return ParseNode(
            type=NodeType.CLASS,
            tokens=tokens,
            children=[],
            metadata={
                'name': name,
                'attributes': attributes,
                'methods': self._extract_methods(tokens)
            }
        )
    
    def _parse_method(self, tokens: List[Token]) -> ParseNode:
        """
        Parse method definition tokens.
        
        Args:
            tokens (List[Token]): List of tokens
            
        Returns:
            ParseNode: Method node
        """
        # Extract method name and purpose
        name = self._extract_method_name(tokens)
        purpose = self._extract_method_purpose(tokens)
        
        return ParseNode(
            type=NodeType.METHOD,
            tokens=tokens,
            children=[],
            metadata={
                'name': name,
                'purpose': purpose,
                'parameters': self._extract_parameters(tokens),
                'return_type': self._infer_return_type(tokens)
            }
        )
    
    def _extract_function_name(self, tokens: List[Token]) -> str:
        """Extract function name from tokens."""
        # Try to extract operation and objects (e.g., add two numbers)
        operations = {'add', 'subtract', 'multiply', 'divide'}
        op = None
        for token in tokens:
            if token.lemma.lower() in operations:
                op = token.lemma.lower()
                break
        if op:
            # Try to find what is being operated on (e.g., numbers)
            nouns = [t.text for t in tokens if t.pos in ('NOUN', 'PROPN')]
            if nouns:
                return f"{op}_{'_'.join(nouns)}"
            else:
                return f"{op}_numbers"
        return "generated_function"
    
    def _extract_function_purpose(self, tokens: List[Token]) -> str:
        """Extract function purpose from tokens."""
        # Implementation depends on specific patterns
        return " ".join(t.text for t in tokens)
    
    def _extract_parameters(self, tokens: List[Token]) -> List[Dict[str, str]]:
        """Extract function/method parameters from tokens."""
        # For arithmetic operations, expect two numbers
        operations = {'add', 'subtract', 'multiply', 'divide'}
        if any(token.lemma.lower() in operations for token in tokens):
            return [
                {'name': 'a', 'type': 'int'},
                {'name': 'b', 'type': 'int'}
            ]
        return []
    
    def _infer_return_type(self, tokens: List[Token]) -> str:
        """Infer return type from tokens."""
        # Implementation depends on specific patterns
        return "Any"
    
    def _extract_class_name(self, tokens: List[Token]) -> str:
        """Extract class name from tokens."""
        # Try to find the first proper noun or noun after 'class'
        found_class = False
        for token in tokens:
            if found_class and token.pos in ('PROPN', 'NOUN'):
                return token.text.capitalize()
            if token.text.lower() == 'class':
                found_class = True
        return "GeneratedClass"
    
    def _extract_attributes(self, tokens: List[Token]) -> List[Dict[str, str]]:
        # Look for "attributes" and collect nouns after it until "method" or end
        attrs = []
        collecting = False
        for token in tokens:
            if token.text.lower() == "attributes":
                collecting = True
                continue
            if collecting:
                if token.text.lower() == "method":
                    break
                if token.pos in ("NOUN", "PROPN"):
                    # Guess type: if "salary" in name, use float, else str
                    attr_type = "float" if "salary" in token.text.lower() else "str"
                    attrs.append({"name": token.text, "type": attr_type})
        return attrs
    
    def _extract_methods(self, tokens: List[Token]) -> List[Dict[str, str]]:
        # Look for "method" and collect the next noun as method name.
        # If the next noun is "details" and the previous token is a verb (like "display"), then join them as "display_details".
        methods = []
        for i, token in enumerate(tokens):
            if token.text.lower() == "method":
                # Next NOUN/PROPN is method name
                for j in range(i+1, len(tokens)):
                    if tokens[j].pos in ("NOUN", "PROPN"):
                        method_name = tokens[j].text
                        # If the next noun is "details" and the previous token (if any) is a verb, join them.
                        if (method_name.lower() == "details" and (j-1) >= 0 and tokens[j-1].pos == "VERB"):
                            method_name = tokens[j-1].text + "_" + method_name
                        methods.append({
                            "name": method_name,
                            "parameters": [],
                            "return_type": "str"
                        })
                        break
        return methods
    
    def _extract_method_name(self, tokens: List[Token]) -> str:
        """Extract method name from tokens."""
        # Implementation depends on specific patterns
        return "generated_method"

class ParseError(Exception):
    """Exception raised when parsing fails."""
    pass 