from astroquery.jplhorizons import Horizons
from datetime import datetime, timedelta, date
from PIL import Image, ImageDraw
import numpy as np

### USER SETTINGS/ ###

# Options
drawTrails = True

# Paths
outputPath = r"/home/daraghhollman/.config/hypr/wallpaper.jpg"
idPath = r"/home/daraghhollman/Main/horizons-wallpaper/IDs.txt"

# Orbit Parameters
orbitCenter = "500@10" # "500@10" for Heliocentric, "500@3" for geocentric, "500@4" mars etc...
scaleFactor = 10
trailLength = 100 # days

# Colours
backgroundColour = '#EDEFEC'
trailColour = "#D3D8D0"

# Features to be added: scale markers, multiple scale functions, dark mode, colour variables

### /USER SETTINGS ###

today = str(date.today())

def main():
    ids, names, colours, isLabelled = ReadIDList(idPath)

    bodies = []
    for id in ids:
        print(f"\rProcessing ID: {id}")
        
        if id.isnumeric(): id = int(id)
        else: id = str(id)

        bodies.append(GetPosition(id, orbitCenter, today))

    print("Drawing bodies...")
    DrawImage(bodies, names, colours, isLabelled, scale=scaleFactor)

def ReadIDList(path):
    ids, names, colours, isLabelled_str = np.loadtxt(path, unpack=True, dtype={'names': ('ID', 'Name', 'Colour', 'isLabelled'), "formats": ('|S15', '|S15', '|S15', '|S15')}, delimiter=";")
    ids = [str(id)[2:-1] for id in ids]
    
    isLabelled = []
    for el in isLabelled_str:
        el = str(el)[2:-1]

        if el == "True":
            el = True
        elif el == "False":
            el = False
        isLabelled.append(el)
    return (ids, names, colours, isLabelled)

def Previous(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    previous_date = date - timedelta(days=trailLength)
    return previous_date.strftime('%Y-%m-%d')

def GetPosition(id, centre, date):

    body = Horizons(id=id, location=centre, epochs={'start':Previous(date), 'stop':date, 'step':'12h'})

    bodyVectors = body.vectors()

    currentVector = bodyVectors[-1]
    name = currentVector["targetname"]

    currentPosition = [currentVector["x"], -currentVector["y"], currentVector["z"]]

    pastPositions = []
    for vector in bodyVectors:
        position = [vector["x"], -vector["y"], vector["z"]]

        pastPositions.append(position)

    bodyDict = {
        "id": id,
        "name": name,
        "position": currentPosition,
        "trail": pastPositions
    }

    return bodyDict

def DrawImage(bodies, names, colours, islabelled, scale=1, drawTrails=drawTrails):
    image = Image.new('RGB', (1920, 1080), color=backgroundColour)

    centerX, centerY = image.size[0] // 2, image.size[1] // 2

    draw = ImageDraw.Draw(image)

    radius = 3
    textOffsetX = 0
    textOffsetY = -15

    divider = 50

    pixelCoords = []
    trailCoords = []

    for body in bodies:
        newScale = scale * 10**-((np.sqrt(body["position"][0]**2 + body["position"][1]**2)-divider)/divider)
        pixelCoords.append([centerX + body["position"][0]*newScale, centerY + body["position"][1]*newScale])

        trailPositions = [] 
        for pastPosition in body["trail"]:         
            trailPositions.append([centerX + pastPosition[0]*newScale, centerY + pastPosition[1]*newScale])

        trailCoords.append(trailPositions)

    print("Locations found")

    for trailPoints in trailCoords:
        if drawTrails:
            trailSize = radius/1.5

            trailPoints.reverse()

            for pastPoint in trailPoints:
                x, y = pastPoint
                draw.ellipse((x - trailSize, y - trailSize, x + trailSize, y + trailSize), fill=trailColour, outline=trailColour)
                
                trailSize -= radius/(1.5*len(trailPoints))

    for point, colour in zip(pixelCoords, colours):
        colour = f"#{str(colour)[2:-1]}"

        x, y = point
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=colour, outline=colour)

    for point, name, colour, label in zip(pixelCoords, names, colours, islabelled):
        colour = f"#{str(colour)[2:-1]}"
        
        x, y = point

        if label: draw.text((x + textOffsetX, y + textOffsetY), name, fill=colour)

    image.save(outputPath)
    print("Image Saved")

if __name__ == "__main__":
    main()