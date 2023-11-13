import os
import mymodule.Pre_processing.index_doc
from time import sleep
directory = '/uploads'  # Replace with the path to your directory

for filename in os.listdir(directory):
    if filename.endswith('.txt'):  # Replace '.txt' with the desired file extension
        file_path = os.path.join(directory, filename)
        index_doc(file_path)
        print("added" + file_path)
        sleep(0.5)
