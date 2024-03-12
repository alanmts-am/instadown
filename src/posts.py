import os
from datetime import datetime

import instaloader
from utils.extract import extract_posts_only


def get_data_posts(user, since, until):
    try:
        print(f'''[{datetime.now()}] Buscando por {user}...''')
        L = instaloader.Instaloader()
        posts = instaloader.Profile.from_username(L.context, user).get_posts()
        
        print(f'''[{datetime.now()}] Baixando...''')
        for post in posts:
            if (post.date >= since) and (post.date <= until):
                L.download_post(post, user)
            elif post.date < since: 
                break
            
        extract_posts_only(user)
    except:
        print("Usuário " + user + " não encontrado ou não contem posts para data informada")
        pass

def get_all_posts(user):
    try:
        print(f'''[{datetime.now}] Buscando por {user}...''')
        L = instaloader.Instaloader()
        posts = instaloader.Profile.from_username(L.context, user).get_posts()

        print(f'''[{datetime.now}] Baixando...''')
        for post in posts:
            L.download_post(post, '.')
            extract_posts_only(user)
    except:
        print("Usuário " + user + " não encontrado ou não contem posts para data informada")
        pass

def count_posts():
    x = 0
    items = os.listdir()
    for items in range(0, len(items)):
        x += 1
    return x
