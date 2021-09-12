from utils.create import create_directory
from utils.move import move_posts

PROFILES_FILE = 'profiles.txt'

with open(PROFILES_FILE, 'r') as file:
    line_itens = file.readline().split(';')
    create_directory(line_itens[1])
    move_posts(line_itens[0], line_itens[1])