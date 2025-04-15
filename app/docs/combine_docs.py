# Combines prompt.md and all history_*.md files into a single plaintext output for provisioning or /info route.
import os
import glob

docs_dir = os.path.dirname(__file__)
prompt_file = os.path.join(docs_dir, 'prompt.md')
history_files = sorted(glob.glob(os.path.join(docs_dir, 'history_*.md')))

def combine_docs():
    output = []
    # Add prompt
    try:
        with open(prompt_file, 'r', encoding='utf-8') as f:
            output.append(f.read())
    except Exception as e:
        output.append(f"Error reading {prompt_file}: {str(e)}")
    # Add history files in chronological order
    for history_file in history_files:
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                output.append(f.read())
        except Exception as e:
            output.append(f"Error reading {history_file}: {str(e)}")
    return '\n\n'.join(output)

if __name__ == '__main__':
    print(combine_docs())