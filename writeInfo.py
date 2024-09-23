# Import packages
import APIrate as APIrate
import browser_cookie3 as browsercookie
import requests
import re  # Import regex module


# Get rat cookie from Firefox in this case
print("please log into the sea of thieves website while enabling keep logged in.")

# Example function that returns cookies based on the browser type
def get_browser_cookies(browser):
    # Replace these with your actual cookie retrieval logic
    browser_cookies = {
        "firefox": lambda: requests.utils.dict_from_cookiejar(browsercookie.firefox()),
        "edge": lambda: requests.utils.dict_from_cookiejar(browsercookie.edge()),
        "brave": lambda: requests.utils.dict_from_cookiejar(browsercookie.brave()),
        "chromium": lambda: requests.utils.dict_from_cookiejar(browsercookie.chromium()),
        "chromiumbased": lambda: requests.utils.dict_from_cookiejar(browsercookie.chromiumbased()),
        "opera_gx": lambda: requests.utils.dict_from_cookiejar(browsercookie.opera_gx()),
        "opera": lambda: requests.utils.dict_from_cookiejar(browsercookie.opera()),
    }
    
    return browser_cookies.get(browser, lambda: "Please check for spelling and try again.")()

# Input for browser
browser = input("Then write what browser you are using (supported: 'firefox', 'edge', 'brave', 'chromium', 'chromiumbased', 'opera_gx', 'opera'): ")

# Get the 'rat' cookie
rat = get_browser_cookies(browser).get('rat')
pirate = APIrate.Pirate(rat)
import os

def fetch_data():
    return pirate.get_profilev2("chest")

tags = ["Wheel", "Cannon", "Mast", "Capstan", "Figurehead", "HullLivery", "SailLivery"]

# Fetch ship data
data = fetch_data().get("chestData").get("Ship")

def clean_text(text):
    # Replace every non-ASCII character with a single quote
    return re.sub(r'[^\x00-\x7F]+', "'", text) if text else text

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
                    title = clean_text(entry.get('title', 'No Title'))
                    subtitle = clean_text(entry.get('subtitle', 'No Subtitle'))
                    image_url = entry.get('image', '')
                    wide_class = 'wide' if entry.get('wide', False) else ''

                    # Create each grid item
                    index_file.write(f'<div class="grid-item {wide_class}">\n')
                    index_file.write(f'  <img src="{image_url}" alt="{title}" style="width:100%;">\n')
                    index_file.write(f'  <h3>{title}</h3>\n')
                    index_file.write(f'  <p>{subtitle}</p>\n')
                    index_file.write('</div>\n')

        index_file.write('</div>\n</details>\n\n')

# Fetch clothing data
data = fetch_data().get("chestData").get("Vanity")

tags = ["Beard", "Hair", "Peg", "HairDye", "Liv_Tattoos", "Emote", "Eyepatch", "Hook", "Curses", "Liv_Makeup_Shop"]

with open("clothes.md", 'w') as index_file:
    index_file.write('<link rel="stylesheet" href="./style.css">\n\n')
    index_file.write('# Clothing Customization Categories\n\n')  # Updated title

    for tag in tags:
        index_file.write(f'<details>\n<summary><strong>{tag}</strong></summary>\n')
        index_file.write('<div class="grid-container">\n')

        # Filter the API data entries by the current tag
        for entry in data:
            if entry.get("#Type") == "ProfileGridItem":
                tags_list = entry.get("Taxonomy", {}).get("Tags", [])
                if any(tag_info.get("#Value") == tag for tag_info in tags_list):
                    title = clean_text(entry.get('title', 'No Title'))
                    subtitle = clean_text(entry.get('subtitle', 'No Subtitle'))
                    image_url = entry.get('image', '')
                    wide_class = 'wide' if entry.get('wide', False) else ''

                    # Create each grid item
                    index_file.write(f'<div class="grid-item {wide_class}">\n')
                    index_file.write(f'  <img src="{image_url}" alt="{title}" style="width:100%;">\n')
                    index_file.write(f'  <h3>{title}</h3>\n')
                    index_file.write(f'  <p>{subtitle}</p>\n')
                    index_file.write('</div>\n')

        index_file.write('</div>\n</details>\n\n')
