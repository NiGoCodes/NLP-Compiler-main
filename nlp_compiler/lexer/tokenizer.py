"""
Lexical analysis component that tokenizes input text using spaCy.
"""

from typing import List, Dict, Any
from dataclasses import dataclass
from spacy.tokens import Doc
from spacy.language import Language

@dataclass
class Token:
    """Represents a token with its properties."""
    text: str
    pos: str  # Part of speech
    lemma: str
    tag: str  # Detailed POS tag
    dep: str  # Dependency relation
    is_keyword: bool = False

class Tokenizer:
    """Handles lexical analysis of input text using spaCy."""
    
    # Keywords that are important for code generation
    KEYWORDS = {
        'function', 'def', 'class', 'method', 'return', 'if', 'else', 'for', 'while',
        'in', 'is', 'and', 'or', 'not', 'with', 'as', 'import', 'from', 'create',
        'write', 'build', 'make', 'check', 'get', 'set', 'add', 'remove', 'find',
        'calculate', 'compute', 'display', 'show', 'print'
    }
    
    def __init__(self, nlp: Language):
        """
        Initialize the tokenizer with a spaCy language model.
        
        Args:
            nlp (Language): Loaded spaCy language model
        """
        self.nlp = nlp
    
    def tokenize(self, text: str) -> List[Token]:
        """
        Tokenize input text into a list of Token objects.
        
        Args:
            text (str): Input text to tokenize
            
        Returns:
            List[Token]: List of Token objects with linguistic properties
        """
        doc = self.nlp(text.lower())
        return [self._create_token(token) for token in doc]
    
    def _create_token(self, token) -> Token:
        """
        Create a Token object from a spaCy token.
        
        Args:
            token: spaCy token object
            
        Returns:
            Token: Token object with linguistic properties
        """
        return Token(
            text=token.text,
            pos=token.pos_,
            lemma=token.lemma_,
            tag=token.tag_,
            dep=token.dep_,
            is_keyword=token.text.lower() in self.KEYWORDS
        )
    
    def get_keywords(self, tokens: List[Token]) -> List[Token]:
        """
        Extract keywords from tokens.
        
        Args:
            tokens (List[Token]): List of tokens
            
        Returns:
            List[Token]: List of keyword tokens
        """
        return [token for token in tokens if token.is_keyword]
    
    def get_nouns(self, tokens: List[Token]) -> List[Token]:
        """
        Extract nouns from tokens.
        
        Args:
            tokens (List[Token]): List of tokens
            
        Returns:
            List[Token]: List of noun tokens
        """
        return [token for token in tokens if token.pos in {'NOUN', 'PROPN'}]
    
    def get_verbs(self, tokens: List[Token]) -> List[Token]:
        """
        Extract verbs from tokens.
        
        Args:
            tokens (List[Token]): List of tokens
            
        Returns:
            List[Token]: List of verb tokens
        """
        return [token for token in tokens if token.pos == 'VERB'] 