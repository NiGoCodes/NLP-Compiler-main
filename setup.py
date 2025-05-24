from setuptools import setup, find_packages

setup(
    name="nlp_compiler",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "spacy==3.7.2",
        "nltk==3.8.1",
        "pytest==7.4.3",
        "python-dotenv==1.0.0",
    ],
    python_requires=">=3.7",
) 