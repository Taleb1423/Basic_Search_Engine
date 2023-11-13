import re
from api.mymodule.elastic import client
import os
def index_doc(file):
    doc = {}
    key = None

    path = os.path.join(os.getcwd(),"uploads",file)

    # Read the text file line by line
    with open(path, 'r') as file:
        for line in file:
            # Check if the line starts with a number followed by a period
            if re.match(r'\d+\.', line):
                # This is a section or subsection header
                # Remove the number and period from the header
                key = re.sub(r'\d+\.\s*', '', line).strip()
                doc[key] = ''
            elif key:
                # This is the content of the current section or subsection
                doc[key] += line.strip()
        s =client.index(index='courses',document=doc)
        return s["_id"]

