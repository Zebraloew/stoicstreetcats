from textwrap import wrap
from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image

typeface = "JetBrainsMono Nerd Font Propo"
fontsize = 60
fontweight = 900
color = "BLACK"
outline_color = "WHITE"
outline_width = 10  # You can adjust this value based on how thick you want the outline to be

# horizontal text alignment
centered_text = False
bottom_text = True


def word_wrap(image, ctx, text, roi_width, roi_height):
    """Break long text to multiple lines, and reduce point size
    until all text fits within a bounding box."""
    mutable_message = text
    iteration_attempts = 100

    def eval_metrics(txt):
        """Quick helper function to calculate width/height of text."""
        metrics = ctx.get_font_metrics(image, txt, True)
        return (metrics.text_width, metrics.text_height)

    while ctx.font_size > 0 and iteration_attempts:
        iteration_attempts -= 1
        width, height = eval_metrics(mutable_message)
        if height > roi_height:
            ctx.font_size -= 0.75  # Reduce pointsize
            mutable_message = text  # Restore original text
        elif width > roi_width:
            columns = len(mutable_message)
            while columns > 0:
                columns -= 1
                mutable_message = '\n'.join(wrap(mutable_message, columns))
                wrapped_width, _ = eval_metrics(mutable_message)
                if wrapped_width <= roi_width:
                    break
            if columns < 1:
                ctx.font_size -= 0.75  # Reduce pointsize
                mutable_message = text  # Restore original text
        else:
            break
    if iteration_attempts < 1:
        raise RuntimeError("Unable to calculate word_wrap for " + text)
    return mutable_message


message = "Claws sharp, eyes keen. In chaos, find calm. Stand alone, remain strong. This is street wisdom"
with Image(filename='img/6.webp') as img:
    with Drawing() as ctx:
        ctx.fill_color = Color(color)
        ctx.font_family = typeface
        ctx.font_weight = fontweight
        ctx.font_size = fontsize
        ctx.stroke_color = Color(outline_color)
        ctx.stroke_width = outline_width
        
        mutable_message = word_wrap(img, ctx, message, img.width - 10, img.height - 10)
        
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
        img.save(filename='centered-text.png')
