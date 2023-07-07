import os

from templateframework.metadata import Metadata

def run(metadata: Metadata = None):
    print("Hello from script.py!")
    dir = "./{{project_name}}"       
    os.makedirs(dir)
    return metadata