from src.posts import  get_all_posts
from utils.create import create_directory

PROFILES_FILE = 'profiles.txt'

with open(PROFILES_FILE, 'r') as file:
    line_itens = file.readline().split(';')

    create_directory(line_itens[0])
    get_all_posts(line_itens[0], line_itens[0])
    