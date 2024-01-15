import glob
import re

# Step 1: Look in the markdown files in the current folder
for md_file in glob.glob('*.md'):
    print(f"Processing file: {md_file}")
    with open(md_file, 'r') as file:
        filedata = file.read()

    # Step 2: Find and replace the image reference format
    pattern = r'!\[\[(.*?)\]\]'
    matches = re.findall(pattern, filedata)
    for match in matches:
        print(f"Found image reference: {match}")
        new_format = f"![{match}](./{match})"
        print(f"Replacing with: {new_format}")
        filedata = filedata.replace(f'![[{match}]]', new_format)

    # Step 3: Write the changes back to the file
    with open(md_file, 'w') as file:
        print(f"Writing changes to file: {md_file}")
        file.write(filedata)