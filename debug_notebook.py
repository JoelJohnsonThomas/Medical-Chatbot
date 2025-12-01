import json
import os

notebook_path = r'e:\CSE\External\AI_Projects\Medical-Chatbot\research\trials.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

found = False
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source = cell['source']
        for j, line in enumerate(source):
            if 'create_stuff_documents_chain' in line:
                print(f"Found at Cell {i}, Line {j}: {repr(line)}")
                if 'from langchain.chains.combine_documents.stuff import create_stuff_documents_chain' in line:
                     print("Exact match found!")
