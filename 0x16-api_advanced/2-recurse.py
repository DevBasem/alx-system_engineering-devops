#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list containing the titles of hot articles (default is an empty list).
        after (str): A token indicating the next page in the paginated response (default is None).

    Returns:
        list or None: A list containing the titles of hot articles, or None if no results are found.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    headers = {
        "User-Agent": "linux:28nMP2OF6Z7BDuB6fTRT3Q:v1.0 (by /u/DevBasem)"
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get("data", {}).get("children", [])
        if data:
            for post in data:
                hot_list.append(post["data"]["title"])
            after = response.json()["data"]["after"]
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    print("This script is meant to be imported and used. Please refer to 2-main.py.")
