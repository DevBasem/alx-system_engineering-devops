#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced.basem:v1.0.0 (by /u/DevBasem)"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["data"]["subscribers"]
    except requests.RequestException as e:
        print("Error fetching data:", e)
        return 0
    except KeyError:
        print("Invalid subreddit or unexpected response format")
        return 0
