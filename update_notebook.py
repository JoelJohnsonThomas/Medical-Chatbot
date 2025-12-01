import json
import os

notebook_path = r'e:\CSE\External\AI_Projects\Medical-Chatbot\research\trials.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

found = False
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        new_source = []
        modified = False
        for line in source:
            if 'from langchain.chains.combine_documents.stuff import create_stuff_documents_chain' in line:
                new_line = line.replace('from langchain.chains.combine_documents.stuff import create_stuff_documents_chain', 'from langchain.chains.combine_documents import create_stuff_documents_chain')
                new_source.append(new_line)
                modified = True
                found = True
            else:
                new_source.append(line)
        
        if modified:
            cell['source'] = new_source

if found:
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print("Notebook updated successfully.")
else:
    print("Target import line not found in notebook.")
