from instagrapi import Client
import os #for local variable
import shutil #for moving files locally

def authenticate():
    cl = Client()
    username = "stoicstreetcats"
    password = os.getenv("SSC_PW")
    cl.login(username, password)
    return cl



def post_photo(cl, photo_path, caption):
    post = cl.photo_upload(photo_path, caption)
    print("Posted photo with ID:", post.dict()["id"])


def move_posted_photo(source_path):
    # Define the target path
    target_path = os.path.join('img/posted', os.path.basename(source_path))
    # Move the file
    shutil.move(source_path, target_path)
    print(f"Moved photo to {target_path}")


def post(photo_path = "img/2.png", caption = ""):
    logbook = "Posting \n"
    print("Logging in")
    try:
        client = authenticate()
        print("Authentification successfull")
    except:
        print("Authentification failed")
    print("\n—Posting")
    
    try:
        post_photo(client,photo_path,caption)
        print("posting success")
    except Exception as e:
        print("failed posting\n", str(e))
    finally:
        print("^_^")

    try:
        move_posted_photo(photo_path)
        print(f"Moved {photo_path} to posted")
    except Exception as e:
        print(f"Failed moving\n",str(e))
    
    return logbook

if __name__ == "__main__":
    post("centered-text_LP4lnBVZPu.png")
        

