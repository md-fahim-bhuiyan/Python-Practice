# Create a new file and write to it
with open('New.txt', 'w') as f:
    f.write('This is some content that we are writing to the file.')

# Read the contents of the file
with open('New.txt', 'r') as f:
    content = f.read()
    print('File Contents:')
    print(content)

# Append more content to the file
with open('New.txt', 'a') as f:
    f.write('\nThis is some additional content.')

# Read the updated contents of the file
with open('New.txt', 'r') as f:
    updated_content = f.read()
    print('Updated File Contents:')
    print(updated_content)
