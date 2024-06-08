import os
import shutil

# Read the .gitignore file
with open('.gitignore', 'r') as f:
    lines = f.readlines()

# Create a temporary directory
os.makedirs('temp', exist_ok=True)

# Iterate over each line in the .gitignore file
for line in lines:
    # Remove newline characters
    line = line.strip()

    # If the line is not empty and does not start with a '#'
    if line and not line.startswith('#'):
        # If the line ends with a '/', it is a directory
        if line.endswith('/'):
            # Copy the directory and its contents to the temporary directory
            shutil.copytree(line[:-1], 'temp/' + line[:-1])
        else:
            # Copy the file to the temporary directory
            shutil.copy(line, 'temp/' + line)

# Now, you can use 'temp' as the rootFolderOrFile in the ArchiveFiles@2 task
# This will only include the files and directories that are not listed in the .gitignore file
