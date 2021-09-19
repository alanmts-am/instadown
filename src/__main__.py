import argparse
import sys
from datetime import datetime

import dotenv

from src.posts import get_all_posts, get_data_posts
from utils.create import create_directory
from utils.extract import extract_data
from utils.move import move_dirs

PROFILES_FILE = 'profiles.txt'
FILE_DIR = 'files'

def download_all_posts_from_file(profiles_file, target_dir):
    with open(profiles_file, 'r') as file:
        line_itens = file.readlines()
    
    for line_item in line_itens:
        line_item_list = line_item.split(';')

        create_directory(line_item_list[0])
        get_all_posts(line_item_list[0], line_item_list[0])
        move_dirs(line_item_list[0], target_dir)

def download_all_posts_from_profile(profile, target_dir):
    create_directory(profile)
    get_all_posts(profile, profile)
    move_dirs(profile, target_dir)

def download_post_by_date_from_file(profiles_file, initial_date, final_date, target_dir):
    listInitial = extract_data(initial_date)
    listFinal = extract_data(final_date)
    SINCE = datetime(int(listInitial[2]), int(listInitial[1]), int(listInitial[0]))
    UNTIL = datetime(int(listFinal[2]), int(listFinal[1]), int(listFinal[0]))
    
    with open(profiles_file, 'r') as file:
        line_itens = file.readlines()
        
    create_directory(target_dir)
    for line_item in line_itens:
        line_item_list = line_item.split(';')
    
        create_directory(line_item_list[0])
        get_data_posts(line_item_list[0], line_item_list[0], SINCE, UNTIL)
        move_dirs(line_item_list[0], target_dir)

def download_post_by_date_from_profile(profiles_name, initial_date, final_date, target_dir):
    listInitial = extract_data(initial_date)
    listFinal = extract_data(final_date)
    SINCE = datetime(int(listInitial[2]), int(listInitial[1]), int(listInitial[0]))
    UNTIL = datetime(int(listFinal[2]), int(listFinal[1]), int(listFinal[0]))

    create_directory(profiles_name)
    create_directory(target_dir)
    get_data_posts(profiles_name, profiles_name, SINCE, UNTIL)
    move_dirs(profiles_name, target_dir)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--post', action='store_true', dest='post', default=None, help='Indicativo de download dos posts')
    parser.add_argument('--story', action='store_true', dest='story', default=None, help='Indicativo de download dos stories')
    parser.add_argument('-u', '--user', action='store', dest='username', default=None, help='Insira o seu usuário')
    parser.add_argument('-p', '--pass', action='store', dest='password', default=None, help='Insira a sua senha')
    parser.add_argument('-id', '--idate', action='store', dest='initial_date', default=None, help='Insira a data inicial dos downloads')
    parser.add_argument('-fd', '--fdate', action='store', dest='final_date', default=None, help='Insira a data final dos downloads')
    parser.add_argument('-prof', '--profile', action='store', dest='profile', default=None, help='Insira user específico do download')
    args = parser.parse_args()

    if (not args.post and not args.story):
        print('É necessário pelo menos a indicação de um dos comandos --post ou --story\n')
        parser.print_usage()
        sys.exit()

    if args.post and not args.story: # post section
        if args.profile is None: # No profile, just from file
            if (args.initial_date is None and args.final_date is None):
                download_all_posts_from_file(PROFILES_FILE, FILE_DIR)

            elif (args.initial_date != None and args.final_date != None):
                download_post_by_date_from_file(PROFILES_FILE, args.initial_date, args.final_date, FILE_DIR)

        elif args.profile != None: # profile found
            if (args.initial_date is None and args.final_date is None):
                download_all_posts_from_profile(args.profile, FILE_DIR)

            elif (args.initial_date != None and args.final_date != None):
                download_post_by_date_from_profile(args.profile, args.initial_date, args.final_date, FILE_DIR)

if __name__ == '__main__':
    main()