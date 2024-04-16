# generate image
# generate text
# place text on image
# post image
# repeat after a while
from imagegen import imagegen
from generate_quote import generate_quote

def instapost():
    imagegen("cuddlecats")
    quote = generate_quote()
    print(quote)
instapost()