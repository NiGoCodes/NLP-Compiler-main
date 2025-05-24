"""
Tests for the NLP compiler components.
"""

import pytest
from nlp_compiler import NLCompiler
from nlp_compiler.lexer.tokenizer import Tokenizer
from nlp_compiler.parser.parser import Parser, ParseError
from nlp_compiler.semantic.analyzer import SemanticAnalyzer, SemanticError
from nlp_compiler.codegen.generator import CodeGenerator, CodeGenerationError

@pytest.fixture
def compiler():
    """Create a compiler instance for testing."""
    return NLCompiler()

def test_prime_function(compiler):
    """Test generating a prime number check function."""
    instruction = "Write a function to check if a number is prime"
    code = compiler.compile(instruction)
    
    # Check that the generated code contains expected elements
    assert "def is_prime" in code
    assert "n: int" in code
    assert "-> bool" in code
    assert "if n < 2" in code
    assert "return False" in code
    assert "return True" in code

def test_even_numbers_function(compiler):
    """Test generating a function to filter even numbers."""
    instruction = "Build a function that returns a list of even numbers from a given list"
    code = compiler.compile(instruction)
    
    # Check that the generated code contains expected elements
    assert "def get_even_numbers" in code
    assert "numbers: List[int]" in code
    assert "-> List[int]" in code
    assert "n % 2 == 0" in code

def test_employee_class(compiler):
    """Test generating an Employee class."""
    instruction = "Create a class Employee with attributes name and salary, and a method to display details"
    code = compiler.compile(instruction)
    
    # Check that the generated code contains expected elements
    assert "class Employee" in code
    assert "def __init__" in code
    assert "self.name = name" in code
    assert "self.salary = salary" in code
    assert "def display_details" in code

def test_generic_function(compiler):
    """Test generating a generic function."""
    instruction = "Write a function to calculate the factorial of a number"
    code = compiler.compile(instruction)
    
    # Check that the generated code contains expected elements
    assert "def generated_function" in code
    assert "pass" in code  # Generic functions have TODO implementation

def test_invalid_instruction(compiler):
    """Test handling of invalid instructions."""
    with pytest.raises(ParseError):
        compiler.compile("This is not a valid instruction")

def test_tokenizer():
    """Test the tokenizer component."""
    import spacy
    nlp = spacy.load("en_core_web_sm")
    tokenizer = Tokenizer(nlp)
    tokens = tokenizer.tokenize("Write a function to check if a number is prime")
    
    # Check that tokens are created correctly
    assert len(tokens) > 0
    assert any(t.is_keyword for t in tokens)  # Should have some keywords
    assert any(t.pos == "VERB" for t in tokens)  # Should have some verbs
    assert any(t.pos == "NOUN" for t in tokens)  # Should have some nouns

def test_parser():
    """Test the parser component."""
    from nlp_compiler.parser.parser import NodeType
    import spacy
    nlp = spacy.load("en_core_web_sm")
    parser = Parser()
    tokenizer = Tokenizer(nlp)
    
    # Test parsing a function definition
    tokens = tokenizer.tokenize("Write a function to check if a number is prime")
    parse_tree = parser.parse(tokens)
    assert parse_tree.type == NodeType.ROOT
    assert len(parse_tree.children) == 1
    assert parse_tree.children[0].type == NodeType.FUNCTION

def test_semantic_analyzer():
    """Test the semantic analyzer component."""
    import spacy
    nlp = spacy.load("en_core_web_sm")
    analyzer = SemanticAnalyzer()
    parser = Parser()
    tokenizer = Tokenizer(nlp)
    
    # Test analyzing a function definition
    tokens = tokenizer.tokenize("Write a function to check if a number is prime")
    parse_tree = parser.parse(tokens)
    semantic_info = analyzer.analyze(parse_tree)
    
    assert semantic_info.type == "function"
    assert semantic_info.name == "is_prime"
    assert len(semantic_info.parameters) == 1
    assert semantic_info.return_type == "bool"

def test_code_generator():
    """Test the code generator component."""
    import spacy
    nlp = spacy.load("en_core_web_sm")
    generator = CodeGenerator()
    analyzer = SemanticAnalyzer()
    parser = Parser()
    tokenizer = Tokenizer(nlp)
    
    # Test generating code for a function
    tokens = tokenizer.tokenize("Write a function to check if a number is prime")
    parse_tree = parser.parse(tokens)
    semantic_info = analyzer.analyze(parse_tree)
    code = generator.generate(semantic_info)
    
    assert "def is_prime" in code
    assert "n: int" in code
    assert "-> bool" in code
    assert "if n < 2" in code 