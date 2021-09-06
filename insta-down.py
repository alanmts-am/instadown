from datetime import datetime
import os
import instaloader

USER = "user"
INITIAL = "03/03/2018"
FINAL = "31/03/2020"

def extractData(data):
    return data.split("/")

def createDirectory(log_directory):
    if os.path.exists(log_directory):
        print("Pasta " + log_directory + " já criada")
    else: 
        os.makedirs(log_directory)

def getDataPosts(user, folder, since, until):
    L = instaloader.Instaloader()
    posts = instaloader.Profile.from_username(L.context, user).get_posts()

    for post in posts:
        if (post.date >= since) and (post.date <= until):
            print("Baixando... ")
            L.download_post(post, user)
            onlyPost(folder, user)
            print("\nArquivos até aqui de " + user + ": " + str(countPosts(folder)) + "\n")
    
    print("\nArquivos totais de " + user + ": " + str(countPosts(folder)) + "\n")

def getAllPosts(user, folder):
    L = instaloader.Instaloader()
    posts = instaloader.Profile.from_username(L.context, user).get_posts()

    for post in posts:
        print("Baixando... ")
        L.download_post(post, user)
        onlyPost(folder, user)
        print("\nArquivos até aqui de " + user + ": " + str(countPosts(folder)) + "\n")
    
    print("\nArquivos totais de " + user + ": " + str(countPosts(folder)) + "\n")

def onlyPost(folder, user):
    items = os.listdir(folder)
    for item in items:
        if (item.endswith(".xz") or item.endswith(".txt")):
            print("Apagando... " + item)
            os.system("del " + folder + "\\" + item)
        elif not item.startswith(user):
            print("Renomeando... " + item)
            os.rename(folder + "\\" + item, folder + "\\" + user + "-" + item)

def countPosts(folder):
    x = 0
    items = os.listdir(folder)
    for items in range(0, len(items)):
        x += 1
    return x

listInitial = extractData(INITIAL)
listFinal = extractData(FINAL)
SINCE = datetime(int(listInitial[2]), int(listInitial[1]), int(listInitial[0]))
UNTIL = datetime(int(listFinal[2]), int(listFinal[1]), int(listFinal[0]))

createDirectory(USER)
getDataPosts(USER, USER, SINCE, UNTIL)
# getAllPosts(USER, FOLDER)