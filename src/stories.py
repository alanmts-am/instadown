from utils.extract import extract_posts_only
import instaloader

def get_stories(user, password, profile_name):
    L = instaloader.Instaloader()
    L.login(user, password)
    profile = instaloader.Profile.from_username(L.context, username=profile_name)
    L.download_stories(userids=[profile.userid], filename_target=profile_name)

    extract_posts_only(profile_name, profile_name)