import os

def create_directory(path):
    if os.path.exists(path):
        return
    else: 
        os.makedirs(path)