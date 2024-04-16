from word_wrap import word_wrap
from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image
from random10 import generate_random_sequence as random10

message = "Claws sharp, eyes keen. In chaos, find calm. Stand alone, remain strong. This is street wisdom"

def add_quote(image="img/6.webp", quote=message):

    typeface = "JetBrainsMono Nerd Font Propo"
    fontsize = 60
    fontweight = 900
    color = "BLACK"
    outline_color = "WHITE"
    outline_width = 10  # You can adjust this value based on how thick you want the outline to be

    # horizontal text alignment
    centered_text = False
    bottom_text = True


    with Image(filename=image) as img:
        with Drawing() as ctx:
            ctx.fill_color   = Color(color)
            ctx.font_family  = typeface
            ctx.font_weight  = fontweight
            ctx.font_size    = fontsize
            ctx.stroke_color = Color(outline_color)
            ctx.stroke_width = outline_width
            
            mutable_message = word_wrap(img, ctx, quote, img.width - 10, img.height - 10)
            
            metrics = ctx.get_font_metrics(img, mutable_message, multiline=True)
            text_width = metrics.text_width
            text_height = metrics.text_height
            
            x = (img.width - text_width) / 2
            if centered_text:
                y = (img.height - text_height) / 2 + metrics.ascender
            if bottom_text:
                y = img.height - text_height - 50

            # outline text
            ctx.text(round(x), round(y), mutable_message)
            # actual text
            ctx.stroke_width = 0
            ctx.text(round(x), round(y), mutable_message)

            ctx.draw(img)
            filename_buffer = "centered-text_" + random10()+ ".png"
            img.save(filename = filename_buffer)
            return filename_buffer
        
if __name__ == "__main__":
    filename = add_quote("img/4.webp","Yo, Cheers!")
    print(filename)