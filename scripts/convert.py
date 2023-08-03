import json
import csv

def convert_to_geojson(json_data):
    geojson_data = {
        "type": "FeatureCollection",
        "features": []
    }

    for item in json_data:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [item["longitude"], item["latitude"]]
            },
            "properties": {
                "description": item["description"],
                "id": item["id"]
            }
        }
        geojson_data["features"].append(feature)

    return geojson_data

def create_geojson():
    with open("data/moments.json", "r") as json_file:
            data = json.load(json_file)

    geojson_data = convert_to_geojson(data)

    with open("data/moments.geojson", "w") as geojson_file:
        json.dump(geojson_data, geojson_file, indent=2)

    print("Data has been converted to GeoJSON and saved to moments.geojson")

def convert_to_csv(json_data):
    fieldnames = ["latitude", "longitude", "description", "id"]

    with open("data/moments.csv", "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(json_data)

def create_csv():
    with open("data/moments.json", "r") as json_file:
        data = json.load(json_file)

    convert_to_csv(data)

    print("Data has been converted to CSV and saved to moments.csv")