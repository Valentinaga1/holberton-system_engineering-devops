#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of
subscribers"""

import json
import requests


def number_of_subscribers(subreddit):
    """Function to returns the number of subscribers"""

    url = "https://www.reddit.com/r/"
    response = requests.get(url + subreddit + "/about.json",
                            allow_redirects=False)
    # print(response)
    if response.status_code == 200:
        x = response.json().get("data").get("subscribers")
        return response.json().get("data").get("subscribers")
    else:
        return 0
