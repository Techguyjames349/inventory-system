# Combines prompt.md and all history_*.md files in chronological order for provisioning or /info route.
import os
import glob
import re

docs_dir = os.path.dirname(__file__)
prompt_file = os.path.join(docs_dir, 'prompt.md')
history_files = glob.glob(os.path.join(docs_dir, 'history_*.md'))

# Sort history files by date in filename (e.g., history_2025-04-09.md)
def sort_history_files(files):
    def extract_date(filename):
        match = re.search(r'history_(\d{4}-\d{2}-\d{2})\.md', filename)
        return match.group(1) if match else '9999-99-99'  # Fallback for invalid names
    return sorted(files, key=extract_date)

def combine_docs():
    output = []
    # Add prompt
    try:
        with open(prompt_file, 'r', encoding='utf-8') as f:
            output.append(f.read())
    except Exception as e:
        output.append(f"Error reading {prompt_file}: {str(e)}")
    # Add history files in chronological order
    for history_file in sort_history_files(history_files):
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                output.append(f.read())
        except Exception as e:
            output.append(f"Error reading {history_file}: {str(e)}")
    return '\n\n'.join(output)

if __name__ == '__main__':
    print(combine_docs())