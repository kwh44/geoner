import time
import grequests

geonames = {"api": "http://api.geonames.org/searchJSON?q=",
            "format": "&maxRows=10&username=kwh44"}

gisgraphy = {"api": "https://services.gisgraphy.com/fulltext/fulltextsearch?q=",
             "format": "&format=json"}

queries = ["Lviv", "Baranivka", "Kyiv", "London", "Zhytomyr"]

urls = [gisgraphy["api"] + i + gisgraphy["format"] for i in queries]

#
s = time.time()
rs = (grequests.get(u) for u in urls)
result = grequests.map(rs)
e = time.time()
print("Lookup time: ", e - s)
for i in result:
    print(i.json())
#response = requests.get(url)

#data = response.json()
#rs = (grequests.get(u) for u in urls)