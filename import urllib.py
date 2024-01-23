import urllib.request
import json

def getHTML():
    url = urllib.request.urlopen('https://www.linkedin.com/feed/')
    print (url.getcode())
    data = url.read()
    print(data)

def EarthQuakeTracker(data):
    urldata = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson'
    theJSON = json.load(data)
