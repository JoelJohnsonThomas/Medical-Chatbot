try:
    from langchain.chains.combine_documents import create_stuff_documents_chain
    print("Success: from langchain.chains.combine_documents import create_stuff_documents_chain")
except ImportError:
    print("Failed: from langchain.chains.combine_documents import create_stuff_documents_chain")

try:
    from langchain.chains import create_stuff_documents_chain
    print("Success: from langchain.chains import create_stuff_documents_chain")
except ImportError:
    print("Failed: from langchain.chains import create_stuff_documents_chain")

try:
    from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
    print("Success: from langchain.chains.combine_documents.stuff import create_stuff_documents_chain")
except ImportError:
    print("Failed: from langchain.chains.combine_documents.stuff import create_stuff_documents_chain")
