library(httr2)
library(jsonlite)
library(tidyverse)
response <- httr2::request("https://www.queeringthemap.com/moments") |>
  httr2::req_perform()
json <- httr2::resp_body_json(response)
total_pages <- json$pages |> as.numeric()
total_moments <- json$count |> as.numeric()

queeringthemap <- tibble("v1" = numeric(), "v2" = numeric(), "v3" = character(), "v4" = numeric())

for (i in 0:total_pages) {
  print(paste0("fetching page ", as.character(i), " (", 100*round(i/total_pages, 3), "%)"))
  url <- dplyr::if_else(i == 0, "https://www.queeringthemap.com/moments",
                 paste0("https://www.queeringthemap.com/moments?page=",i))
  response <- httr2::request(url) |>
    httr2::req_perform()
  json <- httr2::resp_body_json(response)
  to_add <- json$moment_list |>
    as_tibble(.name_repair = "minimal") |>
    t() |>
    as_tibble() |>
    mutate(across(everything(), unlist)) |>
    janitor::clean_names()
  queeringthemap <- queeringthemap |>
    add_row(to_add)
  print(to_add)
}

queeringthemap <- queeringthemap |>
  rename(latitude = v1,
         longitude = v2,
         content = v3,
         id = v4)

print(paste0("recieved ", nrow(queeringthemap), " out of ", total_moments, " moments"))

use_data(queeringthemap, overwrite = TRUE)
