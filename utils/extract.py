import os
from datetime import datetime as dtclass
import datetime as dtpack

def extract_data(data):
    return dtclass.strptime(data, '%Y-%m-%d')

def increase_data_days(data, days_):
    return dtclass.strptime(data, '%Y-%m-%d') + dtpack.timedelta(days = days_)

def extract_posts_only(profile_dir):
    os.chdir(profile_dir)
    items = os.listdir()
    for item in items:
        if (item.endswith(".xz") or item.endswith(".txt")):
            os.remove(item)
    os.chdir("../")