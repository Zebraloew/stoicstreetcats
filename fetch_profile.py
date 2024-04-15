from instagrapi import Client
import os

def authenticate():
    cl = Client()
    username = "stoicstreetcats"
    password = os.getenv("SSC_PW")
    cl.login(username, password)
    return cl

def fetch_profile(cl):
    return cl.user_info(cl.user_id)

if __name__ == "__main__":
    client = authenticate()
    profile_info = fetch_profile(client)
    print("Profile Info:")
    print("Username:", profile_info.username)
    print("Biography:", profile_info.biography)
    print("Followers:", profile_info.follower_count)
    print("Following:", profile_info.following_count)