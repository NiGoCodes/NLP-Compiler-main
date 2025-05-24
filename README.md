# NLP Compiler

A rule-based natural language to Python code compiler that converts English instructions into executable Python code using core compiler concepts.

## Features

- **Lexical Analysis**: Tokenizes input text using spaCy to identify parts of speech and keywords
- **Parsing**: Uses grammar rules to identify user intent and extract code components
- **Semantic Analysis**: Interprets meaning and maps to code logic
- **Code Generation**: Generates modular Python code from templates
- **No External AI APIs**: Purely rule-based implementation

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/nlp-compiler.git
cd nlp-compiler
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Download required spaCy model:

```bash
python -m spacy download en_core_web_sm
```

## Project Structure

```
nlp_compiler/
├── __init__.py
├── lexer/           # Lexical analysis components
├── parser/          # Parsing and grammar rules
├── semantic/        # Semantic analysis
├── codegen/         # Code generation templates
└── utils/           # Utility functions
```

## Usage

```python
from nlp_compiler import NLCompiler

compiler = NLCompiler()
code = compiler.compile("Write a function to check if a number is prime")
print(code)
```

## Example Instructions

The compiler can handle various types of instructions:

1. Function definitions:

   - "Write a function to check if a number is prime"
   - "Build a function that returns a list of even numbers from a given list"

2. Class definitions:
   - "Create a class Employee with attributes name and salary, and a method to display details"

## Development

To run tests:

```bash
pytest tests/
```

## License

MIT License
