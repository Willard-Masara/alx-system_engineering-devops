#!/usr/bin/python3
"""
Basic api queries in python
"""

def number_of_subscribers(subreddit):
    """
    we query reddit using get and requests to get subscribers
    to the subreddit
    """
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
