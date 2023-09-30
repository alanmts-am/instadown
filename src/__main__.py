import argparse
from datetime import datetime
import os
import sys

from utils.create import create_directory
from utils.extract import extract_data, increase_data_days
from utils.move import move_dirs

from src.posts import get_all_posts, get_data_posts

def download_all_posts_from_file(profiles_file, target_dir):
    with open(profiles_file, 'r') as file:
        line_itens = file.readlines()
    
    create_directory(target_dir)
    os.chdir(target_dir)
    for line_item in line_itens:
        line_item = line_item.replace('\n', '')
        get_all_posts(line_item, line_item)
        move_dirs(line_item, target_dir)

def download_all_posts_from_profile(profile, target_dir):
    create_directory(target_dir)
    os.chdir(target_dir)
    get_all_posts(profile)

def download_post_by_date_from_file(profiles_file, initial_date, final_date, target_dir):
    SINCE = extract_data(initial_date)
    UNTIL = increase_data_days(final_date, 1)
    
    with open(profiles_file, 'r') as file:
        line_itens = file.readlines()
        
    create_directory(target_dir)
    os.chdir(target_dir)
    for line_item in line_itens:
        line_item = line_item.replace('\n', '')
        get_data_posts(line_item, SINCE, UNTIL)

def download_post_by_date_from_profile(profiles_name, initial_date, final_date, target_dir):
    SINCE = extract_data(initial_date)
    UNTIL = increase_data_days(final_date, 1)

    create_directory(target_dir)
    os.chdir(target_dir)
    get_data_posts(profiles_name, SINCE, UNTIL)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--post', action='store_true', dest='post', default=None, help='Indicativo de download dos posts')
    parser.add_argument('--idate', action='store', dest='initial_date', default=None, help='Insira a data inicial dos downloads')
    parser.add_argument('--fdate', action='store', dest='final_date', default=None, help='Insira a data final dos downloads')
    parser.add_argument('--today', action='store_true', dest='today', default=None, help='Indicativo de data atual para o idate e fdate')
    parser.add_argument('--profile', action='store', dest='profile', default=None, help='Insira user específico do download')
    parser.add_argument('--profile-file', action='store', dest='profile_file', default='profiles.txt', help='Insira o caminho e tipo do arquivo de profiles')
    parser.add_argument('--download-dir', action='store', dest='download_dir', default='files', help='Insira o caminho da pasta de download padrão')
    args = parser.parse_args()

    if (not args.post):
        print('É necessário pelo menos a indicação de um dos comandos --post ou --story\n\nUtilize o argumento --help para verificar a forma correta')
        sys.exit()

    elif args.post: # post section
        if args.profile is None: # No profile, just from file
            if(args.today and (args.initial_date is None and args.final_date is None)):
                today = datetime.today().strftime('%d/%m/%Y')
                download_post_by_date_from_file(args.profile_file, today, today, args.download_dir)
            
            elif (args.initial_date is None and args.final_date is None):
                download_all_posts_from_file(args.profile_file, args.download_dir)

            elif (args.initial_date != None and args.final_date != None):
                download_post_by_date_from_file(args.profile_file, args.initial_date, args.final_date, args.download_dir)

            else:
                print('Argumentos utilizados incorretamente\n\nUtilize o argumento --help para verificar a forma correta')
                sys.exit()

        elif args.profile != None: # profile found
            if(args.today and (args.initial_date is None and args.final_date is None)):
                today = datetime.today().strftime('%d/%m/%Y')
                download_post_by_date_from_profile(args.profile, today, today, args.download_dir)

            elif (args.initial_date is None and args.final_date is None):
                download_all_posts_from_profile(args.profile, args.download_dir)

            elif (args.initial_date != None and args.final_date != None):
                download_post_by_date_from_profile(args.profile, args.initial_date, args.final_date, args.download_dir)

            else:
                print('Argumentos utilizados incorretamente\n\nUtilize o argumento --help para verificar a forma correta')
                sys.exit()

if __name__ == '__main__':
    main()
