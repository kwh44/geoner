import requests
import xml.etree.ElementTree as ET

geonames_api = ["http://api.geonames.org/searchJSON?q=", "&maxRows=10&username=kwh44"]
gisgraphy_api = ["https://services.gisgraphy.com/fulltext/fulltextsearch?q=paris"]

response = requests.get("https://services.gisgraphy.com/fulltext/fulltextsearch?q=london")

print(response.content)
