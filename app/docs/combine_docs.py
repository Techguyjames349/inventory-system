# Combines prompt.md and history.md into a single plaintext output for provisioning or /info route.
import os

docs_dir = os.path.dirname(__file__)
prompt_file = os.path.join(docs_dir, 'prompt.md')
history_file = os.path.join(docs_dir, 'history.md')

def combine_docs():
    output = []
    for file_path in [prompt_file, history_file]:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                output.append(f.read())
        except Exception as e:
            print(f"Error reading {file_path}: {str(e)}")
    return '\n\n'.join(output)

if __name__ == '__main__':
    print(combine_docs())