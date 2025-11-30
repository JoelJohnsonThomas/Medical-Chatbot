import langchain
import flask
import sentence_transformers
import pypdf
import pinecone
import openai
import numpy
import pandas

print("All imports successful!")
print(f"Numpy version: {numpy.__version__}")
try:
    import pytz
    print("pytz is installed")
except ImportError:
    print("pytz is NOT installed")
