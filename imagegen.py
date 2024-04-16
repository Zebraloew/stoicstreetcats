from openai import OpenAI
from random10 import generate_random_sequence as random10
import requests #safe from web to file

def imagegen(input="Street wildlife: oppossum, raccoon, skunk, squirrel. The animals are depicted engaging in various stoic activities in a quirky, philosophical urban rooftop setting. Roaming the alleys and perched on rooftops, our streetwise cats offer a purr-spective on life through the stoic lens. Discover urban tales and philosophical mewsings from the wisest whiskers in the city. "):
    client = OpenAI()

    print("Generating image")
    response = client.images.generate(
    model="dall-e-3",
    prompt=input,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url
    print("image generated")

    def save_image_from_url(url, filename):
        print("saving to file")
        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open a file in binary write mode and save the content of the response
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Image successfully saved as {filename}")
        else:
            print(f"Failed to download the image. Status code: {response.status_code}")


    url = image_url 
    filename = "downloaded_image____"+random10()+".png"
    save_image_from_url(url, filename)
    return filename

if __name__ == "__main__":
    print(imagegen("catsnest"))
    