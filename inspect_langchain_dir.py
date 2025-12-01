import os
import langchain
import langchain.chains

package_path = os.path.dirname(langchain.__file__)
chains_path = os.path.join(package_path, 'chains')

print(f"LangChain path: {package_path}")
print(f"Chains path: {chains_path}")

if os.path.exists(chains_path):
    print("Contents of langchain/chains:")
    for item in os.listdir(chains_path):
        print(item)
else:
    print("langchain/chains directory not found")
