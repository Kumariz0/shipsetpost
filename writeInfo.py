# import packages
import APIrate as APIrate
import browser_cookie3 as browsercookie
import requests
import json

# get rat cookie from firefox in this case
rat = requests.utils.dict_from_cookiejar(browsercookie.firefox()).get('rat')

pirate = APIrate.Pirate(rat)

import os

def fetch_data():
    return pirate.get_profilev2("chest")

tags = ["Wheel", "Cannon", "Mast", "Capstan", "Figurehead", "HullLivery", "SailLivery"]


data = fetch_data().get("chestData").get("Ship")

with open("shipsets.md", 'w') as index_file:
    index_file.write('<link rel="stylesheet" href="./style.css">\n\n')
    index_file.write('# Ship Customization Categories\n\n')

    for tag in tags:
        index_file.write(f'<details>\n<summary><strong>{tag}</strong></summary>\n')
        index_file.write('<div class="grid-container">\n')

        # Filter the API data entries by the current tag
        for entry in data:
            if entry.get("#Type") == "ProfileGridItem":
                tags_list = entry.get("Taxonomy", {}).get("Tags", [])
                if any(tag_info.get("#Value") == tag for tag_info in tags_list):
                    title = entry.get('title', 'No Title')
                    subtitle = entry.get('subtitle', 'No Subtitle')
                    image_url = entry.get('image', '')
                    wide_class = 'wide' if entry.get('wide', False) else ''

                    # Create each grid item
                    index_file.write(f'<div class="grid-item {wide_class}">\n')
                    index_file.write(f'  <img src="{image_url}" alt="{title}" style="width:100%;">\n')
                    index_file.write(f'  <h3>{title}</h3>\n')
                    index_file.write(f'  <p>{subtitle}</p>\n')
                    index_file.write('</div>\n')

        index_file.write('</div>\n</details>\n\n')


data = fetch_data().get("chestData").get("Vanity")

tags = ["Beard", "Hair", "Peg", "HairDye", "Liv_Tattoos", "Emote", "Eyepatch", "Hook", "Curses", "Liv_Makeup_Shop"]

with open("clothes.md", 'w') as index_file:
    index_file.write('<link rel="stylesheet" href="./style.css">\n\n')
    index_file.write('# Ship Customization Categories\n\n')

    for tag in tags:
        index_file.write(f'<details>\n<summary><strong>{tag}</strong></summary>\n')
        index_file.write('<div class="grid-container">\n')

        # Filter the API data entries by the current tag
        for entry in data:
            if entry.get("#Type") == "ProfileGridItem":
                tags_list = entry.get("Taxonomy", {}).get("Tags", [])
                if any(tag_info.get("#Value") == tag for tag_info in tags_list):
                    title = entry.get('title', 'No Title')
                    subtitle = entry.get('subtitle', 'No Subtitle')
                    image_url = entry.get('image', '')
                    wide_class = 'wide' if entry.get('wide', False) else ''

                    # Create each grid item
                    index_file.write(f'<div class="grid-item {wide_class}">\n')
                    index_file.write(f'  <img src="{image_url}" alt="{title}" style="width:100%;">\n')
                    index_file.write(f'  <h3>{title}</h3>\n')
                    index_file.write(f'  <p>{subtitle}</p>\n')
                    index_file.write('</div>\n')

        index_file.write('</div>\n</details>\n\n')