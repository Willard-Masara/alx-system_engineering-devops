#!/usr/bin/python3
"""Module for task 3"""

import requests

def count_words(subreddit, word_list, word_count={}, after=None):
    """Queries the Reddit API and returns the count of words in
    word_list in the titles of all the hot posts
    of the subreddit"""
    
    # Reddit API endpoint for hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set parameters for pagination and API request
    params = {"after": after} if after else {}
    headers = {"User-Agent": "My-User-Agent"}

    # Make a GET request to the Reddit API
    response = requests.get(url, params=params, headers=headers, allow_redirects=False)
    
    # Check if the request was not successful (status code 200)
    if response.status_code != 200:
        return None

    # Parse the JSON response
    data = response.json()

    # Extract titles of hot posts
    hot_titles = [child.get("data").get("title") for child in data.get("data").get("children")]

    # If there are no hot titles, return None
    if not hot_titles:
        return None

    # Remove duplicates from word_list
    word_list = list(set(word_list))

    # Initialize word_count dictionary if not provided
    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    # Update word counts based on titles
    for title in hot_titles:
        split_words = title.split(' ')
        for word in word_list:
            word_count[word] += split_words.count(word.lower())

    # If there is no 'after', print the sorted word counts
    if not data.get("data").get("after"):
        sorted_counts = sorted(word_count.items(), key=lambda kv: (kv[1], kv[0].lower()), reverse=True)
        [print(f'{k}: {v}') for k, v in sorted_counts if v != 0]
    else:
        # Recursively call the function for the next page
        return count_words(subreddit, word_list, word_count, data.get("data").get("after"))


