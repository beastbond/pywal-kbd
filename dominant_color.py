import colorthief
import os

def get_dominant_color(image):
    '''
    Get the dominant color in an image using colorthief
    
    returns: a tuple of rgb values (Color)
    '''
    image = os.path.abspath(image)
    color_thief = colorthief.ColorThief(image)
    dominant_color = color_thief.get_color(quality=1)
    return dominant_color
