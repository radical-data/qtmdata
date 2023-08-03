import requests
import json

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from {url}")
        return None

def print_progress(page, total_pages):
    percentage = 100 * page / total_pages
    print(f"Page {page}/{total_pages} processed ({round(percentage, 2)}%).")


def depaginate_data(base_url):
    page = 1
    moments = []

    while True:
        url = f"{base_url}?page={page}"
        data = fetch_data(url)

        if data is None:
            break

        moments.extend(data['moment_list'])

        print_progress(page, data['pages'])

        if data['current'] == data['pages']:
            break

        page += 1

    return moments

def scrape():
    base_url = "https://www.queeringthemap.com/moments"
    moments = depaginate_data(base_url)

    with open("data/moments.json", "w") as json_file:
        json.dump(moments, json_file, indent=4)

    print("Data has been collected and saved to moments.json")
