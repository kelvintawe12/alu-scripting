#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'after': after, 'limit': 100}  # Fetch a maximum of 100 posts per request

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            after = data['data']['after']

            # Append titles of the hot posts to hot_list
            for post in posts:
                hot_list.append(post['data']['title'])

            # If there are more pages, continue recursively
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            # Return None if the subreddit is invalid
            return None
    except requests.RequestException:
        # Return None if there are network-related issues
        return None


if __name__ == "__main__":
    # Testing can be done using the 2-main.py script
    pass
