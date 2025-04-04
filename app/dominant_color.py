from PIL import Image

def get_dominant_color(image_path, pallette_size=16):
    '''
    Get the dominant color in an image using colorthief
    
    returns: a tuple of rgb values (Color)
    returns None in case of an Error
    '''
    try:
        image = Image.open(image_path)
        image = image.convert('RGB')
        image.thumbnail((100, 100))

        colors = image.getcolors(maxcolors=10000)
        if not colors:
            return None

        colors.sort(key=lambda x: x[0], reverse=True)

        dominant_color = colors[0][1]
        return dominant_color
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

