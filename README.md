# Horizons Wallpaper
A python script to pull and plot a wallpaper of orbital information from specified objects in the solar system. This script queries the API of [NASA JPL's Horizons System](https://ssd.jpl.nasa.gov/horizons/) to obtain orbital positions in cartesian coorinates. These are then drawn to an image (flattened to the ecliptic) and saved as a png or jpg to a path of your chosing.

![background](https://github.com/daraghhollman/horizons-wallpaper/assets/62439417/3229d214-dc0e-4265-a361-dadf3cea6149)

## Features
- Real and Live Oribts
- Trails of past positions with variable length
- Labels
- Non-linear (and adjustable) scaling to see more distant bodies
- Free choice of colours

## Configuration
Objects can be added/removed from the wallpaper by editing the ID file. It is structured in columns separated by a semicolon:
- ID (from the Horizons database)
- Label Name (of your chosing)
- Colour (Hex without '#', i.e. A0C4DC)
- A boolean for displaying the label (either 'True' or 'False')

## Dependancies
### Python
- pillow
- numpy
- astroquery
- datetime

## How to run
- Setup virtual env (optional)
    ```shell
    python -m venv venv
    ```
    In some Os `python3` works.
- Install dependencies
    ```shell
    pip install -r requirements.txt
    ```
- Set output paths in [horizonsWallpaper.py](horizonsWallpaper.py#L7)
- Run script
    ```shell
    python horizonsWallpaper.py
    ```
    In some Os `python3` works.

## Make it run automatically
### Windows
In this case virtual env is not helpful. Because the script needs to be run as administrator, it is not possible to use the startup folder. Instead, a shortcut to the script needs to be created and set to run as administrator. So **install the dependencies globally** (just run `pip install -r requirements.txt`) and then follow these steps:

- Create a shortcut to the script
- Open the properties of the shortcut
- In the "Shortcut" tab, click "Advanced"
- Check "Run as administrator"
- In the "General" tab, click "Advanced"
- Check "Run as administrator"
- In the "General" tab, click "Change Icon"
- Select an icon of your choice
- Move the shortcut to the startup folder
    - Press Win+R
    - Type "shell:startup"
    - Press Enter
