#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""

import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursive function to get the lists of the hot tittles"""
    try:
        url = "https://www.reddit.com/r/"
        headers = {"User-Agent": "User Agent"}
        parameters = { "after": after}
        response = requests.get(url + subreddit + "/hot.json",
                                headers=headers, params=parameters, allow_redirects=False)
        r_json = response.json()
    except:
        return None
    
    if "data" in r_json and "children" in r_json.get("data"):
        for i in r_json.get("data").get("children"):
            hot_list.append(i.get("data").get("title"))
        if "after" in r_json.get("data") and r_json.get("data").get("after"):
            return recurse(subreddit, hot_list, r_json.get("data").get("after"))
        else:
            return hot_list
    else:
        return None
