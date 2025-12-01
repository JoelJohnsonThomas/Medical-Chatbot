import langchain
import langchain.chains
try:
    from langchain.chains.combine_documents import create_stuff_documents_chain
    print("Import successful from langchain.chains.combine_documents")
except ImportError as e:
    print(f"Import failed: {e}")

try:
    from langchain.chains import create_stuff_documents_chain
    print("Import successful from langchain.chains")
except ImportError as e:
    print(f"Import failed from langchain.chains: {e}")

print(f"LangChain version: {langchain.__version__}")
