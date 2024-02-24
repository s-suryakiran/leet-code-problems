import re

def count_table_rows(readme_path):
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Assuming a simple table format, counting the number of lines starting with '|'
    row_count = len(re.findall(r'^\|', content, re.MULTILINE)) - 1  # Subtracting header row
    return row_count

def update_readme(readme_path, row_count):
    with open(readme_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the pattern to find the section to update
    pattern = r'(<!-- ROW_COUNT_START -->\n).*(\n<!-- ROW_COUNT_END -->)'
    replacement = r'\1Solved {} leetcode problems.\2'.format(row_count)
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

if __name__ == "__main__":
    readme_path = 'README.md'
    row_count = count_table_rows(readme_path)
    update_readme(readme_path, row_count)
