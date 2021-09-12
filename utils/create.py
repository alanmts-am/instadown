import os

def create_directory(log_directory):
    if os.path.exists(log_directory):
        print("Pasta " + log_directory + " já criada")
    else: 
        os.makedirs(log_directory)