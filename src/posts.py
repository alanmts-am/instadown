import os
import instaloader
from utils.extract import extract_posts_only

def get_data_posts(user, folder, since, until):
    L = instaloader.Instaloader()
    posts = instaloader.Profile.from_username(L.context, user).get_posts()

    for post in posts:
        if (post.date >= since) and (post.date <= until):
            print("Baixando... ")
            L.download_post(post, user)
            extract_posts_only(folder, user)
            print("\nArquivos até aqui de " + user + ": " + str(count_posts(folder)) + "\n")
        elif post.date < since: 
            break
    
    print("\nArquivos totais de " + user + ": " + str(count_posts(folder)) + "\n")

def get_all_posts(user, folder):
    L = instaloader.Instaloader()
    posts = instaloader.Profile.from_username(L.context, user).get_posts()

    for post in posts:
        print("Baixando... ")
        L.download_post(post, user)
        extract_posts_only(folder, user)
        print("\nArquivos até aqui de " + user + ": " + str(count_posts(folder)) + "\n")
    
    print("\nArquivos totais de " + user + ": " + str(count_posts(folder)) + "\n")

def count_posts(folder):
    x = 0
    items = os.listdir(folder)
    for items in range(0, len(items)):
        x += 1
    return x