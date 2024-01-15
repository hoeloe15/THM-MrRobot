import os
import glob

# Step 1: Get the filenames from the 'attachments' folder
attachments_folder = 'attachments'
filenames = os.listdir(attachments_folder)

# Step 2: Save the filenames and replace spaces with underscores
new_filenames = {}
for filename in filenames:
    new_filename = filename.replace(' ', '_')
    new_filenames[filename] = new_filename
    os.rename(os.path.join(attachments_folder, filename), os.path.join(attachments_folder, new_filename))

# Step 3: Look in the markdown files in the current folder
for md_file in glob.glob('*.md'):
    with open(md_file, 'r') as file:
        filedata = file.read()

    # Step 4: Replace any occurrences of the old filenames with the new filenames
    for old_filename, new_filename in new_filenames.items():
        filedata = filedata.replace(old_filename, new_filename)

    # Step 5: Write the changes back to the file
    with open(md_file, 'w') as file:
        file.write(filedata)