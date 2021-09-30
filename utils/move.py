import shutil

def move_dirs(source, target):
    try:
        shutil.move(source, target)
    except:
       pass