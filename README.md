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
```pip install -r requirements.txt```
3. Install [OpenRGB](https://openrgb.org/) and run it in background

## Usage
```python wallpaper_rgb.py [--device "device_name"] [--wallpaper "path/to/wallpaper.jpg"]```

## Requirements

- Python 3.x
- OpenRGB
- Compatible RGB hardware
