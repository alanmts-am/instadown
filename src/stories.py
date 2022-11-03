import instaloader
from utils.create import create_directory
from utils.extract import extract_posts_only


def get_stories(user, password, profile_name):
    try:
        L = instaloader.Instaloader()
        L.login(user, password)
        profile = instaloader.Profile.from_username(L.context, username=profile_name)
        L.download_stories(userids=[profile.userid], filename_target='.')

        extract_posts_only()
    except:
        print("Usuário " + user + " não encontrado")
        pass
