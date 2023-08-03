from scripts.scrape import scrape
from scripts.convert import create_geojson, create_csv

scrape()
create_geojson()
create_csv()