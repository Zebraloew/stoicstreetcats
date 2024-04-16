# generate image
# generate text
# place text on image
# post image
# repeat after a while
from imagegen import imagegen
from generate_quote import generate_quote
from add_quote import add_quote
from post import post

def instapost():
    image = imagegen()
    print("Processing ", image)
    quote = generate_quote()
    print("Adding ", quote)
    combinate = add_quote(image, quote)
    posting = post(combinate, quote)

if __name__ == "__main__":
    instapost()