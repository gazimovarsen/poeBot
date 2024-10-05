import requests
import math


def get_posts():
    # Define the API endpoint URL
    url = 'https://poe.ninja/api/data/itemoverview?league=Settlers&type=Scarab'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            full_list_scarab_prices = posts["lines"]
            for n in full_list_scarab_prices:
                if n["divineValue"] < 1 and n["name"] == "Harvest Scarab of Doubling":
                    print(math.ceil(n["chaosValue"]), n["name"])
                    return math.ceil(n["chaosValue"])
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:

        # Handle any network-related errors or exceptions
        print('Error:', e)
        return None


get_posts()
