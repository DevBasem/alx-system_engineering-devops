#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for
a given subreddit.
"""


import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:28nMP2OF6Z7BDuB6fTRT3Q:v1.0 (by /u/DevBasem)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json()["data"]["subscribers"]
    else:
        return 0


if __name__ == "__main__":
    print("This is meant to be imported and used. Please refer to 0-main.py.")
