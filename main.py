import click
import dominant_color
import rgb_setter
import os

@click.command()
@click.argument('image', type=click.Path(exists=True), required=True)
@click.option('-r', '--rgb', is_flag=True, help='Set the rgb to the dominant color in the wallpaper.')
@click.option('-o', '--output', is_flag=True, help='Outputs the color to stdout.')
@click.option('-v', '--verbose', is_flag=True, help='Outputs the color to stdout.')

def set_wallpaper_rgb(image, rgb, output, verbose):
    '''
    Set the rgb to the dominant color in the wallpaper and the wallpaper itself
    if no option is passed.

    :param image: The image to get the dominant color from.
    :param rgb: Set the rgb to the dominant color in the wallpaper.
    :param output: Outputs the color to stdout.

    It will call different functions depending on the Operating system.
    '''
    image = os.path.open(image) 
    color = dominant_color.get_dominant_color(image)
    if rgb:
        print(color)
        rgb_setter.set_rgb(color)
    if output:
        click.echo(f'Color: {dominant_color}')
    if verbose:
        click.echo(verbose)
