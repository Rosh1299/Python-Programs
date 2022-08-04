from pathlib import Path
import json


"""
The json.load() function is used to load JSON file, whereas json.loads() function is used to load string.
The json.dump() function is used when we want to serialize the Python objects into JSON file and
json.dumps() function is used to convert JSON data as a string for parsing and printing.
"""
"""To write data into json file"""
movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Furious 7", "year": 2014}
]

# data = json.dumps(movies)
# Path("movies.json").write_text(data)
# print(type(data))

with open("movies.json", "w") as write_file:
    json.dump(movies, write_file)

"""To read data from json file"""

# data = Path("movies.json").read_text()
# movies = json.loads(data)

# print(movies)
# print(type(movies))

# with open("movies.json", "r") as read_file:
#     b = json.load(read_file)
# print(b, "\n", type(b))
