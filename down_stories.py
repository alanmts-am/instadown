import os
from utils.args import import_variables
from src.stories import get_stories

args = import_variables()

USER = args.username
PASSWORD = args.password
PROFILES_FILE = 'profiles.txt'

with open(PROFILES_FILE, 'r') as file:
    line_itens = file.readline().split(';')

    get_stories(USER, PASSWORD, line_itens[0])

