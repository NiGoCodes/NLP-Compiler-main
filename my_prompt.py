from nlp_compiler import NLCompiler

compiler = NLCompiler()

# Put your prompt (instruction) here:
instruction = "Write a Python code to check if a number is palindrome"

# Compile the instruction to generate code
code = compiler.compile(instruction)

# Print the generated code
print("Generated Code:")
print(code)

with open("generated_code.py", "w") as f:
    f.write(code)
print("Generated code saved to generated_code.py")
#generarted on 25/05/2025