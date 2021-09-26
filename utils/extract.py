import os
from datetime import datetime as dtclass
import datetime as dtpack

def extract_data(data):
    return dtclass.strptime(data, '%d/%m/%Y')

def increase_data_days(data, days_):
    return dtclass.strptime(data, '%d/%m/%Y') + dtpack.timedelta(days = days_)

def extract_posts_only(folder, user):
    items = os.listdir(folder)
    for item in items:
        if (item.endswith(".xz") or item.endswith(".txt")):
            print("Apagando... " + item)
            os.system("del " + folder + "\\" + item)
        elif not item.startswith(user):
            print("Renomeando... " + item)
            os.rename(folder + "\\" + item, folder + "\\" + user + "-" + item)