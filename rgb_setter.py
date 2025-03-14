from openrgb import OpenRGBClient
from openrgb.utils import RGBColor


def set_rgb(**kwargs):
    '''
    Sets the RGB color to use depending on the given input

    returns: None
    '''
    cli = OpenRGBClient()
    for device in cli.devices:
        # print(device)
        cli.devices[device.id].set_color(RGBColor(kwargs[0], kwargs[1], kwargs[2]))
set_rgb((255, 0, 255))
