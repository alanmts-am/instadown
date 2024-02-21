import os
from datetime import datetime as dtclass
import datetime as dtpack

def extract_data(data):
    return dtclass.strptime(data, '%Y-%m-%d')

def increase_data_days(data, days_):
    return dtclass.strptime(data, '%Y-%m-%d') + dtpack.timedelta(days = days_)

def extract_posts_only():
    items = os.listdir()
    for item in items:
        if (item.endswith(".xz") or item.endswith(".txt")):
            print("Apagando... " + item)
            os.remove(item)