from instagrapi import Client
import os

def authenticate():
    cl = Client()
    username = "stoicstreetcats"
    password = os.getenv("SSC_PW")
    cl.login(username, password)
    return cl



def post_photo(cl, photo_path, caption):
    post = cl.photo_upload(photo_path, caption)
    print("Posted photo with ID:", post.dict()["id"])



if __name__ == "__main__":
    print("Logging in")
    try:
        client = authenticate()
        print("Authentification successfull")
    except:
        print("Authentification failed")
    print("\n—Posting")

    photo_path = "img/2.png"
    caption = "Quote"
    try:
        post_photo(client,photo_path,caption)
        print("posting success")
    except Exception as e:
        print("failed posting\n", str(e))
    finally:
        print("^_^")

