# Horizons Wallpaper
A python script to pull and plot a wallpaper of orbital information from specified objects in the solar system.

![wallpaper](https://user-images.githubusercontent.com/62439417/233806907-58c472f5-9361-4ab3-ae54-fb695b09cb1b.jpg)

This script queries the API of (NASA JPL's Horizons System)[https://ssd.jpl.nasa.gov/horizons/] to obtain orbital positions in cartesian coorinates. These are then drawn to an image and saved as a png or jpg to a path of your chosing.

## Features
- Real and Live Oribts
- Trails of past positions with variable length
- Labels
- Non-linear scaling to see more distant bodies (for fans of Pluto :) )
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
