with open('../data/queeringthemap.geojson', 'r') as geojson:
  for item in geojson["features"]:
      del item["latitude"]
      del item["longitude"]

