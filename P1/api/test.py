import json

from mymodule.elastic import client
file = open("P1/api/udemy_courses.json")
data = json.load(file)
file.close()
for course in data:
    client.index(index='courses',document=course)