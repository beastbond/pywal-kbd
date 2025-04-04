def get_wallpaper_path():
    """
    Get the path to the current wallpaper in Windows and returns an Error in case it couldnt find the wallpaper path 
    """
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                           r"Control Panel\Desktop") as key:
            wallpaper = winreg.QueryValueEx(key, "WallPaper")[0]
            return wallpaper
    #TODO: Add Linux support
    except Exception as e:
        print(f"Couldn't get wallpaper path: {e}")
        return None
