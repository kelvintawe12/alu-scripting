#!/usr/bin/python3
"""
This module queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit. If the subreddit is invalid, it prints None.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If not a valid subreddit, prints None.

    Args:
        subreddit (str): The subreddit to search for

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'my-app/0.0.1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            # Print None if the subreddit is invalid (non-200 response)
            print(None)
    except requests.RequestException:
        # Print None in case of network-related issues
        print(None)


if __name__ == "__main__":
    # Testing can be done using the 1-main.py script
    pass
