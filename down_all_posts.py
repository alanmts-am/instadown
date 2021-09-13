from src.posts import  get_all_posts
from utils.create import create_directory

PROFILES_FILE = 'profiles.txt'

with open(PROFILES_FILE, 'r') as file:
    line_itens = file.readlines()
    
for line_item in line_itens:
    line_list = line_item.split(';')
        
    create_directory(line_list[0])
    get_all_posts(line_list[0], line_list[0])
    