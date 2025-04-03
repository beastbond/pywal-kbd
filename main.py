import os
import time
import argparse
# import colorsys | TODO: Add the ability to accept HSV values
from get_wallpaper_path import get_wallpaper_path
from dominant_color import get_dominant_color

try:
    from openrgb import OpenRGBClient
    from openrgb.utils import RGBColor
    OPENRGB_AVAILABLE = True
except ImportError:
    OPENRGB_AVAILABLE = False
   
def set_rgb_lighting(color, device_name="None"):
    """
    set RGB lighting using Open
    """
    if not OPENRGB_AVAILABLE:
        print("the OpenRGB python module is not installed, please install using: pip install openrgb-python")
        return False
    try:
        client = OpenRGBClient()
        
        if device_name:
                
            devices = [dev for dev in client.devices if device_name.lower() in dev.name.lower()]
            if not devices:
                print(f"No device found with name containing '{device_name}'. Available devices:")
                for dev in client.devices:
                        print(f" - {dev.name}")
                return False
            device = devices[0]
            rgb_color = RGBColor(*color)
            device.set_color(rgb_color)
        else:
            #Use the first device by default
            device = client.devices[0]

        rgb_color = RGBColor(*color)
        device.set_color(rgb_color)
        print(f"Set {device.name} to RGB Color: {color}")
        return True
    except Exception as e:
        print(f"Error setting RGB Color: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Set RGB lighting based on the wallpaper's document color")
    parser.add_argument('--device', help="Name of device to control")
    parser.add_argument('--wallpaper', help="Path of to wallpaper image (default: detect current)")
    args = parser.parse_args()

    wallpaper_path = args.wallpaper if args.wallpaper else get_wallpaper_path()
    if not wallpaper_path or not os.path.exists(wallpaper_path):
        print("Could not find wallpaper image")
        return

    color = get_dominant_color(wallpaper_path)
    if not color:
        print("Could not determine dominant color")
        return

    print(f"Dominant color (RGB): {color}")
    
    print(f"Analyzing wallpaper: {wallpaper_path}")
    time.sleep(1)

    if not set_rgb_lighting(color, args.device):
        print("\nThis Script will set the RGB color based on the wallpaper or image in question if you:")
        print("1. Install OpenRGB (https://openrgb.org/)")
        print("2. Run the OpenRGB Server in the background")
        print("3. Install openrgb-python module: pip install openrgb-python")
        print("\nHere's the RGB values you can manually set:")
        print(f"R: {color[0]}, G: {color[1]}, B: {color[2]}")

if __name__ == "__main__":
    main()
