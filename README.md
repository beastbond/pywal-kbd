# Wallpaper RGB Control

A Python script that analyzes your desktop wallpaper, determines the dominant color, and sets it as your RGB lighting color.

## Features

- Detects current wallpaper (Windows)
- Extracts dominant color
- Sets RGB lighting via OpenRGB
- Supports multiple RGB devices

## Installation

1. Install Python 3.x
2. Install dependencies:
```sh
pip install -r requirements.txt
```
3. Install [OpenRGB](https://openrgb.org/) and run it in background
4. Clone the repo
```sh
git clone https://github.com/beastbond/pywal-kbd.git
```

## Usage
 ```sh
  cd app
 python main.py [--device "device_name"] [--wallpaper "path/to/wallpaper.jpg"]
  ```
## Requirements

- Python 3.x
- OpenRGB
- Compatible RGB hardware
