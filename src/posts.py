import os

import instaloader
from utils.extract import extract_posts_only


def get_data_posts(user, since, until):
    try:
        L = instaloader.Instaloader()
        posts = instaloader.Profile.from_username(L.context, user).get_posts()
        
        for post in posts:
            if (post.date >= since) and (post.date <= until):
                print("Baixando... ")
                L.download_post(post, user)
            elif post.date < since: 
                break
            
        os.chdir(user)
        extract_posts_only()
        print("\nArquivos totais de " + user + ": " + str(count_posts()) + "\n")
    except:
        print("Usuário " + user + " não encontrado ou não contem posts para data informada")
        pass

def get_all_posts(user):
    try:
        L = instaloader.Instaloader()
        posts = instaloader.Profile.from_username(L.context, user).get_posts()
        for post in posts:
            print("Baixando... ")
            L.download_post(post, '.')
            extract_posts_only()
            print("\nArquivos até aqui de " + user + ": " + str(count_posts()) + "\n")

        print("\nArquivos totais de " + user + ": " + str(count_posts()) + "\n")
    except:
        print("Usuário " + user + " não encontrado ou não contem posts para data informada")
        pass

def count_posts():
    x = 0
    items = os.listdir()
    for items in range(0, len(items)):
        x += 1
    return x
