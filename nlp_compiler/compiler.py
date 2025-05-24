"""
Main compiler class that orchestrates the NLP to Python code compilation pipeline.
"""

from typing import Dict, Any, Optional
import spacy
from .lexer.tokenizer import Tokenizer
from .parser.parser import Parser
from .semantic.analyzer import SemanticAnalyzer
from .codegen.generator import CodeGenerator

class NLCompiler:
    """Main compiler class that coordinates the compilation pipeline."""
    
    def __init__(self):
        """Initialize the compiler with required components."""
        # Load spaCy model for NLP processing
        self.nlp = spacy.load("en_core_web_sm")
        
        # Initialize compiler components
        self.tokenizer = Tokenizer(self.nlp)
        self.parser = Parser()
        self.semantic_analyzer = SemanticAnalyzer()
        self.code_generator = CodeGenerator()
    
    def compile(self, instruction: str) -> str:
        """
        Compile natural language instruction to Python code.
        
        Args:
            instruction (str): Natural language instruction to compile
            
        Returns:
            str: Generated Python code
            
        Raises:
            CompilationError: If compilation fails at any stage
        """
        # 1. Lexical Analysis
        tokens = self.tokenizer.tokenize(instruction)
        
        # 2. Parsing
        parse_tree = self.parser.parse(tokens)
        
        # 3. Semantic Analysis
        # Pass the first child node (actual instruction) if available
        if parse_tree.children:
            semantic_info = self.semantic_analyzer.analyze(parse_tree.children[0])
        else:
            semantic_info = self.semantic_analyzer.analyze(parse_tree)
        
        # 4. Code Generation
        generated_code = self.code_generator.generate(semantic_info)
        
        return generated_code
    
    def compile_with_context(self, instruction: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Compile natural language instruction with additional context.
        
        Args:
            instruction (str): Natural language instruction to compile
            context (Dict[str, Any], optional): Additional context for compilation
            
        Returns:
            str: Generated Python code
        """
        if context is None:
            context = {}
            
        # Add context to semantic analysis
        self.semantic_analyzer.set_context(context)
        return self.compile(instruction) 