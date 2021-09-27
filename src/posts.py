import os

import instaloader
from utils.create import create_directory
from utils.extract import extract_posts_only


def get_data_posts(user, folder, since, until):
    try:
        L = instaloader.Instaloader()
        posts = instaloader.Profile.from_username(L.context, user).get_posts()
        create_directory(user)
        for post in posts:
            if (post.date >= since) and (post.date <= until):
                print("Baixando... ")
                L.download_post(post, user)
                extract_posts_only(folder, user)
                print("\nArquivos até aqui de " + user + ": " + str(count_posts(folder)) + "\n")
            elif post.date < since: 
                break
            
        print("\nArquivos totais de " + user + ": " + str(count_posts(folder)) + "\n")
    except:
        print("Usuário " + user + " não encontrado")
        pass

def get_all_posts(user, folder):
    try:
        L = instaloader.Instaloader()
        posts = instaloader.Profile.from_username(L.context, user).get_posts()
        create_directory(user)
        for post in posts:
            print("Baixando... ")
            L.download_post(post, user)
            extract_posts_only(folder, user)
            print("\nArquivos até aqui de " + user + ": " + str(count_posts(folder)) + "\n")

        print("\nArquivos totais de " + user + ": " + str(count_posts(folder)) + "\n")
    except:
        print("Usuário " + user + " não encontrado")
        pass

def count_posts(folder):
    x = 0
    items = os.listdir(folder)
    for items in range(0, len(items)):
        x += 1
    return x
