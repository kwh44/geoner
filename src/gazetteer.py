import requests

geonames = {"api": "http://api.geonames.org/searchJSON?q=",
            "format": "&maxRows=10&username=kwh44"}

gisgraphy = {"api": "https://services.gisgraphy.com/fulltext/fulltextsearch?q=",
             "format": "&format=json"}

url = ""

response = requests.get(url)

data = response.json()
