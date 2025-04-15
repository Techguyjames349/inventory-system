# Combines prompt.md and all history_*.md files in reverse chronological order for provisioning or /info route.
import os
import glob
import re

docs_dir = os.path.dirname(__file__)
prompt_file = os.path.join(docs_dir, 'prompt.md')
history_files = glob.glob(os.path.join(docs_dir, 'history_*.md'))

# Sort history files by date in filename (reverse order: newest first)
def sort_history_files(files):
    def extract_date(filename):
        match = re.search(r'history_(\d{4}-\d{2}-\d{2})\.md', filename)
        return match.group(1) if match else '0000-00-00'  # Fallback for invalid names
    return sorted(files, key=extract_date, reverse=True)

def combine_docs():
    output = []
    # Add prompt
    try:
        with open(prompt_file, 'r', encoding='utf-8') as f:
            output.append(f.read())
    except Exception as e:
        output.append(f"Error reading {prompt_file}: {str(e)}")
    # Add history files in reverse chronological order
    sorted_files = sort_history_files(history_files)
    for history_file in sorted_files:
        try:
            with open(history_file, 'r', encoding='utf-8') as f:
                output.append(f.read())
            print(f"Combined: {history_file}")  # Debug log
        except Exception as e:
            output.append(f"Error reading {history_file}: {str(e)}")
    return '\n\n'.join(output)

if __name__ == '__main__':
    print(combine_docs())