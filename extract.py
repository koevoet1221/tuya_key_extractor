import xml.etree.ElementTree as ET
import json
import os

filename = None

current_dir = os.getcwd()
for file in os.listdir(current_dir):
    if file.startswith("preferences_global") and file.endswith(".xml"):
        filename = os.path.join(current_dir, file)

if not filename:
    filename = input("Enter the XML file name: ")

# Parse the XML file
tree = ET.parse(filename)
root = tree.getroot()

# Iterate through all <string> tags to find the one with JSON data
for string_tag in root.findall('string'):
    text = string_tag.text
    try:
        # Attempt to parse the text as JSON
        data = json.loads(text)
        # Check if "deviceRespBeen" exists in the JSON
        if "deviceRespBeen" in data:
            devices = data["deviceRespBeen"]
            # Process each device in the array
            for device in devices:
                print("-------------------------")
                print(f"Device Name:\t{device["name"]}\nLocalkey:\t{device["localKey"]}\nDevice ID:\t{device["devId"]}")
                print("-------------------------")
    except json.JSONDecodeError:
        continue
