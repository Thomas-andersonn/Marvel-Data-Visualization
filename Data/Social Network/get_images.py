import json
import os

details_file = open("superhero_details.txt")

details_json = json.loads(details_file.read())

for hero in details_json.keys():
  details = details_json[hero]
  if "image" in details and "url" in details["image"]:
    image_url = details["image"]["url"]
    print("fetching: " + image_url)
    os.system("wget -O images/" + hero+ ".png" + image_url)

    
