import re
doc = {}
key = None

# Read the text file line by line
with open('document.txt', 'r') as file:
    for line in file:
        # Check if the line starts with a number followed by a period
        if re.match(r'\d+\.', line):
            # This is a section or subsection header
            # Remove the number and period from the header
            key = re.sub(r'\d+\.\s*', '', line).strip()
            doc[key] = ''
        elif key:
            # This is the content of the current section or subsection
            doc[key] += line

# Print the dictionary
print(doc)

