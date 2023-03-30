# create geojson
library(geojsonio)
queeringthemap_geojson <- geojsonio::geojson_write(
  queeringthemap |>
    # head() |>
    select(latitude, longitude, content),
  lat = "latitude",
  lon = "longitude",
  geometry = "point",
  type = "FeatureCollection",
  # convert_wgs84 = TRUE,
  # crs = 3857,
  precision = NULL,
  file = "data/queeringthemap.geojson"
)

# remove latitude and longitude in properties
# library(jsonlite)
# dat <- read_json("data/queeringthemap.geojson")
# dat$features


# usethis::use_data(queeringthemap_geojson, overwrite = TRUE)
