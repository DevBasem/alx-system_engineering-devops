#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "linux:28nMP2OF6Z7BDuB6fTRT3Q:v1.0 (by /u/DevBasem)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])
        if data:
            for post in data:
                print(post["data"]["title"])
        else:
            print("No posts found.")
    else:
        print(None)


if __name__ == "__main__":
    print("This is meant to be imported and used. Please refer to 1-main.py.")
