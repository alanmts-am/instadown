import os

def extract_data(data):
    return data.split("/")

def extract_posts_only(folder, user):
    items = os.listdir(folder)
    for item in items:
        if (item.endswith(".xz") or item.endswith(".txt")):
            print("Apagando... " + item)
            os.system("del " + folder + "\\" + item)
        elif not item.startswith(user):
            print("Renomeando... " + item)
            os.rename(folder + "\\" + item, folder + "\\" + user + "-" + item)